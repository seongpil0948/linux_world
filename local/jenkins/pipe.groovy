pipeline {
    agent any
    
    environment {
        PROFILE = "dev"
        DOCKERHUB_CREDENTIALS = credentials('nexus_theshop')
        SSH_CREDENTIALS_ID = "10.101.91.139_ssh"
        SSH_HOST = "10.101.91.139"
        SSH_USER = "develop"
        SSH_REMOTE_NAME = "theshop_front_seller"
        BUILD_SCRIPT_CD = "/data/theshop_front_seller/script"
    }

    tools {
        nodejs 'nodejs-19.9.0'
        jdk "openjdk-17"
    }

    stages {
        stage('Prepare') {
            steps{
                sh 'npm install -g yarn'
                sh 'yarn config set @idsTrust:registry=http://npm.shop.co.kr/repository/npm/'
                sh 'yarn config set strict-ssl=false'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login  docker.shop.co.kr -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'   
            }
        }
        stage('Git Clone') {
            steps {
                echo 'Git Clone'
                git branch: 'development', credentialsId: 'gitlab', url: 'http://10.101.91.186:5001/ecommerceteam/theshop/frontend/new.theshop.front.git'
            }
        }
        
        stage('SonarQube analysis') {
            steps {
                withEnv(["JAVA_HOME=${tool 'openjdk-17'}", "PATH=${tool 'openjdk-17'}/bin:${env.PATH}"]) {
                    echo "JDK17 ============================="
                    echo "${tool 'openjdk-17'}"
                    sh 'java -version'
                    sh 'javac -version'
                    
                    script {
                        def scannerHome = tool 'SonarQubeScanner'
                            
                        withSonarQubeEnv("SonarServer") {
                            sh "${tool("SonarQubeScanner")}/bin/sonar-scanner \
                                    -Dsonar.projectKey=theshop-seller-key \
                                    -Dsonar.sources=. \
                                    -Dsonar.host.url=http://10.101.91.145:9000 \
                                    -Dsonar.token=sqp_b7dde17e1bb527e298415391dfb16a5ab2749946"
                        }
                    }
                }
            }
        }
     
        stage("Quality Gate") {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    script{
                        echo "Start~~~~"
                        def qg = waitForQualityGate()
                        echo "Status: ${qg.status}"
                        if(qg.status != 'OK') {
                            echo "NOT OK Status: ${qg.status}"
                            updateGitlabCommitStatus(name: "SonarQube Quality Gate", state: "failed")
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        } else{
                            echo "OK Status: ${qg.status}"
                            updateGitlabCommitStatus(name: "SonarQube Quality Gate", state: "success")
                        }
                        echo "End~~~~"
                    }
                }
            }
        }
        
        stage('Docker build') {
            steps {
                echo 'Docker Build'
                sh './deploy.sh $PROFILE'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    nodejs(nodeJSInstallationName: 'nodejs-19.9.0') {
                        sh 'npm install'
                        sh 'npx playwright install --with-deps'
                    }
                }
            }
        }

        stage('Run Playwright Tests') {
            steps {
                script {
                    nodejs(nodeJSInstallationName: 'nodejs-19.9.0') {
                        sh 'npx playwright test'
                    }
                }
            }
        }

        stage('SSH Build Shell Execute') {
            steps {
                script {
                    def cid = "$SSH_CREDENTIALS_ID"
                    def sshUser = "$SSH_USER"
                    def sshRemoteName = "$SSH_REMOTE_NAME"
                    def sshHost = "$SSH_HOST"
                    
                    withCredentials ([sshUserPrivateKey(credentialsId: cid, keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: sshUser)]) {
                        def remote = [:]
                        remote.name = sshRemoteName
                        remote.host = sshHost
                        remote.allowAnyHosts = true
                        remote.user = sshUser
                        remote.identityFile = identity
                       
                        sshCommand remote:remote, sudo:true, command: "$BUILD_SCRIPT_CD/deploy.sh $PROFILE"
                    }
                }
            }
        }

        /* 빌드 속도 저하로 제외 처리
        stage('Docker Clean') {
            steps {
                echo 'Docker <none> Images Delete'
                sh 'docker rmi $(docker images -f "dangling=true" -q)'
            }
        }
        */
    }
}
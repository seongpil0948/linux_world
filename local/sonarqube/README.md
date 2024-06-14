# Sonarqube
Sonarqube is an open source platform developed by SonarSource for continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs, code smells and security vulnerabilities on 20+ programming languages.

## Setup
SonarQube는 코드 품질과 보안을 분석하는 도구로, Jenkins와 통합하여 CI/CD 파이프라인의 일환으로 사용할 수 있습니다. 아래는 SonarQube를 설치하고 구성하는 방법에 대한 단계별 가이드입니다.

### 1. SonarQube 설치
SonarQube를 설치하는 방법은 여러 가지가 있지만, 여기서는 Docker를 사용한 방법을 설명하겠습니다.

#### Docker를 사용한 SonarQube 설치
1. **Docker 및 Docker Compose 설치** (이미 설치된 경우 이 단계는 건너뜁니다):
   ```sh
   sudo apt update
   sudo apt install docker.io
   sudo apt install docker-compose
   ```

2. **SonarQube 및 PostgreSQL 컨테이너 설정**:
   `docker-compose.yml` 파일을 생성하여 다음 내용을 추가합니다:
   ```yaml
   services:
     sonarqube:
       image: sonarqube:lts
       ports:
         - "9000:9000"
       environment:
         - sonar.jdbc.url=jdbc:postgresql://db:5432/sonarqube
         - sonar.jdbc.username=sonar
         - sonar.jdbc.password=sonar
     db:
       image: postgres:13
       environment:
         - POSTGRES_USER=sonar
         - POSTGRES_PASSWORD=sonar
         - POSTGRES_DB=sonarqube
   ```

3. **SonarQube 및 PostgreSQL 컨테이너 시작**:
   ```sh
   docker-compose up -d
   ```

4. **SonarQube 웹 UI에 접속**:
   - 브라우저에서 `http://<your_server_ip>:9000`으로 접속하여 SonarQube 웹 인터페이스에 접속합니다.
   - 기본 관리자 계정은 `admin` / `admin`입니다. 첫 로그인 시 비밀번호 변경을 요구할 수 있습니다.

### 2. SonarQube 프로젝트 생성
1. **SonarQube 로그인**:
   - `http://<your_server_ip>:9000`로 접속하고 로그인합니다.
   - 기본 관리자 계정은 `admin` / `admin`입니다.

2. http://localhost:9000/tutorials?id=test-jenkins&selectedTutorial=jenkins


### 3. Jenkins와 SonarQube 통합
Jenkins에서 SonarQube를 사용하여 코드 분석을 자동화하려면 다음 단계를 따르세요.

#### SonarQube 플러그인 설치
1. **플러그인 설치**:
   - Jenkins 대시보드에서 "Manage Jenkins" -> "Manage Plugins"로 이동합니다.
   - "Available" 탭에서 "SonarQube Scanner" 플러그인을 검색하여 설치합니다.

#### SonarQube 서버 구성
1. **SonarQube 서버 추가**:
   - Jenkins 대시보드에서 "Manage Jenkins" -> "Configure System"으로 이동합니다.
   - "SonarQube servers" 섹션을 찾아 "Add SonarQube"를 클릭합니다.
   - Name, Server URL, 서버 인증 토큰(앞서 생성한 프로젝트 토큰)을 입력합니다.

#### SonarQube Scanner 구성
1. **SonarQube Scanner 설치**:
   - Jenkins 대시보드에서 "Manage Jenkins" -> "Global Tool Configuration"으로 이동합니다.
   - "SonarQube Scanner" 섹션에서 "SonarQube Scanner installations" -> "Add SonarQube Scanner"를 클릭합니다.
   - 이름을 입력하고 자동 설치를 구성합니다.

#### Jenkins 프로젝트에 SonarQube 분석 추가
1. **Jenkins 프로젝트 구성**:
   - SonarQube 분석을 추가할 Jenkins 프로젝트를 엽니다.
   - "Build" 섹션에서 "Add build step"을 클릭하고 "Execute SonarQube Scanner"를 선택합니다.
   - 프로젝트 키, 소스 코드 위치, 기타 필요한 분석 파라미터를 입력합니다.

2. **파이프라인 프로젝트에서의 SonarQube 사용**:
   - 파이프라인 스크립트에서 SonarQube 분석 단계를 추가합니다. 예시는 다음과 같습니다:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Build') {
               steps {
                   // 빌드 스크립트
               }
           }
           stage('SonarQube analysis') {
               steps {
                   withSonarQubeEnv('My SonarQube Server') {
                       sh 'sonar-scanner -Dsonar.projectKey=my-project -Dsonar.sources=src -Dsonar.host.url=http://<your_server_ip>:9000 -Dsonar.login=<project_token>'
                   }
               }
           }
       }
   }
   ```

### 4. SonarQube 대시보드 확인
- Jenkins에서 빌드를 실행하면 SonarQube 분석이 자동으로 수행됩니다.
- SonarQube 대시보드에서 프로젝트를 선택하여 분석 결과를 확인할 수 있습니다.

위 단계를 따르면 Jenkins와 SonarQube를 성공적으로 구성하고 통합하여 코드 품질을 자동으로 분석할 수 있습니다.



## Reference
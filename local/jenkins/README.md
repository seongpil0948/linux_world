# Jenkins
젠킨스는 자동화된 테스트 및 빌드를 지원하는 오픈소스 CI/CD 도구이다.

## 용어
### Item (아이템)
아이템은 Jenkins에서 관리하는 모든 엔티티를 총칭하는 용어입니다. 
프로젝트, 폴더, 뷰, 파이프라인 등 여러 종류의 아이템을 생성하고 관리할 수 있습니다.

#### Project (프로젝트)
- 프로젝트는 Jenkins에서 실행할 수 있는 작업 단위를 의미합니다. 프로젝트는 코드 빌드, 테스트, 배포 등의 작업을 자동화하는 데 사용됩니다.
- Freestyle Project: 가장 기본적인 프로젝트 유형으로, 다양한 빌드 단계를 조합하여 사용할 수 있습니다.
- Pipeline Project: 파이프라인 스크립트를 통해 복잡한 빌드, 테스트, 배포 과정을 정의하고 관리할 수 있는 프로젝트입니다.

###  Pipeline (파이프라인)
- 파이프라인은 Jenkins에서 연속적 통합 및 연속적 배포(CI/CD) 프로세스를 자동화하기 위해 사용되는 스크립트 기반의 워크플로우입니다.
- Declarative Pipeline: 파이프라인 DSL(도메인 특화 언어)을 사용하여 쉽게 작성.
- Scripted Pipeline: Groovy 스크립트를 사용하여 더 복잡한 로직을 포함.
- https://www.jenkins.io/doc/book/pipeline/getting-started/
- https://plugins.jenkins.io/workflow-cps/

###  Folder (폴더)
폴더는 여러 프로젝트와 뷰를 그룹화하여 계층 구조로 관리할 수 있도록 하는 아이템입니다. 
폴더를 사용하면 프로젝트를 논리적으로 그룹화하여 관리하기 편리합니다.

### Multi-Configuration Project (다중 구성 프로젝트)
- Multi-Configuration Project는 다양한 구성(예: 여러 플랫폼, 여러 JDK 버전 등)에서 동일한 빌드를 수행할 수 있는 프로젝트 유형입니다. 매트릭스 프로젝트라고도 합니다.
- 예: 여러 운영 체제에서 동일한 테스트를 실행하거나, 여러 데이터베이스 버전에서 동일한 애플리케이션을 테스트하는 경우.

### Multibranch Pipeline (멀티브랜치 파이프라인)
- Multibranch Pipeline은 Git 등의 소스 코드 저장소의 여러 브랜치에 대해 자동으로 파이프라인을 생성하고 관리하는 프로젝트입니다.
- 각 브랜치마다 별도의 파이프라인을 설정할 필요 없이 브랜치가 추가될 때마다 자동으로 파이프라인을 생성합니다.

### View (뷰)
- 뷰는 Jenkins에서 프로젝트를 논리적으로 그룹화하여 표시하는 방법을 정의하는 아이템입니다.

### Agent (에이전트)
- 에이전트는 Jenkins에서 빌드를 실행하는 노드를 의미합니다. 에이전트는 마스터 노드와 통신하여 빌드를 실행하고 결과를 전달합니다.
- 에이전트는 마스터 노드와 동일한 서버에서 실행할 수도 있고, 다른 서버에서 실행할 수도 있습니다.
- 에이전트는 노드라고도 불립니다.

### Job (잡)
- 잡은 Jenkins에서 실행할 수 있는 작업 단위를 의미합니다. 프로젝트, 빌드, 파이프라인 등 여러 종류의 잡을 생성하고 관리할 수 있습니다.



## Refer
- [install with local](https://www.jenkins.io/doc/book/installing/docker/)
- https://www.jenkins.io/doc/book/using


## setup-wizard
[링크](https://www.jenkins.io/doc/book/installing/docker/#setup-wizard)
```
 *  Executing task: docker logs --tail 1000 -f dc49da7335eb90650543b0db3c50057b5137fe6136f8601e33c5c8aaf982ebb8 

Running from: /usr/share/jenkins/jenkins.war
webroot: /var/jenkins_home/war
2024-06-14 01:39:52.102+0000 [id=1]     INFO    winstone.Logger#logInternal: Beginning extraction from war file
2024-06-14 01:39:52.458+0000 [id=1]     WARNING o.e.j.s.handler.ContextHandler#setContextPath: Empty contextPath
2024-06-14 01:39:52.478+0000 [id=1]     INFO    org.eclipse.jetty.server.Server#doStart: jetty-10.0.20; built: 2024-01-29T20:46:45.278Z; git: 3a745c71c23682146f262b99f4ddc4c1bc41630c; jvm 17.0.11+9
2024-06-14 01:39:52.564+0000 [id=1]     INFO    o.e.j.w.StandardDescriptorProcessor#visitServlet: NO JSP Support for /, did not find org.eclipse.jetty.jsp.JettyJspServlet
2024-06-14 01:39:52.579+0000 [id=1]     INFO    o.e.j.s.s.DefaultSessionIdManager#doStart: Session workerName=node0
2024-06-14 01:39:52.750+0000 [id=1]     INFO    hudson.WebAppMain#contextInitialized: Jenkins home directory: /var/jenkins_home found at: EnvVars.masterEnvVars.get("JENKINS_HOME")
2024-06-14 01:39:52.788+0000 [id=1]     INFO    o.e.j.s.handler.ContextHandler#doStart: Started w.@161f6623{Jenkins v2.452.2,/,file:///var/jenkins_home/war/,AVAILABLE}{/var/jenkins_home/war}
2024-06-14 01:39:52.792+0000 [id=1]     INFO    o.e.j.server.AbstractConnector#doStart: Started ServerConnector@3a1dd365{HTTP/1.1, (http/1.1)}{0.0.0.0:8080}
2024-06-14 01:39:52.796+0000 [id=1]     INFO    org.eclipse.jetty.server.Server#doStart: Started Server@f001896{STARTING}[10.0.20,sto=0] @876ms
2024-06-14 01:39:52.796+0000 [id=27]    INFO    winstone.Logger#logInternal: Winstone Servlet Engine running: controlPort=disabled
2024-06-14 01:39:52.863+0000 [id=35]    INFO    jenkins.InitReactorRunner$1#onAttained: Started initialization
2024-06-14 01:39:53.502+0000 [id=43]    INFO    jenkins.InitReactorRunner$1#onAttained: Listed all plugins
2024-06-14 01:39:53.589+0000 [id=35]    SEVERE  jenkins.InitReactorRunner$1#onTaskFailed: Failed Loading pl

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

e881740752ea43828d7d20619de830f5

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
```

### Create First Admin User
- User name: seongpil0948
- Full name: SeongpilChoi
- Email: seongpil0948@gmail.com
- PW: 1234qwer!!

### Instance Configuration
*Jenkins URL:http://localhost:8080/*  
The Jenkins URL is used to provide the root URL for absolute links to various Jenkins resources. That means this value is required for proper operation of many Jenkins features including email notifications, PR status updates, and the BUILD_URL environment variable provided to build steps.
The proposed default value shown is not saved yet and is generated from the current request, if possible. The best practice is to set this value to the URL that users are expected to use. This will avoid confusion when sharing or viewing links.
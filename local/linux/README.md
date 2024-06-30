# Docker 를 이용하여 Ubuntu 환경 구축
어떤 목적으로든 Docker를 사용하면 호스트 시스템에 영향을 주지 않고 리눅스 환경을 쉽게 구축할 수 있습니다.

## Step

### Pre-requisite
- Docker 설치

### 1. Build Image
```sh
sh ./build.sh
```

### 2. Run Container
```sh
sh ./ignite.sh
```

### 3. Connect to Container
```sh
ssh root@localhost -p 2222
```
password는 `Dockerfile`에 정의된 `root` 계정의 비밀번호입니다.

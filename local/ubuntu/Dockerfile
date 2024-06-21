# 기본 Ubuntu 이미지를 사용
FROM ubuntu:latest

LABEL description="Local Linux Development Environment"

# 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive

# 작업 디렉토리 설정 및 파일 복사
WORKDIR /app
COPY ./app /app

# 필요한 패키지 설치 및 로케일 설정
RUN apt-get update && apt-get install -y \
    locales \
    net-tools \
    iputils-ping \
    curl \
    wget \
    vim \
    dnsutils \
    sudo \
    git \
    openssh-server \
    && locale-gen ko_KR.UTF-8 \
    && update-locale LANG=ko_KR.UTF-8 \
    && apt-get clean

# 로케일 환경 변수 설정
ENV LANG=ko_KR.UTF-8 \
    LANGUAGE=ko_KR:ko \
    LC_ALL=ko_KR.UTF-8

# SSH 서버 설정
RUN mkdir /var/run/sshd \
    && echo 'root:root' | chpasswd \
    && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && echo 'export LANG=ko_KR.UTF-8' >> /etc/default/locale

RUN echo 'root:1234qwer!!' | chpasswd

# 포트 22 열기
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]
# -D: 데몬으로 실행하지 않고 프로세스로 실행
# -e: 로그를 표준 오류로 출력(for logging)
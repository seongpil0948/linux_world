# 기본 Ubuntu 이미지를 사용
FROM ubuntu:latest

LABEL description="Local Linux Development Environment"
# 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive
COPY ./app /app
WORKDIR /app

# 로케일 설정을 위해 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    locales \
    && locale-gen ko_KR.UTF-8 \
    && update-locale LANG=ko_KR.UTF-8

# 네트워킹 관련 패키지 설치
RUN apt-get update && apt-get install -y \
    net-tools \
    iputils-ping \
    curl \
    wget \
    vim \
    dnsutils \
    && apt-get clean

# 로케일 환경 변수 설정
ENV LANG=ko_KR.UTF-8 \
    LANGUAGE=ko_KR:ko \
    LC_ALL=ko_KR.UTF-8

# 필요한 추가 패키지 설치 (예: vim, curl 등)
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    && apt-get clean

# # 필요 패키지 설치 및 SSH 서버 설정
# RUN apt-get update && apt-get install -y \
#     openssh-server \
#     sudo \
#     && mkdir /var/run/sshd \
#     && echo 'root:root' | chpasswd \
#     && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
#     && sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
#     && echo 'export LANG=C.UTF-8' >> /etc/default/locale
# # SSH 서버 실행
# CMD ["/usr/sbin/sshd", "-D"]

# 기본 명령어 설정
CMD ["bash"]

# 포트 22 열기
EXPOSE 22


# 유지보수를 위해 지정된 포트를 열기 (예: SSH)
EXPOSE 22
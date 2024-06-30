#!/bin/bash
echo "start first process"

/usr/sbin/sshd -D -e
# -D: 데몬으로 실행하지 않고 프로세스로 실행
# -e: 로그를 표준 오류로 출력(for logging)
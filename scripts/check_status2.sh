
echo "r/s, w/s rkB/s, wkB/s: read 요청과 write 요청, read kB/s, write kB/s를 나타낸다. \n
    어떤 요청이 가장 많이 들어오는지 확인해볼 수 있는 중요한 지표다. 성능 문제는 생각보다 과도한 요청때문에 발생하는 경우도 있기 때문이다. \n\n
    await: I/O처리 평균 시간을 밀리초로 표현한 값이다. \n
    application한테는 I/O요청을 queue하고 서비스를 받는데 걸리는 시간이기 때문에 application이 이 시간동안 대기하게 된다. \n
    일반적인 장치의 요청 처리 시간보다 긴 경우에는 블럭장치 자체의 문제가 있거나 장치가 포화된 상태임을 알 수 있다.\n"
iostat -xz 1


echo "
이 값은 TCP 통신량을 요약해서 보여준다.

active/s: 로컬에서부터 요청한 초당 TCP 커넥션 수를 보여준다 (예를들어, connect()를 통한 연결).
passive/s: 원격으로부터 요청된 초당 TCP 커넥션 수를 보여준다 (예를들어, accept()를 통한 연결).
retrans/s: 초당 TCP 재연결 수를 보여준다.
active와 passive 수를 보는것은 서버의 부하를 대략적으로 측정하는데에 편리하다. 위 설명을 보면 active를 outbound passive를 inbound 연결로 판단할 수 있는데, 꼭 그렇지만은 않다. (예를들면 localhost에서 localhost로 연결같은 connection)

retransmits은 네트워크나 서버의 이슈가 있음을 이야기한다. 신뢰성이 떨어지는 네트워크 환경이나(공용인터넷), 서버가 처리할 수 있는 용량 이상의 커넥션이 붙어서 패킷이 드랍되는것을 이야기한다. 위 예제에서는 초당 하나의 TCP 서버가 들어오는것을 알 수 있다.
"
sar -n TCP,ETCP 1
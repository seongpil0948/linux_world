# Refer:  https://velog.io/@dojun527/쿠버네티스-인그레스Ingress

# 외부 클라이언트 환경 접속
## ingress-nginx-controller NodePort(HTTP 접속용) 변수 지정
$ export IngHttp=$(kubectl get service -n ingress-nginx ingress-nginx-controller -o jsonpath='{.spec.ports[0].nodePort}')
$ echo $IngHttp


## 인그레스 접속 테스트
$ curl <마스터노드 IP>:<Nginx Controller 의 Service 의 NodePort 중 HTTP 접속용>
# svc1-web 접속
$ curl -s 192.168.10.10:$IngHttp


# svc2-web 접속
$ curl -s 192.168.10.10:$IngHttp/guest

# 부하분산 테스트
$ for i in {1..100}; do curl -s 192.168.10.10:$IngHttp/guest ; done | sort | uniq -c | sort -nr
$ for i in {1..1000}; do curl -s 192.168.10.10:$IngHttp/guest ; done | sort | uniq -c | sort -nr
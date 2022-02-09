# SSHTunnelForwarder
how to access mysql DB of private server

SSHTunnrulForwarder를 통해 SSH 터널링 되고 나면 remote_bind_adress 는 localhost가 된다. 
이후 db_port를 입력하면 해당 SSH 터널링이 해당 IP로 가게 된다.
pymysql은 마치 로컬에서 작동하는 것과 같이 된다. 따라서 pymysql의 host 는 로컬이 되고 user와 pwd는 정해둔 값을 사용.
db='db_naver' 에서 db 의 이름을 사용하면 된다.

argparse 는 추후 수정...

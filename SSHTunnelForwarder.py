import pymysql
from sshtunnel import SSHTunnelForwarder
import argparse


# parser = argparse.ArgumentParser(description='choose the column')
# parser.add_argument('-g', '--group_id', type=str, help='type group_id (ex : Naver)')
# parser.add_argument('-v', '--face_vec', type=list, help='face_vector list (ex [0.0172, -0.565...]')
# args = parser.parse_args()

# group_id = args.group_id

if __name__ == '__main__':
    with SSHTunnelForwarder(('ip', port), # ex: 111.11.11.11, 22
                            ssh_username='naver', #username
                            ssh_pkey='naver.pem', #ssh_key의 위치
                            remote_bind_address=('127.0.0.1', db_port)) as tunnel: #dp_port ex: 1111
        with pymysql.connect(host='127.0.0.1', user='naver', password='naver', port=tunnel.local_bind_port,
                             db='db_naver', charset="utf8", cursorclass=pymysql.cursors.DictCursor) as conn:
            with conn.cursor() as cur:
                sql = '''select naver_id, naver_pwd from naver_member where group_id = "Naver"'''
                cur.execute(sql)
                print(sql)
                results = cur.fetchall()
                for result in results:
                    print(result['naver_pwd'])

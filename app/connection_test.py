import os
import cx_Oracle

oracle_hostname = os.environ.get('hostname')
oracle_port = os.environ.get('port', '1521')
oracle_instance = os.environ.get('instance')
oracle_username = os.environ.get('username')
oracle_password = os.environ.get('password')

connection_string = '{username}/{password}@{hostname}:{port}/{instance}'.format(
    username=oracle_username,
    password=oracle_password,
    hostname=oracle_hostname,
    port=oracle_port,
    instance=oracle_instance,
)

con = cx_Oracle.connect(connection_string)
print(con.version)

con.close()

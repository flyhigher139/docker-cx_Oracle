import cx_Oracle

con = cx_Oracle.connect('system/oracle@172.19.0.2:1521/XE')
print(con.version)

con.close()

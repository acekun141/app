import cx_Oracle
connect = cx_Oracle.connect('travis/travis@localhost:1521/XE')
cursor = connect.cursor()
result1 = cursor.execute('SELECT * FROM auth_user').fetchall()
print(result1)

import cx_Oracle
connect = cx_Oracle.connect('travis/travis@localhost:1521/XE')
cursor = connect.cursor()
result1 = cursor.execute('SELECT * FROM auth_user').fetchall()
result2 = cursor.execute('SELECT * FROM auth_group').fetchall()
print(result1)
print(result2)

from Connect import Connect

db=Connect("sample")
mydb=db.GetConnect()
cursor=mydb.cursor()
cursor.execute("SHOW DATABASES")
databases=cursor.fetchall()
print(databases)
#cursor.execute("DROP TABLE users")
'''cursor.execute("CREATE TABLE users(id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),user_name VARCHAR(255))")'''
cursor.execute("DESC users")
userdesc=cursor.fetchall()
print(userdesc)

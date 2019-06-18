import mysql.connector as mysql
class Connect:
	mydb=None
	def __init__(self,database=None):
		self.mydb=mysql.connect(host='localhost',user='root',passwd='Code@mispl',
		database=database)
	
	def GetConnect(self):
		return self.mydb 




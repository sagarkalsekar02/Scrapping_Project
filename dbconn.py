import pyodbc
import sys
from datetime import datetime
class dbconn:

	def __init__(self):
		try:
			conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'Server=.;'
                          'Database=SVOD_UK_prac;'
                          'Trusted_Connection=yes;')
			self.cur=conn.cursor()

		except pyodbc.Error as ex:
			print(ex)
			sys.exit()

	def Scrapping_Status(self):
		try:
			status_dict={}
			query="SELECT Channel_Id,ProgramLinkScrapping,DataScrapping FROM  dbo.ScrappingStatus where Channel_Id='ITV'"
			self.cur.execute(query)
			row = self.cur.fetchone()
			status_dict.update(ProgramLinkScrapping=row.ProgramLinkScrapping,DataScrapping=row.DataScrapping)
			return status_dict

		except pyodbc.Error as ex:
			print(ex)
			sys.exit()

	def insert_platformlinks(self,el1,els,elstitle,categ):
		try:
			dateobj=datetime.now()
			query="INSERT INTO dbo.PlatFormLinks(ScrappedLink,IsScrapped,CreatedOn,ModifiedOn,Channel_Id,Category,Title,PageLink) VALUES (?,?,?,?,?,?,?,?)"
			self.cur.execute(query,(els,None,dateobj,None,"ITV",categ,elstitle,el1))
			self.cur.commit()
		except pyodbc.Error as ex:
			print(ex)
			sys.exit()

	def update_status(self,column,value):
		try:
			query="UPDATE dbo.ScrappingStatus SET {} = '{}' WHERE Channel_Id='ITV'"
			self.cur.execute(query.format(column,value))
			self.cur.commit()
		except pyodbc.Error as ex:
			print(ex)
			sys.exit()


'''
	conn = pyodbc.connect(
	 'Driver={SQL Server};'
	 'Server=.;'
	 'Database=SVOD_UK_prac;'
	 'Trusted_Connection=yes;')
'''



d1=dbconn()





	
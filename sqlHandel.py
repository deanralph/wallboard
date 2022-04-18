# sqlHandle v1
# Dean Ralph
# Jan 2020

# Description:
# Designed to interface between python and MySQL
# Create a connection object in your main code by passing the appropiate
# creds and then use the pre-defined functions to manipulate the database

#Imports
import pymssql

#Main Code

class MSSQL:

    def __init__(self, server, dbusername, dbpassword, dbname):
        self.con = pymssql.connect(server, dbusername, dbpassword, dbname)

    def getServers():
        cur = self.con.cursor(as_dict=True)
        cur.execute(f"select * from servers;")
        return cur.fetchall()

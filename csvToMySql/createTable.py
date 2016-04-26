#!python3 

import sys
import mysql.connector

databaseName = 'audit'
userName = 'auditWriter'
pwd = 'writer'
cnx =  mysql.connector.connect(user=userName, password=pwd,
                              host='127.0.0.1',
                              database=databaseName)
cnx.close()

# !!!!!!!!!  TODO !!!!!!!!!!!!!!!!!
#!/usr/bin/env python3

#basic python wrapper for SQL queries
'''
Program:Wrapper for SQL queries
File:python_query_tests.py
Version:1.0
Date:May-4-2019
Function: to wrap SQL queries in python language
Author: Yobi Livingstone, Documentaiton Header(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------
Usage:
--------------------------------------------------------------------------
Revision History:
--------------------------------------------------------------------------
Import libraries
import pymysql.cursors
'''
import pymysql.cursors

# Set parameters
dbname   = "ly001"
dbhost   = "ssh.cryst.bbk.ac.uk" #Replace ssh with hope when working from nomachine
dbuser   = "ly001"   # Ask a demonstrator
dbpass   = "7#b8tpkum"   # Ask a demonstrator
port     = 3306


# Create search function
def search_function(output_type, input_type, input_value):
  """ Search Function"""
  sql = "select" + output_type + "where" + input_type + " == " + input_value   

# Connect to the database
db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

# Create a cursor and execute the SQL on it
cursor = db.cursor()
data  = cursor.execute(sql)

# We know there is only one row returned to fetch it and print the data
output_value   = cursor.fetchone()
print (data[0])
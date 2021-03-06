#!/usr/bin/env python3


"""
Program:SQL Python Functions
File:SQL_python_functions.py
Version:1.0
Date:May-6-2019
Author: Yobi Livingstone, Margharita Martorama. Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Functions to perfrom query in the database
--------------------------------------------------------------------------
Usage: For Database Query and setting up database summary
--------------------------------------------------------------------------
Import libraries: import pymysql.cursors
"""
import pymysql.cursors
import sys

sys.path.insert(0,'../../createdb/')
        
""" Data Base Query Function"""
def db_query(output_type, input_type, input_value):
        """Retreive search query when given query parameters;
        output_type, input_type and input_value, provided by the webuser
        input= output_type, input_type, input_value
        query parameters for data retrieval
        output= output_value within the provided parameters
        """
        
        dbname   = "ly001"
        dbhost   = "ssh.cryst.bbk.ac.uk"
        dbuser   = "ly001"   
        dbpass   = "7#b8tpkum"  
        port     = 3306
        db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
                
        sql = "select "+output_type+" from CHROM8 where "+input_type+"='"+input_value+"'"
        cursor = db.cursor()
        data  = cursor.execute(sql)
        output_value   = cursor.fetchall()
        return output_value


""" Data Base Summary Function"""
def db_summary(output_type):
        '''select (*)
        Returning entire record assoiciated with Accession no.
        '''
        dbname   = "ly001"
        dbhost   = "ssh.cryst.bbk.ac.uk" 
        dbuser   = "ly001"   
        dbpass   = "7#b8tpkum"  
        port     = 3306
        db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)
        
        sql="select "+output_type+" from CHROM8"
        cursor = db.cursor()
        data  = cursor.execute(sql)
        output_value   = cursor.fetchall()
        return output_value

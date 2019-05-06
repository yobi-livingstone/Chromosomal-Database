#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Start CDS
File:doStartCDS.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to process start CDS region
--------------------------------------------------------------------------
Import libraries:
import re
import getLocationCDS
"""
import re
import getLocationCDS

def getStartCDS(input_value, input_value):
      """ Process CDS from the getLocationCDS
     Input: input type and vaule in cofig 
     Output:CDS start Coordinate """

     x = getLocationCDS(input_value, input_value)
     coordinate_start = re.findall(r'(\d+)\-', x)

     return coordinate_start
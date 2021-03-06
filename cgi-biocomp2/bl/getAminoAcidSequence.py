#!/usr/bin/env python3
"""
Program:Amino Acid Sequence
File:getAminoAcidSequence.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Function for getting amino acid sequence from the database 
--------------------------------------------------------------------------
imported Libraries:
from SQL_python_functions import db_query
from config import config as cg
import sys
"""
from SQL_python_functions import db_query
from config import config as cg
import sys

sys.path.insert(0, '../db/')
sys.path.insert(0, '../')

#"""Get AMino Scid Sequence"""
def getAminoAcidSequence(input_type, input_value):
     """ Function to obtain Amino Acid Sequence  from the database
     input: database query Arg5, type, and value from the config file
     output:Amino Acid Sequence from database"""
     amino_acid_sequence = db_query(cg.dbArg5, input_type, input_value)
     
     return amino_acid_sequence

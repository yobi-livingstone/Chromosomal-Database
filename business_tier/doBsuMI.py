#!/usr/bin/env python3
#from database_layer import db_query

"""
Program:Restriction Enzyme with BsuMI
File:doBsuMI.py
Version:1.0
Date:May-5-2019
Author: Margherita Martorana, Documentation headers(Jeff Li)
Address: Biological Sciences, Birkbeck ...
--------------------------------------------------------------------------
Description: Funciton to process DNA sequence with restriciton enzyme BsuMI
--------------------------------------------------------------------------
from configFile import *
import re
"""

from configFile import *
import re

def doBsuMI(seq):
     """ Process Sequence with restriction enzyme EcoRi
     Input: input ecoRI from cofigfile 
     Output:Sequence """
     f = re.compile(r'' + bsuMI_forward + '')
     r = re.compile(r'' + bsuMI_reverse + '')
     seq = f.sub(bsuMI_forward[0] + bsuMI_char + \
                 bsuMI_forward[1:len(bsuMI_forward)], seq)
     seq = r.sub(bsuMI_reverse[0] + bsuMI_char + \
                 bsuMI_reverse[1:len(bsuMI_reverse)], seq)
     return seq
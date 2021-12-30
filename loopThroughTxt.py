# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:59:27 2021

@author: akash
"""

import os
import time

textRoot = 'txtFiles/'



fileList = os.listdir(textRoot)

for f in fileList:
    first_char = open(textRoot+f, "r").read(1)
    # print(first_char)
    
    if first_char != '0':
        os.rename(textRoot+f , textRoot+str(int(time.time()))+'.txt' )
print(" Done")
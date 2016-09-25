# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 20:23:19 2016

@author: Administrator
"""

import time 
import os
for i in range(0,30):
    print(i*" "+"   #   #  #   #   # #      #  #   #   #   #     #       ###         ")
    print(i*" "+"    # #   #   #  #   #     #  #   #   #   #    # #     #   #        ")
    print(i*" "+"     #    #   # #   # #    #  #   #   #####   #####   #     #       ")
    print(i*" "+"    # #   #   #   # #      #  #   #   #   #   #   #    #   #        ")
    print(i*" "+"   #   #   # #         #   #   # #    #   #   #   #     ###         ") 
    time.sleep(0.1)
    i = os.system('cls')  
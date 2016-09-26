# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:06:40 2016

@author: Administrator
"""
import time 
import os
os.system('cls')


a01="           # # # # # # # # #                    "
a02="           #               #                    "
a03="           #   ##     ##   #                    "
a04="           #    $     $    #                    "
a05="           #       *       #                    "
a06="           #    _______    #                    "
a07="           #    |_| |_|    #                    "
a08="           #               #                    "
a09="           # # # # # # # # #                    "
                                                      

a=[a01,a02,a03,a04,a05,a06,a07,a08,a09]
for i in a:
    print(i)
time.sleep(1.0)   
i=os.system('cls')
b01="           # # # # # # # # #               "
b02="           #               #               "
b03="           #   __      #   #               "
b04="           #  |__|   > #   #               "
b05="           #   __|  *      #               "
b06="           #  |__|   > #   #               "
b07="           #           #   #               "
b08="           #               #               "
b09="           # # # # # # # # #               "

b=[b01,b02,b03,b04,b05,b06,b07,b08,b09]
for i in b:
    print(i)
time.sleep(1.0)   
i=os.system('cls')
a.reverse()
for i in a:
    print(i)
time.sleep(1.0)   
i=os.system('cls')
b.reverse()
for i in b:
    i=i[::-1]
    print(i)
time.sleep(1.0)   
i=os.system('cls')












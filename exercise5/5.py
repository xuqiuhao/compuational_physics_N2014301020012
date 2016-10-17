# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:43:36 2016

@author: Administrator
"""
import math
import pylab as pl
class canon_trajectory:
    def __init__(self,time_step=0.05,v0=500,g0=9.8,angle_of_depature=45):
        self.i=0
        self.x=[0]
        self.y=[0]
        self.t=[0]
        self.dt = time_step
        self.angle=angle_of_depature/180*math.pi
        self.Vx=[v0*math.cos(angle_of_depature/180.0*math.pi)]
        self.Vy=[v0*math.sin(angle_of_depature/180.0*math.pi)]
        self.g=g0
    def trajectory(self):
        while(self.y[-1]>=0):
            
             temp_Vx=self.Vx[self.i]
             temp_Vy=self.Vy[self.i]-self.g*self.dt
             self.Vx.append(temp_Vx)
             self.Vy.append(temp_Vy)
             temp_x=self.x[self.i]+temp_Vx*self.dt
             temp_y=self.y[self.i]+temp_Vy*self.dt
            
             temp_t=self.t[self.i]+self.dt
            
             self.x.append(temp_x)
             self.y.append(temp_y)
             temp_t=self.t[self.i]+self.dt
             self.t.append(temp_t)
             self.i=self.i+1
             
           
          
             
    def show_result(self):
        pl.plot(self.x,self.y)
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")
        pl.show()
    def store_result(self):
        datafile=open("cannon_data.txt","w")
        for j in range(len(self.t)):
            print('self.t[j],self.x[j],self.y[j],file=datafile')
        datafile.close()  
        
class test_result_NO1(canon_trajectory):
    def draw_a_line(self):
        a=canon_trajectory()
        a.trajectory()
        a.show_result()
        a.store_result
a=test_result_NO1()
a.draw_a_line()  


#the next code is programmed to find the angle of depature that maximize the range.
class test_result_NO2(canon_trajectory):
    def draw_90_lines(self):
        a=1
        for i in range(40):
            b=canon_trajectory(angle_of_depature=a)
            b.trajectory()
            b.show_result()
            a=a+2
b=test_result_NO2()
b.draw_90_lines()
        


        
        
                                                                                 
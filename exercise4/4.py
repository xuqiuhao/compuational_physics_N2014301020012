# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 15:24:00 2016

@author: Administrator
"""

import pylab as pl
class decay_AB:
    def __init__(self,number_of_nucleiA=100,number_of_nucleiB=0,time_constant=1,time_of_duration=5,time_step=0.05):
        self.NA = [number_of_nucleiA]
        self.NB = [number_of_nucleiB]
        self.t =[0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step+1)
        print("Initial number of nucleiA ->", number_of_nucleiA)
        print("Initial number of nucleiB ->", number_of_nucleiB)
        print("Time constant ->", time_constant)
        print("time step ->", time_step)
        print("total time ->", time_of_duration)
         
    def calculate(self):
        for i in range(self.nsteps):
            tmp=self.NA[i]+(self.NB[i]-self.NA[i])/self.tau*self.dt
            tmb=self.NB[i]+(self.NA[i]-self.NB[i])/self.tau*self.dt
            self.NA.append(tmp)
            self.NB.append(tmb)
            self.t.append(self.t[i]+self.dt)
    def show_result(self):           
        plot1,= pl.plot(self.t,self.NA,'b')
        plot2,= pl.plot(self.t,self.NB,'r')
        pl.xlabel('Time($s$)')
        pl.ylabel('Numble of Nuclei')
        pl.title('Decay of Two Nuclei')
        pl.legend([plot1, plot2], ['nucleiA', 'nucleiB'], loc="best")
        pl.show()
    def store_results(self):
        myfile = open('data_of_problem1.5.txt', 'w')
        for i in range(len(self.t)):
            print('self.t[i], self.NA[i],self.NB[i], file = myfile')
        myfile.close()
a=decay_AB()
a.calculate()
a.show_result()
a.store_results()
            
            
  
  
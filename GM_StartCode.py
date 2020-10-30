#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 11:00:58 2020

@author: 

Template for making OOP code
"""

import turtle, random, time
turtle.colormode(255)
turtle.tracer(0)

# =============CLASSES============

class Manager:
    def __init__(self):
        self.panel=turtle.Screen()
        self.w=900
        self.h=900
        turtle.setup(self.w,self.h)
        
        # bring in your global variables and initial setup tasks here
        # try to put as many setup tasks into methods and define them OUTSIDE
        # of the init method
        
        
        
        
        # call methods you want to run AS SOON AS YOUR GAME STARTS here
        self.main()
        
    def main(self):
        # copy and paste the ACTIONS that happened BELOW all of your classes 
        # in PC08 here (this is things like instantiating objects, calling
        # methods, etc.)
        
        
        
        
        self.panel.mainloop() # keep listeners on
        
# Copy and paste BOARD class here




# Copy and paste PLAYER class here




# instantiate Manager object here




# call Manager methods here:
game = Manager()
    
turtle.done()

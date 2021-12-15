# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:15:46 2021

@author: hakantandogdu
"""
from fiveDigit import FiveDigit

class Guess(FiveDigit):
    '''Guess object has three attributes; figure, heritaded 
    from parent class FiveDigit and two news: in_place and 
    out_place'''
    
    def __init__(self):
        FiveDigit.__init__(self)
        self.in_place = None
        self.out_place = None
        
    def compare_p(self,other):
        '''Compares two objects' figures and returns 
        the number of in place digits'''
        t = 0
        for x, y in zip(self.figure, other.figure):
            if x == y:
                t += 1       
        return t
    
    def compare_n(self,other):
        '''Compares two objects' figures and returns 
        the number of common digits'''
        t = 0
        for char in self.figure:
            if char in other.figure:
                t -= 1
        return t
    
    def get_in_place(self):
        return self.in_place
    
    def get_out_place(self):
        return self.out_place

    def set_in_place(self,other):
        '''Set in_place attribute for simulation or 
        while playing a game'''
        in_place = self.compare_p(other)
        self.in_place = in_place
        
    def set_in_place_forced(self,in_place):
        '''Set manualy in_place attribute '''
        self.in_place = in_place
        
    def set_out_place(self,other):
        '''Set out_place attribute for simulation or 
        while playing a game'''
        out_place = self.compare_n(other) + self.in_place
        self.out_place = out_place
        
    def set_out_place_forced(self,out_place):
        '''Set manualy out_place attribute '''
        self.out_place = out_place
        
    def __str__(self):
        return FiveDigit.__str__(self) + ' , ' + str(Guess.get_in_place(self)) + ' , ' + str(Guess.get_out_place(self))
    
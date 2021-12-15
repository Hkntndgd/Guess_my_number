# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:17:09 2021

@author: hakantandogdu
"""
import random
from string import digits

class FiveDigit(object):
    '''FiveDigit Class object has one atribute in strings: five digit number'''
    
    def __init__(self):
        self.figure = None
        
        
    def set_figure(self,number):
        if len(number) == 5:
            self.figure = number
        else:
            print('FiveDigit object has five digits!')
        
    def get_figure(self):
        return self.figure
    
    def __str__(self):
        char = ''
        for item in self.figure:
            char += item + ' '
            
        return char[:-1]
    
    def randomly_set_figure(self):
        '''Set randomly the figure attribute'''
        initial_digits = random.sample(digits,k=5)
        my_number = ''.join(map(str, initial_digits))
        self.set_figure(my_number)

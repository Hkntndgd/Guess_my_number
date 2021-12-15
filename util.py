# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:10:17 2021

@author: htand_000
"""

import random
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def prioritise_the_short(temp_possible_len_dict,temp_possible):
    
    shortest = np.argmin(np.array(list(temp_possible_len_dict.values())))
    
    '''if 1 in list(temp_possible_len_dict.values()):
        for index in list(temp_possible_len_dict.keys()):
            if temp_possible_len_dict[index] == 1:
                critical_index = index'''
    if shortest > 1 and temp_possible_len_dict[shortest] == 1:           
        for index in range(5):
            if index != shortest:
                try:
                    for item in temp_possible[shortest]:
                        temp_possible[index].remove(item)
                except:
                    pass

def temp_possible_finder(possible,in_place_dict,out_place_dict,last_guess_figure):
    temp_possible_len_dict = {}
    temp_possible = copy.deepcopy(possible)
    for index in range(5):
        for value in list(in_place_dict.values()):
           
            try:
                temp_possible[index].remove(int(value))
            except:
                pass
            
        for value in list(out_place_dict.values()):
           
            try:
                temp_possible[index].remove(int(value))
            except:
                pass
        try:
           
            temp_possible[index].remove(int(last_guess_figure[index]))
        except:
            pass
        temp_possible_len_dict[index] = len(temp_possible[index])
    return temp_possible,temp_possible_len_dict

def clean_up_and_guess(in_place_dict,out_place_dict,possible,last_guess_figure):
    char = ''
    
    temp_possible,temp_possible_len_dict = temp_possible_finder(possible,in_place_dict,out_place_dict,last_guess_figure)
    
    prioritise_the_short(temp_possible_len_dict,temp_possible)    
    #print(temp_possible)
                      
    for index in range(5):
        
        if index in list(in_place_dict.keys()):
            temp_char = in_place_dict[index]
        elif index in list(out_place_dict.keys()):
            temp_char = out_place_dict[index]
        else:
            
            try:
                temp_char = str(random.sample(temp_possible[index],1)[0])
            except ValueError:
                temp_char = last_guess_figure[index]
                print('possible:',possible,'\ntemp_possible:',temp_possible,'\nin_place_dict:',in_place_dict,'\nout_place_dict:',out_place_dict)
            
        char += temp_char
        if index != 4:
            for j in range(index+1,5):
                
                try:
                    temp_possible[j].remove(int(temp_char))
                    
                except:
                    pass
        temp_possible_len_dict[index] = len(temp_possible[index])
        prioritise_the_short(temp_possible_len_dict,temp_possible) 
        temp_char = ''
        
    return char

def clean_up_out_place_dict(temp_permute,in_place_dict,last_guess_figure,possible):
    temp_keys = [key for key in list(range(5)) if key not in list(in_place_dict.keys())]
    permute = copy.deepcopy(temp_permute)
    for per in temp_permute:
       for x,y in list(zip(temp_keys,per)):
           if x == y and per in permute:
               permute.remove(per) 
    #temp_keys: possible keys list
    #permute:value pointers
    #temp_permute: keys  
    forbidden_keys_pointers ={}
    temp_possible = copy.deepcopy(possible)
    for keys in temp_permute:
        for pointers in permute:
            temp_dict = {}
            for key,pointer in list(zip(keys,pointers)):
                temp_dict[key] = last_guess_figure[pointer]
                temp_possible,temp_possible_len_dict = temp_possible_finder(possible,in_place_dict,temp_dict,last_guess_figure)
                if 0 in list(temp_possible_len_dict.values()):
                    forbidden_keys_pointers[keys] = pointers
            
    return forbidden_keys_pointers

def example_plot(ax,d):
    
    
    ax.plot(d,'ro',markersize = 12)

    ax.locator_params(nbins=3)
    
   
    ax.set_xlabel('episode', fontsize=12)
    ax.set_ylabel('average trial to success', fontsize=12)
    ax.set_title('Simulation with various episode values each with 250 samples', fontsize=12)
    ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

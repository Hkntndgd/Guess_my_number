# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:16:08 2021

@author: hakantandogdu
"""
from guess import Guess
from fiveDigit import FiveDigit
import random
import itertools
import copy
import numpy as np
import pandas as pd
import util
import matplotlib.pyplot  as plt



class Iterate(Guess):
    '''Iterate object has an attribute; guess_list. 
    Inherits from Guess'''
    
    def __init__(self):
        self.guess_list =[]
        
    def get_list(self):
        return self.guess_list
        
    def addguess(self,guess):
        '''Add a Guess object to guess_list'''
        self.guess_list.append((guess))
            
    def get_guess(self,nth):
        '''Returns the nth element of the guess_list'''
        return self.get_list()[nth]
        
        
    def __str__(self):
        result = ''
        for guess in self.guess_list:            
            result += Guess.__str__(guess) + '\n'
        return result
    
    
        
    def initial_possible():
        '''Create an initial possible list composed of five 
        elements each initialy authorize all the digits of alphabet'''
        k = []
        for i in range(5):
            k.append(list(range(10)))     
        return k
    
    def possible_digits_in_index(self,possible):
        '''Updates possible list as things progress. It removes a figure
        from a given index:
            if last prediction's in_place is zero;
            and if previous prediction's in_place is greater than zero'''
        last_guess = Iterate.get_guess(self,-1)
        
        if last_guess.get_in_place() == 0:
            for i in range(5):
                try:
                    possible[i].remove(int(Iterate.get_figure(last_guess)[i]))
                except:
                    pass
                
            try:
                previous_guess = Iterate.get_guess(self,-2)
                if Iterate.get_in_place(previous_guess) >= 1:
                    for i, x, y in enumerate(zip(Iterate.get_figure(previous_guess),Iterate.get_figure(last_guess))):
                        if x == y:
                            try:
                                possible[i].remove(int(Iterate.get_figure(last_guess))[i])
                            except:
                                pass
            except:
                pass
    
        return possible



    def guess_in_place_digits(self,possible):
        '''Returns a dictionary for in_place digits for the nextprediction.
        key: index
        value: one digit number from possible'''
        in_place_dict = {}
        last_guess = Iterate.get_guess(self,-1)
        
        
        
        index_to_sample = [key for key in list(range(5)) if int(Iterate.get_figure(last_guess)[key]) in possible[key]]
        
        temp_keys = random.sample(index_to_sample,Iterate.get_in_place(last_guess))
        
        for key in temp_keys:
            in_place_dict[key] = Iterate.get_figure(last_guess)[key]
            
        return in_place_dict
    
    def guess_out_place_digits(self,possible,in_place_dict):
        '''Returns a dictionary for out_place digits for the nextprediction.
        key: randomly selected within the set of remaining indexes after
            allocating for in_place dictionary
        value: one digit number from possible tuples preprocesssed in order not to have the
        figure on the same index as in the last guess'''
        out_place_dict = {}
        last_guess = Iterate.get_guess(self,-1)
        
        temp_keys = [key for key in list(range(5)) if key not in list(in_place_dict.keys())]

        if -Iterate.get_out_place(last_guess) == 1:
            key_value = list(itertools.permutations(temp_keys,2))
            key,value = random.sample(key_value,1)[0]
            out_place_dict[key] = Iterate.get_figure(last_guess)[value]
            
        elif -Iterate.get_out_place(last_guess) >= 2:
        
            
            
            temp_permute = list(itertools.permutations(temp_keys,-Iterate.get_out_place(last_guess)))
            
            # temp_permute = [per for per in temp_permute if list(per) != sorted(per)]
            
            permute = copy.deepcopy(temp_permute)
            
            for per in temp_permute:
                for x,y in list(zip(temp_keys,per)):
                    if x == y and per in permute:
                        permute.remove(per)
            
            
                   
            
            #pointers = list(random.sample(permute,1)[0])
            #last_guess_figure = Iterate.get_figure(last_guess)
            #forbidden_keys_pointers = util.clean_up_out_place_dict(temp_permute,in_place_dict,last_guess_figure,possible)
            
            
            keys = random.sample(temp_keys,-Iterate.get_out_place(last_guess))
            
            if keys[0] in permute:
                permute.remove(keys[0])
            
            #if tuple(keys) in list(forbidden_keys_pointers.keys()):
                #permute.remove(forbidden_keys_pointers[tuple(keys)])
                
            pointers = list(random.sample(permute,1)[0])
            
            
            
            for i,key in enumerate(keys):
                out_place_dict[key] = Iterate.get_figure(last_guess)[pointers[i]]
        
        
        return out_place_dict
    
    def guess_out_place_digits_very_long(self,possible,in_place_dict):
        '''Created to test how heavy is the algorithm to avoid bug mentioned
        on README.txt'''
        
        out_place_dict = {}
        last_guess = Iterate.get_guess(self,-1)
        
        temp_keys = [key for key in list(range(5)) if key not in list(in_place_dict.keys())]

        if -Iterate.get_out_place(last_guess) == 1:
            key_value = list(itertools.permutations(temp_keys,2))
            key,value = random.sample(key_value,1)[0]
            out_place_dict[key] = Iterate.get_figure(last_guess)[value]
            
        elif -Iterate.get_out_place(last_guess) >= 2:
        
            
            
            temp_permute = list(itertools.permutations(temp_keys,-Iterate.get_out_place(last_guess)))
            
            # temp_permute = [per for per in temp_permute if list(per) != sorted(per)]
            
            permute = copy.deepcopy(temp_permute)
            
            for per in temp_permute:
                for x,y in list(zip(temp_keys,per)):
                    if x == y and per in permute:
                        permute.remove(per)
            
            
                   
            
            #pointers = list(random.sample(permute,1)[0])
            last_guess_figure = Iterate.get_figure(last_guess)
            forbidden_keys_pointers = util.clean_up_out_place_dict(temp_permute,in_place_dict,last_guess_figure,possible)
            
            
            keys = random.sample(temp_keys,-Iterate.get_out_place(last_guess))
            
            if keys[0] in permute:
                permute.remove(keys[0])
            
            if tuple(keys) in list(forbidden_keys_pointers.keys()):
                permute.remove(forbidden_keys_pointers[tuple(keys)])
                
            pointers = list(random.sample(permute,1)[0])
            
            
            
            for i,key in enumerate(keys):
                out_place_dict[key] = Iterate.get_figure(last_guess)[pointers[i]]
        
        
        return out_place_dict
    
    
    def guess_(self,possible):
        '''Generate a prediction'''
        result = Guess()
        last_guess = Iterate.get_guess(self,-1)
        in_place_dict = self.guess_in_place_digits(possible)
        out_place_dict = self.guess_out_place_digits(possible,in_place_dict)
        last_guess_figure = Iterate.get_figure(last_guess)
        char = util.clean_up_and_guess(in_place_dict,out_place_dict,possible,last_guess_figure)
        #print(char)
        result.set_figure(char) 
            
        return result
    
    def compare_as_if(self,new_guess):
        '''Evaluate a potential new guess and attribute a score 
        to it'''
        score = 0
        
        for guess in self.get_list():
            
           
            
            if Iterate.get_figure(new_guess) == Iterate.get_figure(guess):
                score = -1
                
            else:
                
                new_guess.set_in_place(guess)
                new_guess.set_out_place(guess)
                
                if (Iterate.get_in_place(guess),Iterate.get_out_place(guess)) == (Iterate.get_in_place(new_guess),Iterate.get_out_place(new_guess)):
                    score += 1
            
        return score


    def iterate_w_in_place_out_place(self,possible,episode) :
        '''Make episode time predictions and return the best score prediction'''
        iter_dict = {}
        result = Guess()
        for i in range(episode):
            
            
            new_guess = self.guess_(possible)
            
            score = self.compare_as_if(new_guess)
            iter_dict[new_guess.get_figure()] = score
        
        best = max(iter_dict.values())
        for key in iter_dict.keys():
            if iter_dict[key] == best:
                result.set_figure(key)
                return result
            
    def make_guess_till_success(self,episode=200):
        '''Return number of prediction to succeed. 
        episode is the unique argument you can arbitrarily
        choose'''
        my_num = FiveDigit()
        my_num.randomly_set_figure() 
        print('my_number = ',my_num)
        n = 0
        possible = Iterate.initial_possible()
        
        
        while True:
            guess = Guess()
            if n == 0:
                guess.randomly_set_figure()
            else:
                guess = self.iterate_w_in_place_out_place(possible,n*episode)
                
            guess.set_in_place(my_num)
            guess.set_out_place(my_num)
                
                    
            self.addguess(guess)
            #print(Iterate.__str__(self))
            
            if guess.get_figure() == my_num.get_figure(): 
                #print('C O N G R A T U L A T I O N S'+'\n'+Iterate.__str__(self)+'\n'+'n = ',n+1)
                
                return n+1
            elif guess.get_in_place() == 5 and guess.get_figure() != my_num.get_figure():
                print('C R A C K !!!')
                break
            
            possible = self.possible_digits_in_index(possible)
            n += 1
            
    
    def simulate(sample,start,stop,step):
        '''Return a pandas dataFrame with 3 columns:
            sample,episode,number_of_iter. Called to get 
            some insights about the algorithm,especially 
            how things progress with episode '''
        temp_list = []
        for episode in range(start,stop,step):
            
            for i in range(sample):
                iterate = Iterate()
                n = iterate.make_guess_till_success(episode)  
                temp_list.append([sample,episode,n])
                del iterate
        np_result = np.array(temp_list)    
        df = pd.DataFrame(np_result)
        df = df.rename(columns={0: "sample", 1: "episode",2: "number_of_iter"})
        
        return df
    
    def opt(df):
        '''Return a statistical summary of a dataFrame 
        created with the above procedure'''
        df_avg = df.groupby("episode").mean().rename(columns={"number_of_iter":"avg"}).drop(columns =["sample"])
        df_std_dev = df.groupby("episode").std().rename(columns={"number_of_iter":"std_dev"}).drop(columns =["sample"])
        df_sta = pd.concat([df_avg, df_std_dev], axis=1)
        df_sta.apply(lambda row: row.avg + 3*row.std_dev, axis=1)
        df_sta["confidence_inter"] = df_sta.apply(lambda row: row.avg + 2*row.std_dev, axis=1)  
        return df_sta
    #df.groupby('iter_coef').mean(),df.groupby('iter_coef').std()       
    
    def boxplot():
        '''Create and save a box plot figure from the dataFrame 
        created with the above procedure. The objective of the box plot
        is to visualize the convergence of the mean and distibution of
        the samples with a given episode'''
        df_50_300_by_50 = pd.read_csv('df_50_300_by_50.csv',index_col = [0])
        table = pd.pivot(df_50_300_by_50,columns='episode',values='number_of_iter')
        
        ax = table.plot(kind='box',
                     boxprops=dict(linestyle='-', linewidth=4),
                     flierprops=dict(linestyle='-', linewidth=1.5, alpha = 0.1),
                     medianprops=dict(linestyle='-', linewidth=1.5),
                     whiskerprops=dict(linestyle='-', linewidth=4),
                     capprops=dict(linestyle='-', linewidth=4),
                     showfliers=True, grid=False, rot=0,
                     showmeans = True)
        ax.set_title("Simulation with various episode each with 200 samples", fontsize=14)
        ax.set_xlabel('episode')
        ax.set_ylabel('trials to succeed')
        #plt.show()
        ax.get_figure().savefig('simulation.pdf')
        
    def make_one_guess_w_in_place_out_place(episode):
        '''Step by step prediction process untill succes and
        run in the main.py do not forget to press 'y' to proceed '''
        my_num = FiveDigit()
        my_num.randomly_set_figure() 
        print('my_number = ',my_num)
        
        g_l = Iterate()
        
        n = 0
       
        possible = Iterate.initial_possible()
        while True:
            s = input('--> enter y to continue   ')  
            if s != 'y':
                break
                
            g = Guess()
            
            if n == 0:
                
                g.randomly_set_figure()
                
            else:
                
                g = g_l.iterate_w_in_place_out_place(possible,n*episode)
                
            g.set_in_place(my_num)
            g.set_out_place(my_num)
                
                    
            g_l.addguess(g)
            print(g_l)
            if g.figure == my_num.figure: 
                print('C O N G R A T U L A T I O N S')
                print('n = ',n+1)
                break
            elif g.in_place == 5 and g.figure != my_num.figure:
                print('C R A C K !!!')
                break
            
            possible = g_l.possible_digits_in_index(possible)
           
            n += 1
  
'''Provide game code
Created Fall 2018
Final Project
@author: Sinai Park (sp46)
'''
from tkinter import *
import tkinter as tk
import random

class Game:
    '''This creates the game class to be used in GUI'''
    
    #constructor
    def __init__ (self, num = 3, level = 3):
        '''This method creates the user choice'''
        self._user = 0        
        self._mouse_list = []
        self._button_list = []
        self._current_score = 0
        self._fail_score = 0      
        self._num = num
        self._num_level = level
        self.name_input = ''
        
        
        
        
    def random_button(self):
        '''This method appends random number boxes into a list that the gui imports'''
        for x in range (self.get_num()**2):
            self._button_list = random.sample(range(self.get_num()**2), self.get_num_level())
        self.print_buttonlist()
        
#       loop through buttons to set them black
#       set buttons clicked to empty list
#       process(button) button nbumber += list of numbers BUTTON1_CLICKED

#       user choice>>> list
#     
#       game will see if user cilcked butotns matches >>score point

        #randomly select random buttons from range 0 to 9 set
 
    def get_buttonlist(self):
        '''This method returns the random number of buttons'''
        return self._button_list
    
    def print_buttonlist(self):
        '''This method returns the random number of buttons'''
        print(self._button_list)
    
    def get_mouse_list(self):
        '''This method returns the number of correctly clicked buttons'''
        return len(self._mouse_list)
    
    def get_correct_buttons(self):
        '''This method returns the number of correctly clicked buttons'''
        return self._mouse_list
    
    def print_mouse_list(self):
        '''This method returns the clicked buttons'''
        print(self._mouse_list)
        
    def reset_mouse_list(self):
        '''This method resets the clicked buttons list'''
        self._mouse_list = []

    def get_current_score(self):
        '''This method returns the value of the current score'''
        return self._current_score
    
    def print_current_score(self):
        '''This method returns the value of the current score'''
        print(self._current_score)
        
    def reset_current_score(self):
        '''This method returns the value of the current score'''
        self._current_score = 0
    
    def get_fail_score(self):
        '''This method returns the value of the fail score to end the game'''
        return self._fail_score
    
    def get_num(self):
        '''This method returns the value of the default NUM'''
        return self._num
    
    def add_num(self):
        '''This method adds another square to the default NUM'''
        self._num +=1
    
    def reset_num(self):
        '''This method resets the num value to three for player to start over'''
        self._num = 3
        
    def get_num_level(self):
        '''This method returns the value of the default level'''
        return self._num_level
    
    def add_num_level(self):
        '''This method adds another square to the default NUM'''
        self._num_level +=1

    def reset_num_level(self):
        '''This method resets the num value to three for player to start over'''
        self._num_level = 3
        
    def reset_name(self, string):
        '''This method resets the name into whatever the string is'''
        self.name_input = str(string)
        
    def get_name(self):
        '''This method returns the self.name_input'''
        return str(self.name_input)

    def check_button(self, button_number):
        '''This keeps track of user choice and button and scores the current game score'''
        print(button_number)
        if button_number not in self._button_list:
            self._fail_score = -1
            
            
        elif button_number in self._button_list:
            self._mouse_list.append(button_number)
            self.print_mouse_list()
            self._current_score += 1
       
    def get_high_score(self):
        '''This method gets the high school out of the scoreboard textfile'''
        high_score = []
        try:
            with open('scoreboard.txt', 'r') as file:
                for line in file:
                    s = line.split()
                    score = s[1]
                    high_score.append(int(score))
                return max(high_score)
        except ValueError:
            return 'None'
        
    def erase_scoreboard(self):
        '''This method erases the scoreboard file'''
        open("scoreboard.txt", "w").close()
        
    def print_scoreboard(self):
        '''Opens, reads, and writes in the scoreboard'''

        f = open('scoreboard.txt', 'r')
        if f.mode == 'r':
            contents = f.read()
            return contents

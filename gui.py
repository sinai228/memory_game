'''This is a program to incorporate TKinter and Game
Code lines referenced from GUI controller for a
Tic-Tac-Toe game created by
@author: Serita Nelesen
@author: kvlinden
Created Fall 2018
Final Project
@author/edit: Sinai Park (sp46)
'''

from tkinter import *
import tkinter as tk
from game import Game
import random
import time


def donothing():
    x = 0
    
def showinstructions():
        '''This method shows the instructions to play the game'''
        win = Toplevel()                                                #http://effbot.org/tkinterbook/toplevel.htm
        win.title("Instructions")
        instructions = Label(win, text = "HOW TO PLAY:\n\n Game will start once the user clicks on the PLAY button.\n When the boxes change color, \nremember the position of the boxes that change its color. \nWhen the boxes come back to the default color, \n click on the boxes that had blinked.\n\n If you get all the boxes correct, you will move onto the next level. \nThe current score will keep track of the\n number of boxes you have guess correctly. \n \n Good Luck!")
        instructions.grid(sticky = NSEW)
                      
def about():
    '''This method displays the purpose and objective of the game'''
    win = Toplevel()
    win.title("About")
    about = Label(win, text = "\nFinal Project made by Sinai Park(sp46). \n CS 108 Fall 2018\n ")
    about.grid(sticky = NSEW)


class Gui:      
    '''This will create the GUI application class'''
    def __init__(self, window, TIME = 1500):
        '''Constructor'''
        self._game = Game()
        self._window = window
        self._buttons = []
        self._time = TIME
        
#         for i in range(9):
#             button = Button(self._window, width=3, height=1, font=('Helvetica', 30),
#                             command=lambda i=i: self.process(i))
#             button.grid(row=i // 3, column=i % 3)
#             self._buttons.append(button)

        self.draw_starting_board()

        self._game.print_current_score()
        self._game.print_mouse_list()
        
        self._game.get_high_score
        
    
        #creating menubar
        menubar = Menu(root)
        #create a file menu tab
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label="New Game", command = self.setup)
        filemenu.add_separator()
        filemenu.add_command(label="Reset Scoreboard", command = self._game.erase_scoreboard)
        filemenu.add_command(label="Open Scoreboard", command = self.open_scoreboard)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Menu", menu=filemenu)
        #create a help menu tab
        helpmenu = Menu(menubar, tearoff = 0)
        helpmenu.add_command(label="Instructions", command = showinstructions)
        helpmenu.add_separator()
        helpmenu.add_command(label="About", command = about)
        menubar.add_cascade(label="Help", menu=helpmenu)
         
        root.config(menu = menubar)
        
        
        #labels and buttons
    def labels_buttons(self):
        '''This method builds up all the labels and buttons needed on the window'''
        self._message = StringVar()
        self._message.set('Welcome! \nClick on How to Play')
        message = Label(self._window, textvariable = self._message )
        message.grid(row = self._game.get_num()+3, column = 0, columnspan = 2, sticky = W)
        highscore = Label(self._window, text="Highest Score: ")
        highscore.grid(row = self._game.get_num()+3, column = self._game.get_num()-1, sticky = W)
        currentscore = Label(self._window, text="Current Score: ")
        currentscore.grid(row = self._game.get_num()+4, column = self._game.get_num()-1, sticky = W)
        self._high_label = IntVar()
        self._high_label.set(self._game.get_high_score())
        highscore_label = Label(self._window, textvariable = self._high_label)
        highscore_label.grid(row = self._game.get_num()+3, column =self._game.get_num(), sticky = W)
        self._current_label = IntVar()
        self._current_label.set(self._game.get_current_score())
        currentscore_label = Label(self._window, textvariable = self._current_label)
        currentscore_label.grid(row = self._game.get_num()+4, column =self._game.get_num(), sticky = W)
        add_button = Button(self._window, text = 'Play Game', command = self.start)
        add_button.grid(row = self._game.get_num()+5, column = 0, sticky = NSEW)
        add_button = Button(self._window, text = 'How to Play', command = showinstructions)
        add_button.grid(row = self._game.get_num()+5, column = 1, sticky = NSEW)
        add_button = Button(self._window, text = 'Quit Game', command = root.quit)
        add_button.grid(row = self._game.get_num()+5, column = 2, sticky = NSEW)
        
    def setup(self):
        '''This method resets all settings for the user to start a new game'''
        print('setup')
        self.clear()
        self._game = Game()
        
        self._buttons.clear()
        
        self.draw_starting_board()
        
    def clear(self):
        '''This clears all the widgets on window'''
        widget = root.grid_slaves()
        for w in widget:
            w.destroy()
        
    def draw_starting_board(self):
        '''This method will draw the number of grid buttons'''         
        self._game.reset_num()
        self._game.reset_num_level()
        self._game.reset_current_score()
        for i in range(self._game.get_num()**2):
            button = Button(self._window, width=3, height=1, font=('Helvetica', 30),
                            command=lambda i=i: self.process(i))
            button.grid(row=i // self._game.get_num(), column=i % self._game.get_num())
            self._buttons.append(button)
        self.labels_buttons()
        
        
    def start(self):
        '''This method is to make the buttons blink'''
        self._game.random_button()
        self.random_color()
        

    def draw_button(self):
        '''This method will draw the number of grid buttons'''
#         self._game.random_button()
        self._buttons.clear()
        for i in range(self._game.get_num()**2):
            button = Button(self._window, width=3, height=1, font=('Helvetica', 30),
                            command=lambda i=i: self.process(i))
            button.grid(row=i // self._game.get_num(), column=i % self._game.get_num())
            self._buttons.append(button)
    

    def random_color(self):
        '''This method will start the game by making the boxes blink'''
        for i in range(self._game.get_num()**2):   
            if i in self._game.get_buttonlist():  
                self._buttons[i].config(bg="black", state='disabled')
                self._buttons[i].after(self._time, lambda: self.change_back())
    def change_back(self):                      
        for i in range(self._game.get_num()**2):
            self._buttons[i].config(bg=DEFAULT, state= 'normal') # after 1000ms
            
            
    def start_next_level(self):
        '''This method allows the level to continue and the grid to increase as needed'''
        self._game.print_mouse_list()
        
        if self._game.get_current_score() == 12:
            self._game.add_num()
            self._game.reset_num_level()
            self.draw_button()
            
        elif self._game.get_current_score() == 45:
            self._game.add_num()
            self._game.reset_num_level()
            self.draw_button()
            
        elif self._game.get_current_score() == 108:
            self._game.add_num()
            self._game.reset_num_level()
            self.draw_button()
        
        elif self._game.get_current_score() == 211:
            self._game.add_num()
            self._game.reset_num_level()
            self.draw_button()
                    
        self._time -= 50
        
        self.normal_board()
        
        self.start()
        
    
    def disable_board(self):
        ''' Draw the disabled state of the board on the GUI using the game model state '''
        for i in range(self._game.get_num()**2):
            self._buttons[i].config(state = 'disabled')
            
    def normal_board(self):
        ''' Draw the normal state of the board on the GUI using the game model state '''
        for i in range(self._game.get_num()**2):
            self._buttons[i].config(state = 'normal')
    
    def process(self, button_number):
        ''' Process a click of button with the given button_number... '''
#       #checks whether button clicked is boxes blinked
        self._game.check_button(button_number)
        
        #clicked button becomes disabled
        self._buttons[button_number].config(state='disabled')                 

        #current score gets changed
        self._current_label.set(self._game.get_current_score())

        #if button is not button blinked:
        if self._game.get_fail_score() == -1:
            self._message.set('You clicked on the \n WRONG button...\nNext Time!')
            self.disable_board()
            
            self._player_name = StringVar()
            input1_label = Label(self._window, text = "Please enter your name \n(without space):")
            input1_label.grid(row = 0, column = self._game.get_num()+1, sticky = E)
            input1_entry = Entry(self._window,  textvariable = self._player_name, width = 12)
            input1_entry.grid(row = 1, column = self._game.get_num()+1, sticky = NSEW)
            
            
            #allows player to see scoreboard
            add_button = Button(self._window, text = 'Save & See Scoreboard', command = self.save_and_see_scoreboard)
            add_button.grid(row = self._game.get_num()-1, column = self._game.get_num()+1, sticky = NSEW)
            

        #if the number of buttons correctly clicked is less than actual number
        elif self._game.get_mouse_list() < self._game.get_num_level() :
            self._message.set('Correct,\n click on another box!')
            
        elif self._game.get_mouse_list() == self._game.get_num_level():
        
            self._message.set('You got everything right! \n Next Level!')
    
            time.sleep(1)
            self.disable_board()
               
            self._game.add_num_level()
            self._game.reset_mouse_list()
            
            self.start_next_level()
            
    def save_and_see_scoreboard(self):
        '''This method saves and opens a new window that prints the scoreboard'''
        self.username = self._player_name.get()
        win = Toplevel()
        win.title("Scoreboard")
        self.save_score()
        scores = Label(win, text = '---------------------------------------------------------------------------------\nSCOREBOARD\n---------------------------------------------------------------------------------\n' + self._game.print_scoreboard())
        scores.pack()
        self._game.print_scoreboard()
        
    def open_scoreboard(self):
        '''This method opens a new window that prints the scoreboard'''
        win = Toplevel()
        win.title("Scoreboard")
        scores = Label(win, text = '---------------------------------------------------------------------------------\nSCOREBOARD\n---------------------------------------------------------------------------------\n' + self._game.print_scoreboard())
        scores.pack()
        self._game.print_scoreboard()
        
    def save_score(self):
        '''This method displays the purpose and objective of the game'''
        file= open("scoreboard.txt","a+")
        file.write(str(self.username) + ' ' + str(self._game.get_current_score()) + '\n')
        file.close()         
    
    def safe_exit(self):
        ''' Terminate the animation before shutting down the GUI window. '''
        self._terminated = True
        self._window.destroy()      

if __name__ == '__main__':
    root = Tk()
    DEFAULT = root.cget('bg')
    root.title('Memory 9box game')    
    app = Gui(root)
    root.mainloop()

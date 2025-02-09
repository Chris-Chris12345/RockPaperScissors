from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [("Rock",0),("Paper",1),("Scissors",2)]

def computer_win():
    global  player_score, computer_score
    computer_score += 1
    winner_label.config(text="Computer Wins!")
    computer_score_label.config(text="Computer score:"+ str(computer_score))
    player_score_label.config(text="Player score:"+str(player_score))

def player_win():
    global  player_score, computer_score
    player_score += 1
    winner_label.config(text="Player Wins!")
    computer_score_label.config(text="Computer score:"+ str(computer_score))
    player_score_label.config(text="Player score:"+str(player_score))

def tie():
    global  player_score, computer_score
    winner_label.config(text="It's a Tie!")
    computer_score_label.config(text="Computer score:"+ str(computer_score))
    player_score_label.config(text="Player score:"+str(player_score))

def player_choice(player_input):
    global player_score,computer_score
    print(player_input)
    computer_input = get_computer_choice()
    print(computer_input)

    player_choice_label.config(text="You selected:"+ player_input)
    computer_choice_label.config(text="Computer selected:"+ computer_input)


    if (player_input == computer_input):
        tie()

    if (player_input[1] == 0):
        if (computer_input[1] == 1):
            computer_win()
        elif (computer_input[1] == 2):
            player_win()

    if (player_input[1] == 1):
        if (computer_input[1] == 0):
            player_win()
        elif (computer_input[1] == 2):
            computer_win()

    if (player_input[1] == 2):
        if (computer_input[1] == 0):
            computer_win()
        elif (computer_input[1] == 1):
            player_win()

def  get_computer_choice():
    return random.choice(options)

game =  Tk()
game.title = "Rock Paper Scissors"

game_font = font.Font(size=15)

game_title = Label(game,text="Rock Paper Scissors Game",font= font.Font(size=18),bg="blue",fg="red")
game_subtitle = Label(game,text="Let's Play!",font= font.Font(size=12),bg="blue",fg="red")

input_frame = Frame(game)
input_frame.pack()

rock_btn = Button(input_frame,text="Rock",width=30,bg="grey",fg="black",command= player_choice(options[0]))
rock_btn.grid(row=0,column=0,pady=8)
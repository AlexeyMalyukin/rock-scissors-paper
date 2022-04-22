import random
import tkinter as tk
from tkinter import*
from tkinter import messagebox

root = Tk()

image_scissors = tk.PhotoImage(file="scissors.png")
image_rock = tk.PhotoImage(file="rock.png")
image_paper = tk.PhotoImage(file="paper.png")
image_bg = tk.PhotoImage(file="background.png")

class Application(tk.Frame):
  def __init__(self, master=None):
      super().__init__(master)
      self.pack()
      self.widgets()

  def widgets(self):
      self.rock = tk.Button(frame, text='Rock', bg='yellow', command=self.btn_click_rock, image=image_rock,
                            compound= "bottom", relief = 'flat')
      self.rock.pack(side=LEFT)

      self.paper = tk.Button(frame, text='Paper', bg='yellow', command=self.btn_click_paper, image=image_paper,
                             compound= "bottom", relief = 'flat')
      self.paper.pack(side=RIGHT)

      self.scissors = tk.Button(frame, text='Scissors', bg='yellow', command=self.btn_click_scissors, image=image_scissors,
                                compound="bottom", relief = 'flat')
      self.scissors.pack(side=BOTTOM)


  def btn_click_rock(self):
    self.player_choice = 'rock'
    self.random_choice = random.randint(0, 2)
    if self.random_choice == 0:
        self.computer_choice = 'rock'
        self.winner = 'Draw'
    elif self.random_choice == 1:
        self.computer_choice = 'paper'
        self.winner = 'Computer'
    elif self.random_choice == 2:
        self.computer_choice = 'scissors'
        self.winner = 'Player'

    print("Computer's choice: ", self.computer_choice)
    print("Winner is: ", self.winner)

    messagebox.showinfo('Winner is: ' + self.winner, 'Computer\'s choice: ' + self.computer_choice)

  def btn_click_paper(self):
    self.player_choice = 'paper'
    self.random_choice = random.randint(0, 2)
    if self.random_choice == 0:
        self.computer_choice = 'rock'
        self.winner = 'Player'
    elif self.random_choice == 1:
        self.computer_choice = 'paper'
        self.winner = 'Draw'
    elif self.random_choice == 2:
        self.computer_choice = 'scissors'
        self.winner = 'Computer'

    print("Computer's choice: ", self.computer_choice)
    print("Winner is: ", self.winner)

    messagebox.showinfo('Winner is: ' + self.winner, 'Computer\'s choice: ' + self.computer_choice)

  def btn_click_scissors(self):
    self.player_choice = 'scissors'
    self.random_choice = random.randint(0, 2)
    if self.random_choice == 0:
        self.computer_choice = 'rock'
        self.winner = 'Computer'
    elif self.random_choice == 1:
        self.computer_choice = 'paper'
        self.winner = 'Player'
    elif self.random_choice == 2:
        self.computer_choice = 'scissors'
        self.winner = 'Draw'

    print("Computer's choice: ", self.computer_choice)
    print("Winner is: ", self.winner)

    messagebox.showinfo('Winner is: ' + self.winner, 'Computer\'s choice: ' + self.computer_choice)


root['bg'] = '#fafafa'
root.title('Rock, Scissor, Paper')
root.wm_attributes('-alpha', 1)
root.geometry ('900x600')

root.resizable(width=True, height=True)

canvas = Canvas(root,height=100, width=200)
canvas.pack()

frame = Label(root, bg='white', image=image_bg)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

title = Label(frame, text= 'Let\'s play! \n Make your choice:', bg='green', font=80)
title.pack()

app = Application(master=root)
app.mainloop()







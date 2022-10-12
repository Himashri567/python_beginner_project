import random
from tkinter import *
root = Tk()
root.geometry("1000x900")
root.minsize(1000, 900)
root.title("Dice game")
text1 = Label(root, text='', font="arial 300")
text_s = Label(root, text='', font="Helvetica 20 bold")
text2 = Label(root, text='', font="Helvetica 18 bold", fg="red")
text3 = Label(root, text='', font="Helvetica 18 bold", fg="blue")
def roll_die():
    num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice1 = random.choice(num)      # generating random value from the mum list
    dice2 = random.choice(num)
    dice3 = random.choice(num)
    d1,d2,d3=0,0,0
    text1.config(text=f'{dice1}{dice2}{dice3}')
    text1.pack()
    text_s.config(text='')
    text_s.pack()
    text2.config(text='')
    text2.pack()
    text3.config(text='')
    text3.pack()

    if dice1 == '\u2680':
        d1 = 1
    elif dice1 == '\u2681':
        d1 = 2
    elif dice1 == '\u2682':
        d1 = 3
    elif dice1 == '\u2683':
        d1 = 4
    elif dice1 == '\u2684':
        d1 = 5
    elif dice1 == '\u2685':
        d1 = 6


    if dice2 == '\u2680':
        d2 = 1
    elif dice2 == '\u2681':
        d2 = 2
    elif dice2 == '\u2682':
        d2 = 3
    elif dice2 == '\u2683':
        d2 = 4
    elif dice2 == '\u2684':
        d2 = 5
    elif dice2 == '\u2685':
        d2 = 6


    if dice3 == '\u2680':
        d3 = 1
    elif dice3 == '\u2681':
        d3 = 2
    elif dice3 == '\u2682':
        d3 = 3
    elif dice3 == '\u2683':
        d3 = 4
    elif dice3 == '\u2684':
        d3 = 5
    elif dice3 == '\u2685':
        d3 = 6

    total_s = d1+d2+d3
    text_s.config(text=" Your Score is "f'{total_s}')       # the score gets updated after each roll
    text_s.pack()
    if dice1 == dice2 == dice3:
        text3.config(text="Congrats!! BONUS X3..Your score  3 x total of numbers in 3 dice...You score: "f'{total_s*3}')
        text3.pack()
    elif (dice1 == dice2) or (dice1 == dice3) or (dice2 == dice3):
        text2.config(text="Congrats!! BONUS X2..Your score  2 x total of numbers in 3 dice...You score: "f'{total_s*2}')
        text2.pack()



button_1 = Button(root, text="Click to roll the die", font="arial 16 bold", bg="cyan", command=roll_die)
button_1.place(x=500, y=15)

root.mainloop()
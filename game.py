from tkinter import *
import tkinter as tk
from tkinter import ttk

import random
from tkinter import Entry
from tkinter import messagebox
import tkinter.font as font
root = Tk()
root.geometry('1000x450')
root.resizable(0,0)
root.title("Game")
root.iconbitmap(r'C:\Users\DELL\Downloads\hnet.com-image.ico')
root.configure(bg='slate blue')
myFont = font.Font(family='Londrina Solid',weight="bold")
# canvas=Canvas(root,width=1000,height=450)
# image5=ImageTk.PhotoImage(file="images/OM.png")
# canvas.create_image(0,0,anchor=NW,image=image5)
# canvas.pack()
#############################################

varp=IntVar()
Player1_text=Entry(root,textvariable=varp,font='arial 54')
Player1_text.place(x=138, y=138,width=80,height=80)
# play=int(Player1_text.get())
intchan=IntVar()
intchan1=IntVar()
chanceee=IntVar()
intchan.set(8)
chanceee.set(intchan.get())
chanceee1=IntVar()
intchan1.set(8)
chanceee1.set(intchan1.get())
mess="hgfcc"
chance1=Entry(root,font=("Courier", 20),textvariable=intchan1)
chance1.place(x=950, y=0,width=36,height=36)
chance=Entry(root,font=("Courier", 20),textvariable=intchan)
chance.place(x=110, y=0,width=36,height=36)
intvar2=IntVar()
intvar=IntVar()
var=StringVar()
varp1=IntVar()
var.set(("Guess a number between 1 to 10"))
Points=IntVar()
Points.set(intvar.get())
number = int(random.randint(1, 11))
number1 = int(random.randint(1, 11))
# #######################################################
def compare_number1():
    chanceee.set(intchan.get())
    if intchan.get() > 0:
        if varp.get() == number:
            print(varp.get())
            var.set("Congratulation YOU WON!!!")
            intchan.set(intchan.get()-1)
            intvar.set(intvar.get()+1)
        elif varp.get() > number:
            var.set("YOU CHOOSED BIGGER NUMBER")
            intchan.set(intchan.get()-1)
        elif varp.get() < number:
            var.set("YOU CHOOSED SMALLER NUMBER")
            intchan.set(intchan.get()-1)
        else:
             var.set("ERROR")
    else:
        var.set("CHANCES OVER")


###################################################
def compare_number2():
    chanceee1.set(intchan1.get())
    if intchan1.get() > 0:
        if varp1.get() == number1:
            print(varp1.get())
            var.set("Congratulation YOU WON!!!")
            intchan1.set(intchan1.get()-1)
            intvar2.set(intvar.get()+1)
        elif varp1.get() > number1:
            print(varp1.get())
            var.set("YOU CHOOSED BIGGER NUMBER")
            intchan1.set(intchan1.get()-1)
        elif varp1.get() < number1:
            print(varp1.get())
            var.set("YOU CHOOSED SMALLER NUMBER")
            intchan1.set(intchan1.get()-1)
        else:
             var.set("ERROR")
    else:
        var.set("CHANCES OVER")

# def final():
#     pass

# def messsagebox():
#     if intvar.get() > intvar2.get():
#         messagebox.showinfo("showinfo", "Information")
#     elif intvar.get() < intvar2.get():
#         messagebox.showinfo("showinfo", "Information")
#     else:
#         messsagebox.showinfo(title="dfghjdcv",message=mess)
#######################################################
Label_middle = Label(root, text ='NUMBER GUESSING GAME',font=("Courier", 29),relief=GROOVE,bg="red")
Label_middle.place(x=500,y = 24, anchor = 'center')
player1_Label = Label(root, text ='PLAYER 1',font=("Courier", 29),relief=GROOVE)
player1_Label.place(x=180,y = 84,anchor = 'center')
player2_Label = Label(root,text ='PLAYER 2',font=("Courier", 29),relief=GROOVE)
player2_Label.place(x=810, y = 84,anchor = 'center')
###########################################################


Player2_text=Entry(root,textvariable=varp1,font='arial 54')
Player2_text.place(x=775, y=138,width=80,height=80)
# messagebox.showinfo("showinfo", "Information")
# scorrrrre 1111111111
score1_label=Label(root,text ='SCORE-',font=("Courier", 29),relief=GROOVE)
score1_label.place(x=38, y=388)

score1=Entry(root,font=("Courier", 29),textvariable=intvar)
score1.place(x=188, y=389,width=46,height=46)
# scorrrrre 222222222
score2_label=Label(root,text ='SCORE-',font=("Courier", 29),relief=GROOVE)
score2_label.place(x=750, y=388)

score2=Entry(root,font=("Courier", 29),textvariable=intvar2)
score2.place(x=900, y=389,width=46,height=46)
# chancess left
chance_label=Label(root,text ='CHANCE',font=("Courier", 20),relief=GROOVE)
chance_label.place(x=0, y=0)
chance_label2=Label(root,text ='CHANCE',font=("Courier", 20),relief=GROOVE)
chance_label2.place(x=840, y=0)
#####################################
click_button1=Button(root,text ="CLICK",command=compare_number2,width=8,bg = 'grey', activebackground = 'sky blue',font=myFont,pady = 1)
click_button1.place(x=595,y=168)
click_button=Button(root,text ="CLICK",command=compare_number1,width=8,bg = 'grey', activebackground = 'sky blue',font=myFont,pady = 1)
click_button.place(x=289,y=168)

# resukt_button=Button(root,text ="RESULT",command=messsagebox,width=8,bg = 'grey', activebackground = 'sky blue',font=myFont,pady = 1)
# resukt_button.place(x=459,y=400)
######################################
mess_Label = Entry(root,textvariable=var,font=("Courier", 20),relief=GROOVE,width=32)
mess_Label.place(x=240, y = 270)
mainloop()
#####################################################
# import random
# points=0
# points1=0
# def game1(points=0):
#
#     for x in range(6):
#         num = int(input("enter chossed number from range 1-10"))
#         number = random.randint(1, 11)
#         if num == number:
#
#             print("hey u win ")
#             points+=1
#             return points
#             break
#         elif num>number:
#             print("u guessed bigger number")
#         elif num<number:
#             print("u guessed smaller number")
#
# def game2(points1=0):
#
#     for x in range(6):
#         num = int(input("enter choosed number from range 1-10"))
#         number = random.randint(1, 11)
#         if num == number:
#             print("hey u win ")
#             points1+=1
#             return points1
#             break
#         elif num > number:
#             print("u guessed bigger number")
#         elif num < number:
#             print("u guessed smaller number")
# #
# #
# # def player1():
# #     print("player 1 turn")
# #     game1()
# #     print()
# # def player2():
# #     print("player 2 turn")
# #     print()
# #
# #     game2()
# #
# # def start():
# #     n=0
# #     while(n<=1):
# #         player1()
# #         player2()
# #         n=n+1
# #     print(points)
# #     print(points1)
# #     if points==points1:
# #         print("its a tie")
# #     elif points>points1:
# #         print("player 1 win")
# #     elif points<points1:
# #         print("player 2 win")
# # start()
# #
#
#
#
#
#

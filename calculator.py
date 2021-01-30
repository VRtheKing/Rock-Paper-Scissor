from tkinter import *
import tkinter as tk

m = tk.Tk()
m.title("Calculator")

Screen = Entry(m, borderwidth=5, width=35)
Screen.grid(row=0, column=0, columnspan=4, padx=25, pady= 10)


def shownumber(number):
	Screen.insert(END, number)

def button_clear():
    Screen.delete(0, END)

def add():
    fnum = Screen.get()
    global firstNumber 
    global operator
    operator = "addition"
    firstNumber = int(fnum)
    Screen.delete(0, END)

def subtract():
    fnum = Screen.get()
    global firstNumber 
    global operator
    operator = "subtraction"
    firstNumber = int(fnum)
    Screen.delete(0, END)

def multiply():
    fnum = Screen.get()
    global firstNumber 
    global operator
    operator = "multiplication"
    firstNumber = int(fnum)
    Screen.delete(0, END)

def divide():
    fnum = Screen.get()
    global firstNumber 
    global operator
    operator = "division"
    firstNumber = int(fnum)
    Screen.delete(0, END)

def button_equals():
    second_num = Screen.get()
    Screen.delete(0, END)

    if operator == "addition":
        Screen.insert(0, int(second_num) + int(firstNumber))
    if operator == "multiplication":
        Screen.insert(0, int(second_num) * int(firstNumber))
    if operator == "division":
        Screen.insert(0, int(firstNumber) / int(second_num))
    if operator == "subtraction":
        Screen.insert(0, int(firstNumber) - int(second_num))



one = tk.Button(m, text="1", padx=20, pady=10, command=lambda: shownumber(1))
two = tk.Button(m, text="2", padx=20, pady=10, command=lambda: shownumber(2))
three = tk.Button(m, text="3", padx=20, pady=10, command=lambda: shownumber(3))
four = tk.Button(m, text="4", padx=20, pady=10, command=lambda: shownumber(4))
five = tk.Button(m, text="5", padx=20, pady=10, command=lambda: shownumber(5))
six = tk.Button(m, text="6", padx=20, pady=10, command=lambda: shownumber(6))
seven = tk.Button(m, text="7", padx=20, pady=10, command=lambda: shownumber(7))
eight = tk.Button(m, text="8", padx=20, pady=10, command=lambda: shownumber(8))
nine = tk.Button(m, text="9", padx=20, pady=10, command=lambda: shownumber(9))
zero = tk.Button(m, text="0", padx=20, pady=10, command=lambda: shownumber(0))
doublezero = tk.Button(m, text="00", padx=18, pady=10, command=lambda: shownumber(00))
addition = tk.Button(m, text="+", padx=35, pady=10, command=add)
subtraction = tk.Button(m, text="_", padx=35, pady=10, command=subtract)
multiplication = tk.Button(m, text="X", padx=35, pady=10, command=multiply)
division = tk.Button(m, text="/", padx=35, pady=10, command=divide)
equals = tk.Button(m, text='=', padx=20, pady=10, command=button_equals)
clear = tk.Button(m, text='Clear', padx=120, pady=20, command=button_clear)

one.grid(row=2, column=0)
two.grid(row=2, column=1)
three.grid(row=2, column=2)
four.grid(row=3, column=0)
five.grid(row=3, column=1)
six.grid(row=3, column=2)
seven.grid(row=4, column=0)
eight.grid(row=4, column=1)
nine.grid(row=4, column=2)
zero.grid(row=5, column=0)
doublezero.grid(row=5, column=2)
addition.grid(row=2, column=3)
subtraction.grid(row=3, column=3)
multiplication.grid(row=4, column=3)
division.grid(row=5, column=3)
equals.grid(row=5, column=1)
clear.grid(row=6, columnspan=4)


m.mainloop()

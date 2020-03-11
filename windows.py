from tkinter import *
import random

root = Tk()
root.title("W I N D O W S")
root.geometry("500x500")
root.config(bg="black")

baseFrame = Frame(root, width=399, height=299, bg="black")
baseFrame.grid(sticky=NSEW)

topFrame = Frame(baseFrame, height=100, width=300, bg="purple")
topFrame.grid(row=0,sticky=N,columnspan=2)
purple = Label(root, bg="purple", text="purple")
purple.grid(row=0)

frame = Frame(baseFrame, height=100, width=100, bg="red")
frame.grid(row=4, column=0)
red = Label(baseFrame, bg="red", text="red")
red.grid(row=4, column=0)

frame1 = Frame(baseFrame, height=200, width=150, bg="blue")
frame1.grid(row=5, column=0)
blue = Label(baseFrame, bg="blue", text="blue")
blue.grid(row=5, column=0)

frame2 = Frame(baseFrame, height=200, width=150, bg="green")
frame2.grid(row=4, column=1)
green = Label(baseFrame, bg="green", text="green")
green.grid(row=4, column=1)

frame3 = Frame(baseFrame, height=200, width=150, bg="yellow")
frame3.grid(row=5, column=1)
yellow = Label(baseFrame, bg="yellow", text="yellow")
yellow.grid(row=5, column=1)


root.mainloop()

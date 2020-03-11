from tkinter import *
import random
root = Tk()

root.title("UwU")
root.geometry("500x500")

frame = Frame(root,bg = "gainsboro")
frame.grid()

lbl = Label(frame, bg="gainsboro", text=";)")
lbl.grid()

text_ent = Entry(frame)
text_ent.grid()
bttn1 = Button(frame,text = "DINGO BB <3")
bttn1.grid()

root.mainloop()
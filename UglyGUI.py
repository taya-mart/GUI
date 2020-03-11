from tkinter import *
import random
root = Tk()

root.title("Simple GUI")
root.geometry("500x500")

frame = Frame(root, bg="yellow")
frame.grid()

texts = ["in life u either kill or get killed","watcha gonna do watcha gonna do","ur my dad, boogie woogie woogie","motha trucker that hurt like a buttcheek on a stick","C O R O N A T I M E ! ! !","FRE SHA VA CADO"]
buttons = ["iridocyclitis","more like hurricane katrina","i cant believe uve done this","wow"]
colors = ["saddlebrown","olive","darkorchid","maroon","orangered","mediumvioletred"]


for i in range(5):
    text = ""
    color = random.choice(colors)
    text = random.choice(texts)
    lbl = Label(frame, bg=color, text=text)
    lbl.grid()


for i in range(3):
    button = ""
    color = random.choice(colors)
    button = random.choice(buttons)
    bttn = Button(frame, bg=color, text=button)
    bttn.grid()


root.mainloop()

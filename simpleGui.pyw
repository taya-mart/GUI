from tkinter import *
import random
root = Tk()

root.title("Simple GUI")
root.geometry("500x500")

frame = Frame(root, bg="gainsboro")
frame.grid()


# adding labels onto a frame:
# 20 phrases of 5 random, non-existent, 5 lettered words
for i in range(20):
    label = ""
    text = ["a","b","c","d","e","f","g","h","i","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]
    for w in range(5):
        word = ""
        for l in range(5):
            letter = random.choice(text)
            word = word + letter
        label = label + " " + word
    lbl = Label(frame, bg="gainsboro", text=label)
    lbl.grid()

text_ent = Entry(frame)
text_ent.grid()
bttn1 = Button(frame, bg="dimgray", text="do not click")
bttn1.grid()



root.mainloop()
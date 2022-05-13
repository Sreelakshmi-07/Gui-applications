# Import Required Library
from tkinter import *
import random

root = Tk()

root.geometry("700x300")
root.config(bg="#D2B1C4")
root.title("Game \n Rock Paper Scissor")

computer= {
	"0":"Rock",
	"1":"Paper",
	"2":"Scissor"
}
def play_again():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player			 ")
	l3.config(text = "Computer")
	l4.config(text = "")

def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

def isrock():
	c_v = computer[str(random.randint(0,2))]
	if c_v == "Rock":
		result = "ITS A TIE!"
	elif c_v=="Scissor":
		result = "Player WON!"
	else:
		result = "Computer WON!"
	l4.config(text = result)
	l1.config(text = "Rock		 ")
	l3.config(text = c_v)
	button_disable()

def ispaper():
	c_v = computer[str(random.randint(0, 2))]
	if c_v == "Paper":
		result = "ITS A TIE!"
	elif c_v=="Scissor":
		result = "Computer Won!"
	else:
		result = "Player Won!"
	l4.config(text = result)
	l1.config(text = "Paper		 ")
	l3.config(text = c_v)
	button_disable()

def isscissor():
	c_v = computer[str(random.randint(0,2))]
	if c_v == "Rock":
		result = "Computer Won!"
	elif c_v == "Scissor":
		result = "Its a Tie!"
	else:
		result = "Player Won!"
	l4.config(text = result)
	l1.config(text = "Scissor		 ")
	l3.config(text = c_v)
	button_disable()


Label(root,
	text = "Rock Paper Scissor",
	font = "normal 20 bold",
	fg = "#522834",bg="#D2B1C4").pack(pady = 20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text = "Player		 ",
		font =" Times 15 ",
        fg = "#9B597E",bg="#D2B1C4")

l2 = Label(frame,
		text = "VS		 ",
		font = "Times 15 bold" ,fg="#412535",bg="#D2B1C4")

l3 = Label(frame, text = "Computer", font = "Times 15 ",
fg = "#9B597E",bg="#D2B1C4")

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()

l4 = Label(root,
		text = "",
		font = "normal 20 bold",
		width = 15 ,
		borderwidth = 2,
		relief = "solid")
l4.pack(pady = 20)

frame1 = Frame(root)
frame1.pack()
frame1.config(bg="#D2B1C4")
b1 = Button(frame1, text = "Rock",
			font = 10, width = 7,borderwidth = 5,bg="#AE8488",
			command = isrock)

b2 = Button(frame1, text = "Paper ",
			font = 10, width = 7,borderwidth = 5,bg="#AE8488",
			command = ispaper)

b3 = Button(frame1, text = "Scissor",
			font = 10, width = 7,borderwidth = 5,bg="#AE8488",
			command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

Button(root, text = "Play Again",
	font = 10, fg = "#D0C1D7",
	bg = "#2C2032",borderwidth = 5, command = play_again).pack(pady = 20)

root.mainloop()

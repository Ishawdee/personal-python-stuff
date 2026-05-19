from tkinter import *
tk1 = Tk() #making a Tk object
tk1.title("Test") # giving a title to this window
var = StringVar() # creating a variable for text
# button isn't clicked:
label = Label(tk1, textvariable=var, fg="black", bg="gold",font=("Helvetica",16))
var.set("you haven't clicked me yet")
def didClick(event): # when button is clicked
    var.set("now you did!")
label.pack() # saving label info
button = Button(tk1, text="Click me",fg="pink",bg="green",font=("Helvetica",12))
button.pack() # saving button info
button.bind("<Button-1>", didClick) # calling didClick function
tk1.mainloop() # running the program

# ❓ What did you learn of this exercise?
# with button = Button(object, attributes=variables) make a button
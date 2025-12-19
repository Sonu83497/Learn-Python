from tkinter import *
root = Tk()
var = StringVar()
Label = Label(root,textvariable=var, relief=RAISED)
var.set("Hey !? How are you doing ?")
Label.pack()
root.mainloop()
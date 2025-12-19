from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

redButton = Button(frame, text="Red", fg="red")
redButton.pack(side=TOP)

greenButton = Button(frame, text="Brown", fg="brown")
greenButton.pack(side=RIGHT)

blueButton = Button(frame, text="Blue", fg="blue")
blueButton.pack(side=LEFT)

blackButton = Button(bottomframe, text="Black", fg="black")
blackButton.pack(side=BOTTOM)

root.mainloop()
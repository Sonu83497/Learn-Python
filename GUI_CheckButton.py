from tkinter import *
import tkinter
top = tkinter.Tk()
CheckVar1  =IntVar()
CheckVar2  =IntVar()

c1 = Checkbutton(top,text="Male",variable=CheckVar1,onvalue =1,offvalue=0, height=5, width=20)

c2 = Checkbutton(top,text="Female",variable=CheckVar2,onvalue =1,offvalue=0, height=5, width=20)

c1.pack()
c2.pack()
top.mainloop()
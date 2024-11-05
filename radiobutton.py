#radiobutton
from tkinter import *
root=Tk()
rb1=Radiobutton(text="cash",value="cash")
rb1.pack(anchor=W)
rb2=Radiobutton(text="cheque",value="cheque")
rb2.pack(anchor=W)
rb3=Radiobutton(text="dd",value="dd")
rb3.pack(anchor=W)
mainloop()
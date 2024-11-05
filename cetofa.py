#celsius to fahrenhit
from tkinter import *
root=Tk()
root.title("temperature conversion")
root.geometry("300x300+600+350")
root.config(bg="#33ceff")
def temp():
 try:
  celsius=float(e1.get())
  fahrenhit=(celsius*9/5)+32
  e2.delete(0,'end')
  e2.insert(0,fahrenhit)
 except:
  messagebox.showinfo("error","please enter valid values")
  e1.delete(0,'end')
  e1.focus()
lb1=Label(text="celsius")
lb1.grid(row=0,column=0)
e1=Entry()
e1.grid(row=0,column=1)
lb2=Label(text="fahrenhit")
lb2.grid(row=1,column=0)
e2=Entry()
e2.grid(row=1,column=1)
b1=Button(text="calculate",command=temp)
b1.grid(row=3,column=1)
mainloop()

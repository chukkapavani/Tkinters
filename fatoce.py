#fahrenhit to celsius
from tkinter import *
root=Tk()
root.title("temperature conversion")
root.geometry("300x300+600+350")
root.config(bg="#33ceff")
def temperature():
 try:
  fahrenhit=float(e1.get())
  celsius=(fahrenhit-32)*5/9
  e2.delete(0,'end')
  e2.insert(0,celsius)
 except:
  messagebox.showinfo("error","please enter valid values")
  e1.delete(0,'end')
  e1.focus()
lb1=Label(text="fahrenhit")
lb1.grid(row=0,column=0)
e1=Entry()
e1.grid(row=0,column=1)
lb2=Label(text="celsius")
lb2.grid(row=2,column=0)
e2=Entry()
e2.grid(row=2,column=1)
b1=Button(root,text="calculate",command=temperature)
b1.grid(row=7,column=1)

mainloop()
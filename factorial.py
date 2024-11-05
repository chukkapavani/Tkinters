#factorial
from tkinter import *
root=Tk()
root.geometry("300x300+600+350")
root.title("factorial")
def factorial():
 try:
  f=1
  i=1
  n=int(e1.get())
  while(i<=n):
   f=f*i
   i=i+1
   e2.delete(0,'end')
   e2.insert(0,f)
 except:
  messagebox.showinfo("error","enter correct values")
  e1.delete(0,'end')
  e1.focus()
lb1=Label(text="enter a number")
lb1.grid(row=0,column=0)
e1=Entry()
e1.grid(row=2,column=1)
lb2=Label(text="factorail")
lb2.grid(row=3,column=0)
e2=Entry()
e2.grid(row=5,column=1)
b1=Button(root,text="result",command=factorial)
b1.grid(row=6,column=1)
mainloop()

#calculator
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x300+600+350")
lb1=Label(text="A")
lb1.grid(row=0,column=0,sticky="w")
e1=Entry()
e1.grid(row=0,column=1)
lb2=Label(text="B")
lb2.grid(row=1,column=0,sticky="w")
e2=Entry()
e2.grid(row=1,column=1)
lb3=Label(text="C")
lb3.grid(row=2,column=0,sticky="w")
e3=Entry()
e3.grid(row=2,column=1)
def mysum():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a+b
 e3.insert(0,c)
def mysub():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a-b
 e3.insert(0,c)
def mymul():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a*b
 e3.insert(0,c)
def mydiv():
 try:
  e3.delete(0,'end')
  a=int(e1.get())
  b=int(e2.get())
  c=a/b
  e3.insert(0,c)
 except:
  messagebox.showinfo("error","you cannot divide a number with zero")
  e2.delete(0,'end')
  e2.focus()
def myfdiv():
 try:
  e3.delete(0,'end')
  a=int(e1.get())
  b=int(e2.get())
  c=a//b
  e3.insert(0,c)
 except:
  messagebox.showinfo("error","you cannot divide a number with zero")
  e2.focus()
def mymod():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a%b
 e3.insert(0,c)
def myexpo():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a**b
 e3.insert(0,c)
def mycf():
 e1.delete(0,'end')
 e2.delete(0,'end')
 e3.delete(0,'end')
def myqf():
 root.destroy()
b1=Button(text="+",width=10,command=mysum)
b1.grid(row=3,column=0)
b2=Button(text="-",width=10,command=mysub)
b2.grid(row=3,column=1)
b3=Button(text="*",width=10,command=mymul)
b3.grid(row=3,column=2)
b4=Button(text="/",width=10,command=mydiv)
b4.grid(row=4,column=0)
b5=Button(text="//",width=10,command=myfdiv)
b5.grid(row=4,column=1)
b6=Button(text="%",width=10,command=mymod)
b6.grid(row=4,column=2)
b7=Button(text="**",width=10,command=myexpo)
b7.grid(row=5,column=0)
b8=Button(text="<-",width=10,command=mycf)
b8.grid(row=5,column=1)
b9=Button(text="x",width=10,command=myqf)
b9.grid(row=5,column=2)
mainloop()
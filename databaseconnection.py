#python databse insert
from tkinter.ttk import *
from  tkinter import *
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(host="localhost",user="root",password="@Chinna2233",database="demodatabase")
mycursor=mydb.cursor()
root=Tk()
root.title("office data")
root.geometry("750x350");
label1=Label(root,text="eno",width=20,height=2).grid(row=1,column=0)
label2=Label(root,text="ename",width=20,height=2).grid(row=2,column=0)
label3=Label(root,text="esal",width=20,height=2).grid(row=3,column=0)
label4=Label(root,text="egrade",width=20,height=2).grid(row=4,column=0)
e1=Entry(root,width=30,borderwidth=5)
e1.grid(row=1,column=2)
e2=Entry(root,width=30,borderwidth=5)
e2.grid(row=2,column=2)
e3=Entry(root,width=30,borderwidth=5)
e3.grid(row=3,column=2)
e4=Entry(root,width=30,borderwidth=5)
e4.grid(row=4,column=2)
def Register():
 Insert="insert into myemp(eno,ename,esal,egrade)values(%s,%s,%s,%s)"
 eno=e1.get()
 ename=e2.get()
 esal=e3.get()
 egrade=e4.get()
 if(eno!="" and ename!="" and esal!="" and egrade!=""):
  value=(eno,ename,esal,egrade)
  mycursor.execute(Insert,value)
  mydb.commit()
  messagebox.askokcancel("Information","Record inserted")
  e1.delete(0,'end')
  e2.delete(0,'end')
  e3.delete(0,'end')
  e4.delete(0,'end')
 else:
  if(eno==" " and ename==" " and esal==" " and egrade==" "):
   messagebox.askokcancel("Information","New entry fill all details")
  else:
   messagebox.askokcancel("Information","some fields left blank")
button=Button(root,text="Register",width=10,height=2,command=Register).grid(row=5,column=2)
root.mainloop()

#checkbutton
from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("checkbox selection")
def update_label():
 s=[text for var,text in zip(vars,texts) if var.get()==1]
 label.config(text=",".join(s))
vars=[]
texts=["a","b","c","d"]
for text in texts:
 var=IntVar()
 vars.append(var)
 checkbox=Checkbutton(text=text,variable=var,command=update_label)
 checkbox.pack(anchor="w")
label=Label(text="")
label.pack()
root.mainloop()

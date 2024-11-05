#radiobutton
import tkinter as tk
def update_label():
 selected_value=radio_val.get()
 label.config(text=f"selected:{selected_value}")
root=tk.Tk()
root.title("radiobutton example")
radio_var=tk.stringVar()
radio_var.set("option 1")
r1=tk.Radiobutton(root,text="cash",variable=radio_val,value="cash",command=update_label)
r1.pack(anchor=tk.W)
r2=tk.Radiobutton(root,text="cheque",variable=radio_val,value="cheque",command=update_label)
r2.pack(anchor=tk.W)
r3=tk.Radiobutton(root,text="dd",variable=radio_val,value="dd",command=update_label)
r3.pack(anchor=tk.W)
label=tk.Label(root,text="")
label.pack()
root.mainloop()
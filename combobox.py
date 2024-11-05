#combobox
import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("combobox example")
def up(event):
 s=combobox.get()
 label.config(text=f"selected:{selected_value}")
s=tk.StringVar()
combobox=ttk.Combobox(root,textvariable=s)
combobox['values']=("pen","pencil","book")
combobox.current(0)
combobox.pack()
combobox.bind("<<combobox selected>>",up)
label=tk.Label(root,text="")
label.pack()
root.mainloop()
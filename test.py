from tkinter import ttk
from tkinter import *

lst = [1, 2, 3, 4]

cb = ttk.Combobox(values=lst)
help(cb)
cb.tkraise()
cb.pack()

mainloop()

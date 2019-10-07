import tkinter as tk
from tkinter import *

import pythondrill6_func

class Drill2(Frame):
    def __init__(self, master):

        self.dirpath= StringVar()
        
        self.master = master
        self.master.minsize(600,200)
        self.master.maxsize(600,200)
        self.master.title('Drill2')
        self.master.config(bg='lightgray')


        self.btn_browse = tk.Button(self.master,width=12,height=1,text='Files',command=lambda:pythondrill6_func.showFiles(self))
        self.btn_browse.grid(row=3,column=0,padx=(15,5),pady=(25,0),sticky=N+W)
        self.txt_fname = tk.Entry(self.master,text='',width=70, textvar=self.dirpath)
        self.txt_fname.grid(row=3,column=1,rowspan=1,columnspan=3,padx=(25,0),pady=(25,0),sticky=N+E+W)















if __name__ == "__main__":
    root = Tk()
    my_gui = Drill2(root)
    root.mainloop()

import tkinter as tk
from tkinter import *

import pydrill_func

class Drill:
    def __init__(self, master):

        self.dirpathdest=StringVar()
        self.dirpathsource=StringVar()
        
        self.master = master
        self.master.minsize(500,150)
        self.master.maxsize(500,300)
        self.master.title("Check Files")
        self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:pydrill_func.showSource(self))
        self.btn_browse.grid(row=3,column=0,padx=(15,5),pady=(25,0),sticky=N+W)
        self.btn_browse_1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:pydrill_func.showDestination(self))
        self.btn_browse_1.grid(row=4,column=0,padx=(15,5),pady=(10,0),sticky=N+W)
        self.btn_browse_2 = tk.Button(self.master,width=12,height=2,text='Check for Files...',command=lambda:pydrill_func.findFiles(self))
        self.btn_browse_2.grid(row=5,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program', command=self.cancel)
        self.btn_close.grid(row=5,column=2,padx=(270,0),pady=(10,0),sticky=E)


        self.txt_fname = tk.Entry(self.master,text='',textvariable=self.dirpathsource)
        self.txt_fname.grid(row=3,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(25,0),sticky=N+E+W)
        self.txt_lname = tk.Entry(self.master,text='',textvariable=self.dirpathdest)
        self.txt_lname.grid(row=4,column=1,rowspan=1,columnspan=2,padx=(25,0),pady=(15,0),sticky=N+E+W)

    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    my_gui = Drill(root)
    root.mainloop()

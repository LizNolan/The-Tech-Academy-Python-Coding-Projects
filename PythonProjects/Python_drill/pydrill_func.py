import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil
import sqlite3

import pydrill_GUI

conn = sqlite3.connect('drill2.db')

with conn:
   cur = conn.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS tbl_drill2( \
      ID INTEGER PRIMARY KEY AUTOINCREMENT, \
      col_docs TEXT, \
      col_time TEXT \
      )")
   conn.commit()
conn.close()

def showDestination(self):
    x=filedialog.askdirectory()
    print(x)
    self.dirpathdest.set(x)

def showSource(self):
    y=filedialog.askdirectory()
    print(y)
    self.dirpathsource.set(y)

#filelist = os.listdir(y)

def findFiles(self):
   print ("executing findFiles()")
   folder=self.dirpathsource.get() + '/'
   print("dirpathsource: " + folder)
   destination=self.dirpathdest.get() + '/'
   print(destination + " = destination")
   filelist = os.listdir(folder)
   for file in filelist:
       if(file.endswith(".txt")):
           filepath=os.path.join(folder, file)
           #print(filepath + " = absolute filepath")
           timestamp = os.path.getmtime(filepath)
           print(file,timestamp)
           shutil.move(filepath, destination)
           conn = sqlite3.connect('drill2.db')

           with conn:
               cur = conn.cursor()
               cur.execute("INSERT INTO tbl_drill2(col_docs,col_time) VALUES (?,?)", \
                      (file,timestamp))
               conn.commit()
           conn.close()
           

           # filepath=os.path.join(y, filename)
           # print(filename,os.path.getmtime(filepath))
        
    




if __name__ == "__main__":
    pass

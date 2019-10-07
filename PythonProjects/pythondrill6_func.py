import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

import pythondrill6_GUI


def showFiles(self):
    x=filedialog.askdirectory()
    print(x)
    self.dirpath.set(x)    


if __name__ == "__main__":
    pass

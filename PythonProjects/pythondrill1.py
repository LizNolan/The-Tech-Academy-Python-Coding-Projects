import os
import time

filelist= os.listdir(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects')
print(filelist)

fName = 'Liz.txt'

fPath ='C:\\Users\15035\Documents\Tech Academy Projects\PythonProjects\\'

abPath = os.path.join(fPath, fName)
print (abPath)

modification_time = os.path.getmtime(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\Liz.txt')
local_time = time.ctime(modification_time)
print("Last modification time (Local time):", local_time)

print(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\file10.txt') 
modification_time = os.path.getmtime(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\file10.txt')
local_time = time.ctime(modification_time)
print("Last modification time (Local time):", local_time)

print(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\file3.txt') 
modification_time = os.path.getmtime(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\file3.txt')
local_time = time.ctime(modification_time)
print("Last modification time (Local time):", local_time)

print(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\Liz2.txt') 
modification_time = os.path.getmtime(r'C:\Users\15035\Documents\Tech Academy Projects\PythonProjects\Liz2.txt')
local_time = time.ctime(modification_time)
print("Last modification time (Local time):", local_time)

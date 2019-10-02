
import os
import time


dirPath = r'C:\Users\15035\Documents\GitHub\The-Tech-Academy-Python-Coding-Projects\PythonProjects'
filelist= os.listdir(dirPath)

for filename in filelist:
   if(filename.endswith(".txt")):
       print(filename, filename.endswith(".txt"),os.path.join(dirPath, filename),os.path.getmtime(filename))



   
print()





#filename = "file10.txt"

#filePath = os.path.join(dirPath, filename)

#os.path.getmtime(filePath)


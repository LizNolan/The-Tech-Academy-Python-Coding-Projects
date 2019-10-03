
import os
import time


dirPath = r'C:\Users\15035\Documents\GitHub\The-Tech-Academy-Python-Coding-Projects\PythonProjects'
filelist= os.listdir(dirPath)

for filename in filelist:
   if(filename.endswith(".txt")):
       filepath=os.path.join(dirPath, filename)
       print(filename,os.path.getmtime(filepath))



   
print()





#filename = "file10.txt"

#filePath = os.path.join(dirPath, filename)

#os.path.getmtime(filePath)


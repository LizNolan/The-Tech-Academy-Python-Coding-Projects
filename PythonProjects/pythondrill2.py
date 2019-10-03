

import sqlite3

conn = sqlite3.connect('drill.db')

with conn:
   cur = conn.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS tbl_drill( \
      ID INTEGER PRIMARY KEY AUTOINCREMENT, \
      col_docs TEXT \
      )")
   conn.commit()
conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('drill.db')

with conn:
   cur = conn.cursor()

for filename in fileList:
   if filename.endswith(".txt"):
      cur.execute("INSERT INTO tbl_drill(col_docs) VALUES (?)", \
                  (filename,))
      conn.commit()
      print(filename)
conn.close() 


 

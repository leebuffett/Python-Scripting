import os.path
from os import path

f = open("unrecovered.txt","a+",encoding="utf-8")
z = open("DoneRecovered.txt","a+",encoding="utf-8")
w = open('recovered.txt', encoding="utf8").readlines()

for line in w:
    line = line.replace("\n", "")
    string1= line + " ->  File exists:"+str(path.exists(line)) + "\n"
    if(path.exists(line))==False:
        f.write(string1)
    else:
        z.write(string1)
   
f.close()
w.close()
z.close()
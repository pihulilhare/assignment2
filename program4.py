# 4. Write a Python program to read last n lines of a file and display the same.
import sys  
import os  
def readFile(File4,lines):  
        buffersize = 8192  
        filesize = os.stat(File4).st_size  
        iter = 0  
        with open(File4) as f:  
                if buffersize > filesize:  
                        buffersize = filesize-1  
                        data = []  
                        while True:  
                                iter +=1  
                                f.seek(filesize-buffersize*iter)  
                                data.extend(f.readlines())  
                                if len(data) >= lines or f.tell() == 0:  
                                        print(''.join(data[-lines:]))  
                                        break  
  
readFile('File4.txt',3)  

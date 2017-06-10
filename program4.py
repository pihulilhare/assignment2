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

'''Output

"Failure is a part of life. From time to time you will fail at something. That does not mean that you should give up and never be happy." Clement Getate, Your Cross to Happiness 
"Your life is not a thing, it's an experience; the fun comes from designing and enjoying the experience." Bill Burnett; Dave Evans, Designing Your Life: How to Build a Well-Lived, Joyful Life 
"Sometimes, due to unforeseen tough times, we get discouraged and don't achieve our goals. As hard as it may seem, don't procrastinate in taking renewed action to reach your goals." Byron Pulsifer 
"Everyone wishes for the better things of life, such as money, a good position, fame, and recognition; but most people never go far beyond the 'wishing' stage." Andrew Carnegie
"Life is for the living, and there's a large difference between living and merely existing. When you can seize your potential and truly feel as if you are doing your best in this life, you are living." Patrick King, Limitless: Destroy Your Fears, Escape Your Comfort Zone, and Conquer Any Goal - Create The Life You Want 


[root@test assignment2]# python program4.py
"Sometimes, due to unforeseen tough times, we get discouraged and don't achieve our goals. As hard as it may seem
, don't procrastinate in taking renewed action to reach your goals." Byron Pulsifer 
"Everyone wishes for the better things of life, such as money, a good position, fame, and recognition; but most p
eople never go far beyond the 'wishing' stage." Andrew Carnegie
"Life is for the living, and there's a large difference between living and merely existing. When you can seize yo
ur potential and truly feel as if you are doing your best in this life, you are living." Patrick King, Limitless:
 Destroy Your Fears, Escape Your Comfort Zone, and Conquer Any Goal - Create The Life You Want '''


#3. Write a Python program to append text to a file and display the text. 
def file_read(python):  
        from itertools import islice  
        with open(python, "w") as file:  
                file.write("Python Exercises\n")  
                file.write("Java Exercises")  
        txt = open(python)  
        print(txt.read())  
file_read('python.txt')  
'''Output 
[root@test assignment2]# python program3.py
Python Exercises
Java Exercises'''

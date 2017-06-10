#6. Write a Python program to read a file line by line store it into a variable. 
def file_read(python):  
        with open (python, "r") as file:  
                data=file.readlines()  
                print(data)  
file_read('python.txt')  

'''Output
[root@test assignment2]# python program6.py
['Python Exercises\n', 'Java Exercises\n', 'Cloud Practice\n', 'Basic Learning\n', 'Andriod Training\n', 'Framework Training\n']
'''

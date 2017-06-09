#6. Write a Python program to read a file line by line store it into a variable. 
def file_read(python):  
        with open (python, "r") as file:  
                data=file.readlines()  
                print(data)  
file_read('python.txt')  

#16 : Write a Python program to remove newline characters from a file

def remove_newlines(python):  
    filelist = open(python).readlines()  
    return [s.rstrip('\n') for s in filelist]    
print(remove_newlines("python.txt"))  

#16 : Write a Python program to remove newline characters from a file

def remove_newlines(NewLine):  
    filelist = open(NewLine).readlines()  
    return [s.rstrip('\n') for s in filelist]    
print(remove_newlines("NewLine.txt"))  

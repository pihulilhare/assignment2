#15. Write a Python program to assess if a file is closed or not. 
#Open a file
f = open("File3", "wb")
print "Name of the file: ", f.name

# Close opend file
print "Closed or not : ", f.closed

''' Output
[root@test assignment2]# python program15.py
Name of the file:  File3
Closed or not :  False'''

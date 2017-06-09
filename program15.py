#15. Write a Python program to assess if a file is closed or not. 
#Open a file
f = open("File3", "wb")
print "Name of the file: ", f.name

# Close opend file
print (f.close())

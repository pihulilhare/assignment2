#1. Write a Python program to read an entire text file and print its contents.
file = open("python.txt", "w+")
file.write( "This is First file.\Example of PythonProgram.\Learning Python new Experience.")
file.seek(0,0)
print file.read()
print "Name of the file: ", file.name
print "Closed or not : ", file.closed

'''Output 
[root@test assignment2]# python program1.py
This is First file.\Example of PythonProgram.\Learning Python new Experience.
Name of the file:  python.txt
Closed or not :  False

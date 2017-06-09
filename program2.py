#2. Write a Python program to read first n lines of a file and print these lines.
file = open("program.txt", "w+")
file.write( "This is First file.\nExample of PythonProgram.\nLearning Python new Experience.")
file.write( "This is Second file.\nExample of PythonProgram.\nLearning Python new Experience.")
file.write( "This is Third file.\nExample of PythonProgram.\nLearning Python new Experience.")
file.seek(0,0)
#print file.read()
#print file.readline(1)
#print file.readline(2)
print file.readlines() 
print "Name of the file: ", file.name
print "Closed or not : ", file.closed

''' Output 
[root@test assignment2]# python program2.py
This is First file.Example of PythonProgram.
Learning Python new Experience.
This is Second file.Example of PythonProgram.Learning Python new Experience.
This is Third file.Example of PythonProgram.Learning Python new Experience.
Name of the file:  program.txt
Closed or not :  False

file = open("program.txt", "w+")
file.write( "This is First file.\Example of PythonProgram.\Learning Python new Experience.")
print file.read()
print "Name of the file: ", file.name
print "Closed or not : ", file.closed

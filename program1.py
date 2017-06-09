
file = open("python.txt", "w+")
file.write( "This is First file.\Example of PythonProgram.\Learning Python new Experience.")
file.seek(0,0)
print file.read()
print "Name of the file: ", file.name
print "Closed or not : ", file.closed

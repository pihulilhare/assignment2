file = open("program.txt", "w+")
file.write( "This is First file.\nExample of PythonProgram.\nLearning Python new Experience.")
file.write( "This is Second file.\nExample of PythonProgram.\nLearning Python new Experience.")
file.write( "This is Third file.\nExample of PythonProgram.\nLearning Python new Experience.")
file.seek(0,0)
print file.read()
print file.readline(1)
print file.readline(2)
#print file.readlines() 
print "Name of the file: ", file.name
print "Closed or not : ", file.closed

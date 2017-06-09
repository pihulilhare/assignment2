import io
file = open(“first.txt”,”w”) 
file.write(“Hello”) 
file.write(“This is First file”) 
file.write(“Example of PythonProgram”) 
file.write(“Learning Python new Experience.”) 
file.seek(0,0)
file.read()
file.close() 

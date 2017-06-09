file = open(“first.txt”,”w”) 
 
file.write(“Hello”) 
file.write(“This is First  file”) 
file.write(“Example of Python”) 
file.write(“Learning Python is new Experience.”) 
file.seek(0,0)
file.read()
file.close() 

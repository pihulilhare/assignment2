#7. Write a Python program to read a file line by line store it into an array
def file_read(python):  
        content_array = []  
        with open(python) as file:  
                #Content_list is the list that contains the read lines.       
                for line in file:  
                        content_array.append(line)  
                print(content_array)  
file_read('python.txt')  

'''Output [root@test assignment2]# python program7.py
['Python Exercises\n', 'Java Exercises\n', 'Cloud Practice\n', 'Basic Learning\n', 'Andriod Training\n', 'Framework Training\n']'''

#5. Write a Python program to read a file line by line and store it into a list. 
def file_read(python):
      with open(python) as file:             
        #Content_list is the list that contains the read lines.     
                 content_list = file.readlines()
                 print(content_list)
file_read('python.txt')
'''Output 
[root@test assignment2]# python program5.py
['Python Exercises\n', 'Java Exercises\n', 'Cloud Practice\n', 'Basic Learning\n', 'Andriod Training\n', 'Framewo
rk Training\n']'''



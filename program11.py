
# Question 11 :Write a Python program to write a list to a file

SkillSet = ['Andriod', 'Java', 'MongoDb', 'Python', 'Php', 'Ruby']   
with open('File1.txt', "w") as file:   
  for f in SkillSet:   
    file.write("%s\n" % f)       
content = open('File1.txt')   
print(content.read())   

'''
output:
[root@test assignment2]# python program11.py
Andriod
Java
MongoDb
Python
Php
Ruby
'''

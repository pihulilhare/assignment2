# Question 11 :Write a Python program to write a list to a file

SkillSet = ['Andriod', 'Java', 'MongoDb', 'Python', 'Php', 'Ruby']   
5 with open('File1.txt', "w") as file:   
6         for file in SkillSet:   
7                 file.write("%s\n" % file)   
8    
9 content = open('File1.txt')   
10 print(content.read())   

'''
output:
[root@demo FileHandlingAssignment]# python program11.py 
apple
mango
banana
watermelon
papaya
lichi


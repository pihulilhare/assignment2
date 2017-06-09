
# Question 11 :Write a Python program to write a list to a file

SkillSet = ['Andriod', 'Java', 'MongoDb', 'Python', 'Php', 'Ruby']   
with open('File1.txt', "w") as file:   
  for file in SkillSet:   
   file.write("%s\n" % file)       
   content = open('File1.txt')   
print(content.read())   

'''
output:
[root@demo FileHandlingAssignment]# python program11.py 
apple
mango
banana
watermelon
papaya
lichi
'''

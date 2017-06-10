# 8. Write a python program to find the longest words. 

def longest_word(File1):  
    with open(File1, 'r') as infile:  
              words = infile.read().split()  
    maxlen = len(max(words, key=len))  
    return [word for word in words if len(word) == maxlen]  
  
print(longest_word('File1.txt')) 

''' Output '''

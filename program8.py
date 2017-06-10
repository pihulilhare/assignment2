# 8. Write a python program to find the longest words. 
'''
def longest_word(File1):  
    with open(File1, 'r') as infile:  
              words = infile.read().split()  
    maxlen = len(max(words, key=len))  
    return [word for word in words if len(word) == maxlen]  
  
print(longest_word('File1.txt')) '''

import sys 
def main():
	max_word = ''
	max_word_length = 0
	filename = sys.argv[1]
	infile = open(File1, 'r')
	for line in infile:
		line_list = line.split()
		for word in line_list:
			if len(word) > max_word_length:
				max_word = word
				max_word_length = len(word)	
	infile.close()

''' Output '''

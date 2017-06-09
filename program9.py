9. Write a Python program to count the frequency of words in a file. 
'''from collections import Counter
def count_letters(in_filename, out_filename):
    counts = Counter()
    with open(in_filename, "r") as in_file:
        for chunk in iter(lambda: in_file.read(8196), ''):
            counts.update(chunk)
    with open(out_filename, "w") as out_file:
        for letter, count in counts.iteritems():
            out_file.write('{}:{}\n'.format(letter, count)'''
                         
file=open("File3.txt","r+")

wordcount={}

for w in file.read().split():
    if w not in wordcount:
        wordcount[w] = 1
    else:
        wordcount[w] += 1

for n in wordcount.items():
    print n

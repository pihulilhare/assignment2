#Write a Python program to combine each line from first file with the corresponding line in second file. 
with open('File2.txt') as f2, open('File1.txt') as f1:  
    for l1, l2 in zip(f2, f1):  
        # l1 from File2.txt, l2 from File1.txt
        print(l1+l2)  

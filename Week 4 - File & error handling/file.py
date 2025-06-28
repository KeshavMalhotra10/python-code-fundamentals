animals = open('file.txt', 'a+')
#note that open takes two argument, which file, and which mode
#modes:
'''
r = open for read (default)
w = open for write, truncate(remove all data from file)
r+ = open for read/write
w+ = open for read/write, truncate
a+ = open for read/append
'''
#set up at start of file
animals.seek(0)

#read
#text = animals.read()
#print(text)

#read lines
for animal in animals:
    print(animal)


#write/append
animals.write('giraffe\n')
 
#close
animals.close()



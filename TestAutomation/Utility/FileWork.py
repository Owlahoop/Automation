# How to read data from a file
obj = open("C:\\Users\\Ryan\\Desktop\\PY.txt", 'r')

# Read all data from the file
#print(obj.read())

# Read 1 line from the file
#print(obj.readline())

# Read 2 lines from the file
#print(obj.readline())
#print(obj.readline())

# Read only a few characters from the file
#print(obj.readline(10))

# Read all characters in the file, one by one
#for i in obj.read():
#    print(i)

# Read all data from file line by line
s = obj.readline()
while(s):
    print(s)
    s = obj.readline()

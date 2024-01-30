obj = open("C:\\Users\\Ryan\\Desktop\\PY.txt", 'r')

# Prints line character the reader is currently on
print(obj.tell())
obj.readline()
print(obj.tell())
obj.readline()
print(obj.tell())

# Moves cursor to specific position
obj.seek(5)
print(obj.tell())
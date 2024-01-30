data = "Hello This is A Test String IS"

# Replaces parts of the string with new characters
print(data.replace("Te", "##"))

# Replaces lowercase with capital
print(data.replace("l", "L"))

# Replace multiple substrings in one line
print(data.replace("is", "$$$").replace("IS", "$$$"))

# Remove spaces from the string
print(data.replace(" ", ""))

# Find data in a string
print(data.find("This"))

# Split string
result = data.split(" ")  # Splits each word at the space, and stores in a list
for data in result:  # for loop, based on amount of splits
    print(data)
    
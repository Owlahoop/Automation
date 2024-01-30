data = input("Input number:")
data = int(data)

# Approach 1
if data < 0:
    print("This is a negative number")
else:
    if data % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")

# Approach 2
if data >= 0:
    if data % 2 == 0:
        print("This is an even number")
    else:
        print("This is an odd number")
else:
    print("This is a negative number")
    
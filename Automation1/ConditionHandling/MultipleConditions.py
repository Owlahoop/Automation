data = input("Input number:")
data = int(data)

if data < 0:
    print("This is a negative number")
elif data == 0:
    print("This is zero")
elif data % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

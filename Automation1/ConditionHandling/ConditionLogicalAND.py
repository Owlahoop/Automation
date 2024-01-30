num = input("input number:")
num = int(num)

if num >= 0 and num % 2 == 0:
    print("This is a positive even number")
elif num >= 0 and num % 2 == 1:
    print("This is a positive odd number")
elif num < 0 and num % 2 == 0:
    print("This is a negative even number")
elif num < 0 and num % 2 == abs(1):
    print("This is a negative odd number")

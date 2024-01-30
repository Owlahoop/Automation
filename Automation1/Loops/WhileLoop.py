# Simple while loop
i = 1
while i <= 10:
    print(i)
    i += 1
    # i += 1 is the same as i = i + 1
# Will print 1 to 10

# While loop with user input
num = input("Enter number:")
i = 1
while i <= 10:
    print(int(num) * i)
    i += 1
# Will print num*(1 to 10)

# Simple while loop decreasing
i = 10
while i >= 1:
    print(i)
    i -= 1
# Will print 10 to 1

# While loop decreasing with user input
num = input("Input number:")
i = 10
while i >= 1:
    print(int(num) * i)
    i -= 1
# Will print num*(10 to 1)

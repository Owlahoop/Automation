# For loop with final range
for i in range(10):
    print(i)
# Will print 0 to 9

# For loop using input from user
num = input("Input number:")

for i in range(int(num)):
    print(i)
# Will print 0 to num

# For loop with starting and end value
for i in range(1, 10):
    print(i)
# Will print 1 to 9

# For loop with different increments
z = 5
for i in range(1, 10):
    print(z*i)
# Will print 5*(1 to 9)

# For loop with equation
num = input("Input number:")
for i in range(1, 10):
    print(num + " * " + str(i) + " = " + str(int(num)*i))
# Will print full equation of num*(1 to 9)

# For loop with different increment values
for i in range(1, 12, 2):
    print(i)
# Will print 1 to 11, by increments of 2

# For loop with decrement value
for i in range(10, 0, -1):
    print(i)
# Will print 10 to 1

# For loop decreasing with user value
num = input("Input number:")
for i in range(10, 0, -1):
    print(int(num)*i)
# Will print num*(10 to 1)

# For loop using list
list1 = [1, 3, 5, 7, 9, 12, 20, "one", "two", "three"]
for i in list1:
    print(i)
# Will print all values in list1

# For loop using string as a list
for i in "testing":
    print(i)
# Will print all letters in "testing" in sequential order

# List that adds values together
li = [43, 56, 34, 45, 77]
z = 0
for i in li:
    z = z + i
print("sum is " + str(z))
# Will print "sum is 255"

# Simple break loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Will print 1 to 4, breaks at 5

# Use continue to skip multiples of 10
num = input("Enter number:")
for i in range(1, 11):
    if int(num) * i % 10 == 0:
        continue
    print(int(num)*i)
# Will print num*(1 to 10), except multiples of 10

# else executes once loops end
for i in range(1, 11):
    print(i)
else:
    print("loop has ended")
# Will print 1 to 10 and then print "loop has ended"

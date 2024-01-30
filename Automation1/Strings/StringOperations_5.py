a = "Hello"
b = "Hello"
c = " Hello"
d = "Hello "
e = "hello"
f = "HelLo"

# Check to see if two strings are the same
if a == b:
    print("Strings are the same")
else:
    print("Strings are not same")

# Check to see if two strings are the same, regardless of spaces, case-sensitive
if a.strip() == b.strip():
    print("Strings are the same")
else:
    print("Strings are not same")

# Check to see if two strings are the same, case-insensitive
if e.upper() == f.upper():
    print("Strings are the same")
else:
    print("Strings are not the same")

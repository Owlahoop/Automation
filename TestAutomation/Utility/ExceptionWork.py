try:
    user_input1 = input("Please enter first number:")
    user_input2 = input("Please enter second number:")
    c = int(user_input2) + int(user_input1)
    print(c)
except:
    print("Incorrect input")
finally:
    print("This executes at end")
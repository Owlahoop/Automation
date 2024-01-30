name = input("Name:")
math = input("Math Score:")
sci = input("Science Score:")
eng = input("English Score:")

avg = (int(math)+int(sci)+int(eng))/3

print("User name is " + name + ", Scored " + str(avg) + "% in exams")
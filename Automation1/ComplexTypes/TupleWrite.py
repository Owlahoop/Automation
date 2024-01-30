programming_lang = (2021, "C#", "Java", "Python", True, False)
new_programming = ("PHP", "GROOVY")

# Combine two tuples
final_tuple = programming_lang + new_programming
print(final_tuple)

# Update value in tuple
programming_lang[2] = "Javascript"
print(programming_lang)
# Displays error, cannot update tuple

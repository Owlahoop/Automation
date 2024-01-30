programmingLanguage = [2021, 'Java', 'C#', 'Python', True, False]
programmingLanguage_latest = ['PHP', 'Ruby']

final_list = programmingLanguage + programmingLanguage_latest
print(final_list)
print(len(final_list))

# Write operations on list and update values on list
programmingLanguage[2] = 'C++'
print("***Updated_List***")
print(programmingLanguage)

# Insert values to list
programmingLanguage.insert(2, "PHP Language")
print("***Added_Value_In_List***")
print(programmingLanguage)

# Delete Value in the list
programmingLanguage.remove('Java')
print("***Removed_Value_In_List***")
print(programmingLanguage)

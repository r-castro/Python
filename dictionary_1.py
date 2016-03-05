# Creating, accessing and modifying a dictionary

empty_dictionary = {}
print("The value of empty_dictionary is", empty_dictionary)

grades = {"John": 87, "Steve": 76, "Laura": 92, "Edwin": 89}
print("\nAll grades:", grades)

print("\nSteve's current grade:", grades["Steve"])
grades["Steve"] = 90
print("Steve's new grade:", grades["Steve"])

grades["Michael"] = 93
print("\nDictionary grades after modification:")
print(grades)

del grades["John"]
print("\nDictionary grades aftrr deletion:")
print(grades)

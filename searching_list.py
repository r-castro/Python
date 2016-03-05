# Searching a list for an integer

alist = range(0, 199, 2)

search_key = int(input("Enter integer search key: "))

if search_key in alist:
    print("Found at index:", alist.index(search_key))
else:
    print("Value not found")

counter = 0
sum = 0
while True:
    this_input = float(input('#? :~> '))
    if this_input < 0:
        if counter == 0:
            print("You haven't entered any numbers yet!")
            continue
        break
    sum += this_input
    counter += 1
    print(counter, ":", sum)

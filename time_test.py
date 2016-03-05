# Creating and manipulating object of class time


from time import Time

time1 = Time()

print("The attributes of time1 are: ")
print("time1.hour:", time1.hour)
print("time1.minute:", time1.minute)
print("time1.second:", time1.second)


print("Calling method print_military:", time1.print_military())
print("Calling method print_standard:", time1.print_standard())

print("Charging time1's hour atrribute... ")
time1.hour = 25
print("Calling method print_military after alteration:",
      time1.print_military(), end="")

# Cretating and accessing tuples.

hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
second = int(input("Enter second: "))

current_time = hour, minute, second

print("The value of current_time is:", current_time)

print("The number of seconds since midnight is",
      (current_time[0] * 3600 + current_time[1] * 60 + current_time[2]))

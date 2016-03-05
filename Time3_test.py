from Time3 import Time


def print_time_values(timeToPrint):
    print(timeToPrint.print_military())
    print(timeToPrint.print_standard())

time1 = Time()
time2 = Time(2)
time3 = Time(21, 34)
time4 = Time(12, 25, 42)

print("Constructed with:")

print("\nall arguments defaulted:")
print_time_values(time1)
print("hour specified; minute and second defaulted:")
print_time_values(time2)
print("hour and minute soecified; second defaulted:")
print_time_values(time3)
print("hour, minute and second specified:")
print_time_values(time4)

# Drive to test class TimeControl

from Time2 import Time


time = Time()

print("The initial military time is", time.print_military())
print("\nThe initial standard time is", time.print_standard())


time.time(13, 27, 6)
print("\n\nMilitary time after time is", time.print_military())
print("\nStandard time after time is", time.print_standard())

time.hour = 4
time.minute = 3
time.second = 34

print("\n\nMilitary time after hour, minute, second is",
      time.print_military())
print("\nStandard time after hour, minute, second is",
      time.print_standard())

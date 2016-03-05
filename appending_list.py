# Appending items to a list.

playlist = []

print("Enter your 5 favorite Shakespearean plays.\n")

for i in range(5):
    playname = input("Play %d: " % (i + 1))
    playlist.append(playname)

print("\nSubscript           Value")

for i in range(len(playlist)):
    print("%9d     %-25s" % (i + 1, playlist[i]))

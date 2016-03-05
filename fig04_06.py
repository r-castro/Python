# Random integer produced by randrange

import random

for i in range(1, 21):
    print("%10d" % (random.randrange(1, 7)))

    if i % 5 == 0:
        print

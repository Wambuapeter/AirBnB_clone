import random
import math

# bubblesort LOL
# get random variables
randnum = []
for i in range(5):
    randnum.append(random.randrange(1, 9))
i = len(randnum) - 1
while i > 0:
    j = 0
    while j < i:
        print("\nis {} > {}?".format(randnum[j], randnum[j+1]))
        if randnum[j] > randnum[j+1]:
            print('switch')
            temp = randnum[j]
            randnum[j] = randnum[j+1]
            randnum[j+1] = temp
        else:
            print("Don't switch")
        j += 1

        for k in randnum:
            print(k, end=", ")
        print()
    print("End of round")
    i -= 1
for k in randnum:
    print(k, end=", ")
print()

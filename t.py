import random

for repetition in range(3):
    print("Repetition {}:".format(repetition))
    for i in range(10):
        random.seed(1)
        print(random.random())
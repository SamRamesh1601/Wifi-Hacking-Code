import math


def process_bar(process , total):
    present = 100 * (process / float(total))
    bar = '#' * int(present) + "-" * (100 - int(present))
    print(f"\r|{bar}| {present:.2f}% ",end="\r")

numbers = [i*5 for i in range(2000,3000)]
results = []

process_bar(0,len(numbers))
for i , number in enumerate(numbers):
    results.append(math.factorial(number))
    process_bar(i+1 , len(numbers))
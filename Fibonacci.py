import numpy as np
import time

MAX_FIB_INDEX = 100

def main():
    testing([10, 20, 30])


def fib_bf(index):
    if(index == 0 or index == 1):
        return index
    else:
        return fib_bf(index - 1) + fib_bf(index - 2)

list = [-1] * MAX_FIB_INDEX
list[0] = 0
list[1] = 1

def fib_dp(index):
    if(list[index] is not -1):
        return list[index]
    else:
        list[index] = fib_dp(index - 1) + fib_dp(index - 2)
        return list[index]

def testing(testing_nums):

    for num in testing_nums:
        print("\nBrute Force Fibbonacci (", num, "): ")
        start = time.time()
        fib_bf(num)
        end = time.time()
        print("Elapsed Time: ", end - start, " seconds")

        print("\nDynamic Programming Fibbonacci (", num, "): ")
        start = time.time()
        fib_dp(num)
        end = time.time()
        print("Elapsed Time: ", end - start, " seconds")

if __name__ == "__main__":
    main()
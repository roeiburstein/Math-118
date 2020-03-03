import time

MAX_FIB_INDEX = 501

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

def fib_dp_top_down(index):
    if(list[index] is not -1):
        return list[index]
    else:
        list[index] = fib_dp_top_down(index - 1) + fib_dp_top_down(index - 2)
        return list[index]

def fib_dp_bottom_up(index):
    my_list = [0, 1]
    for iter in range(2, index + 1):
        my_list.append(my_list[iter - 1] + my_list[iter - 2])
    return my_list[index]

def testing(testing_nums):
    for num in testing_nums:
        print("\nBrute Force Fibbonacci (", num, "): ")
        start = time.time()
        fib_bf(num)
        end = time.time()
        print("Elapsed Time: ", end - start, " seconds")

        print("\nTop Down Dynamic Programming Fibbonacci (", num, "): ")
        start = time.time()
        fib_dp_top_down(num)
        end = time.time()
        print("Elapsed Time: ", end - start, " seconds")

        print("\nBottom Up Dynamic Programming Fibbonacci (", num, "): ")
        start = time.time()
        fib_dp_bottom_up(num)
        end = time.time()
        print("Elapsed Time: ", end - start, " seconds")

if __name__ == "__main__":
    main()
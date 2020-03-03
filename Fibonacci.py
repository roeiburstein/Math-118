import time

MAX_FIB_INDEX = 501 # Used for array with -1's for top-down dp

def main():
    testing([10, 20, 30])

# Generic fibonacci recursive function: order O(n^2)
def fib_bf(index):
    if(index == 0 or index == 1):
        return index # fib(0) = 0 and fib(1) = 1, so just return index
    else:
        return fib_bf(index - 1) + fib_bf(index - 2) # fib(n) = fib(n-1) + fib(n-2)

list = [-1] * MAX_FIB_INDEX # Creates list with MAX_FIB_INDEX number of -1's
list[0] = 0
list[1] = 1

# DP Fibonacci starting from target index and going backward
def fib_dp_top_down(index):
    if(list[index] is not -1):
        return list[index]
    else:
        list[index] = fib_dp_top_down(index - 1) + fib_dp_top_down(index - 2)
        return list[index]

# DP Fibonacci starting from index 2 (fib(0)=0 and fib(1)=1) to target index
def fib_dp_bottom_up(index):
    my_list = [0, 1]
    for iter in range(2, index + 1): # fib(0) and fib(1) are predefined
        my_list.append(my_list[iter - 1] + my_list[iter - 2]) # Add fib(iter) to the list
    return my_list[index]

# Tester for each type of fibonacci with associated elapsed times:
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
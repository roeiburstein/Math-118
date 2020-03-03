import time

def main():
    print("Brute Force Fibbonacci:")
    start = time.time()
    fib_brute_force(5)
    end = time.time()
    print("Elapsed Time: ", end - start, " seconds")

def fib_brute_force(index):
    if(index == 0 or index == 1):
        return index
    else:
        return fib_brute_force(index - 1) + fib_brute_force(index - 2)

if __name__ == "__main__":
    main()
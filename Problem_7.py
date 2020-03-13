import numpy as np

P = np.array([[0, 1, 1/2, 1/3], [1, 0, 0, 1/3], [0, 0, 0, 1/3], [0, 0, 1/2, 0]], np.float64)

def main():
   NUM_PRODUCTS = 1000
   # v = np.random.rand(4, 1)
   v = np.array([1, 2, 3, 4])
   for i in range(NUM_PRODUCTS):
      v = np.matmul(P, v)
   print(v)
   print("\n\n\n", np.matmul(P, v))

if __name__ == "__main__":
    main()
import numpy as np

P = np.array([[0, 1, 1/2, 1/3],
              [1, 0, 0, 1/3],
              [0, 0, 0, 1/3],
              [0, 0, 1/2, 0]], np.float64)
P_tilda = np.array([[0.0125, 0.9625, 0.4875, 0.329166],
                    [0.9625, 0.0125, 0.0125, 0.329166],
                    [0.0125, 0.0125, 0.0125, 0.329166],
                    [0.0125, 0.0125, 0.4875, 0.012]])
#print(np.sum(P_tilda,axis=0))
def main():
   NUM_PRODUCTS = 20
   v = np.random.rand(4, 1)
   #v = np.array([1, 2, 3, 4])
   for i in range(NUM_PRODUCTS):
      v = np.matmul(P_tilda, v)
   print(v)
   print("\n\n\n", np.matmul(P_tilda, v))

if __name__ == "__main__":
    main()
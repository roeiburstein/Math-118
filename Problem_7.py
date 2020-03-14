import numpy as np

P = np.array([[0, 1, 1/2, 1/3],
              [1, 0, 0, 1/3],
              [0, 0, 0, 1/3],
              [0, 0, 1/2, 0]], np.float64)
P_tilda = np.array([[0.0125, 0.9625, 0.4875, 0.329166],
                    [0.9625, 0.0125, 0.0125, 0.329166],
                    [0.0125, 0.0125, 0.0125, 0.329166],
                    [0.0125, 0.0125, 0.4875, 0.0125]])
def main():
   NUM_PRODUCTS = 10000
   v = np.random.rand(4, 1)
   for i in range(NUM_PRODUCTS):
      v = np.matmul(P_tilda, v)
   two_norm = np.linalg.norm(v)
   for j, i in enumerate(v):
      v[j] = (i / two_norm)
   print(v)
   print("\n\n", np.matmul(P_tilda, v))
   print("\n\n", np.linalg.eig(P_tilda)[1])
if __name__ == "__main__":
    main()
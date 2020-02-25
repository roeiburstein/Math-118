import numpy as np

def main():
   dim = 3
   A = np.random.rand(dim, dim)
   B = np.array([[4, 1, 7, 9], [1, 6, 3, 1], [4, 8, 9, 9], [12, 6, 1, 9]], np.float64)
   # print("A: \n", A)
   print("B: \n", B)
   L, U = decompose(B)
   print("\nL: \n", L, "\nU: \n", U)
   print("\nL*U: \n", np.dot(L, U))

def decompose(matrix):
   dim = len(matrix)
   L = np.identity(dim, np.float64)  # Identity matrix to be filled in later

   for num in range(dim):
      curr_col = matrix[:, num]
      curr_pivot = curr_col[num]
      if curr_pivot == 0:
         print("Error: pivot is zero, row permutations needed")
         return None, None

      for count in range(num + 1, dim):
         multiplier = -1 * (curr_col[count] / curr_pivot)
         new_row = matrix[count] + (multiplier * matrix[num])
         matrix[count] = new_row
         L[count, num] = (-1 * multiplier)
   return L, matrix

if __name__ == "__main__":
    main()
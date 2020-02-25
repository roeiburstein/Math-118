import numpy as np

def main():
   dim = 3
   A = np.random.rand(dim, dim)

   print("A: \n", A)
   L, U = decompose(A)
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
import numpy as np

def main():
   test_1()

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


def linear_system(A, b):
   L, U = decompose(A) #LU = A -> LUx = b
   y = np.zeros(len(A), np.float) # We will build y such that Ly = b

   for row in range(len(A)):
      sum = b[row]
      for col in range(len(A)):
         if(col != row):
            sum -= L[row][col] * y[col]
      y[row] = sum

   x = np.zeros(len(A), np.float) # We will build x such that Ux = y

   for row in range(len(A) - 1, -1, -1):
      sum = y[row]
      for col in range(len(A)):
         if(col != row):
            sum -= U[row][col] * x[col]
         else:
            divisor = U[row][col]
      x[row] = sum / divisor

   return x

def test_1():
   A = np.array([[2, 4, -4],
                 [1, -4, 3],
                 [-6, -9, 10]], np.float64)

   b = np.array([12, -21, -24])

   print(linear_system(A, b)) # Expected: x = [-4, 2, -3]

if __name__ == "__main__":
    main()
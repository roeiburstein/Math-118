import numpy as np

def main():
   # test_1()
   # test_2()
   A = np.array([[2, 4, -4],
                 [1, -4, 3],
                 [-6, -9, 10]], np.float64)

   b = np.array([12, -21, -24])

   linear_system(A, b)

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
   L, U = decompose(A)
   y = np.zeros(len(A), np.float)

   for row in range(len(A)):
      sum = b[row]
      for col in range(len(A)):
         if col != row:
            sum -= L[row][col] * y[col]
      y[row] = sum

   x = np.zeros(len(A), np.float)

   #LUx=b
   #Ly=b
   #Ux=y

def test_1():
   dim = 3
   A = np.random.rand(dim, dim)
   print("A: \n", A)
   L, U = decompose(A)
   print("\nL: \n", L, "\nU: \n", U)
   print("\nL*U: \n", np.dot(L, U))

def test_2():
   B = np.array([[4, 1, 7, 9], [1, 6, 3, 1], [4, 8, 9, 9], [12, 6, 1, 9]],
                np.float64)
   print("B: \n", B)
   L, U = decompose(B)
   print("\nL: \n", L, "\nU: \n", U)
   print("\nL*U: \n", np.dot(L, U))

if __name__ == "__main__":
    main()
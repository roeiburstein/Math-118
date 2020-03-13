import numpy as np

A = np.array([[0.5377, -0.8622],
              [1.8339, 0.3188],
              [-2.2588, 1.3077]], np.float64)

b_trans = np.array([-0.4336, 0.3426, 0.5163], np.float64)
b = np.transpose(b_trans)

a = 0.01
x_0 = np.transpose(np.array([0, 0]))


def main():
   x_1 = x_k_plus_one(x_0)
   x_2 = x_k_plus_one(x_1)
   x_3 = x_k_plus_one(x_2)

   print("x_1: ", x_1)
   print("x_2: ", x_2)
   print("x_3: ", x_3)



def x_k_plus_one(x_k):
   return P_x(x_k - a * grad_f(x_k))

def grad_f(x_k):
   C = np.matmul(A, x_k) - b
   return np.matmul(2*np.transpose(A), np.transpose(C))

def P_x(v):
   for j, i in enumerate(v):
      if i >= 0:
         continue
      else:
         v[j] = 0
   return v

if __name__ == "__main__":
    main()
import numpy as np
import math

I= np.array([[232, 177, 82, 7],
             [241, 18, 152, 140],
             [156, 221, 67, 3]])

x = float(input("Enter first number : "))
y = float(input("Enter second number: "))

def bilinear_interpolate_numpy(I, x, y):
   x0 = math.floor(x)
   x1 = x0 + 1
   y0 = math.floor(y)
   y1 = y0 + 1



   Ia = I[y0, x0]
   Ib = I[y0, x1]
   Ic = I[y1, x0]
   Id = I[y1, x1]

   ax = x-x0
   ay = y-y0
   a_x = 1-ax
   a_y = 1-ay


   return (a_x*a_y*Ia)+(ax*a_y*Ib)+(a_x*ay*Ic)+(ax*ay*Id)
print ("numpy result:", bilinear_interpolate_numpy(I,x,y))



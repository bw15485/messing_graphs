import numpy as np     #use numpy for whenever you dealing with arrays

u = np.array(range(1,5))  #creates an array from 1-4

v = np.array([[1,2],[3,4]]) #creates 2d array
#print(v[0,1])   #will print out 2 (0th row, 1st column)

#print(v.shape) # prints shape of array e.g (2,2) as 2 rows and 2 cols
#print(v.size)   #prints size of array

x = np.arange(0,10,1)   #creates an array from 0-9 with step size 1

y = np.linspace(0,10,25) #linspace includes both end points

z = np.random.rand(5,5)  #produces a 5 by 5 matrix filled with random numbers between 0 and 1

a = np.eye(3)  #eye is the inditiy matrix 3 denotes size of the matrix

b = np.zeros((3,3))  #creates a 3 by 3 zero matrix

c = np.array([n for n in range(5)])   #creatsa an array from 1-4

mask = (2 < c) * (c < 4)

#print(mask)   #this will print an boolean array with true for the elemtents that satisy e.g 3 and false everyelse

d = np.array([[1,2],[3,4]])
e = np.array([[2,2],[2,2]])

f = np.dot(d,e)   #matrix multiplication

g = np.mean(d) #finds mean of matrix, you can also use sum, mean, std, var, min and max here
















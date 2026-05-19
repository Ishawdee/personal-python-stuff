import numpy as np # faster than python lists

a = [[1,2,3],[4,5,6]] # all rows must have the same size, cuz numpy arrays are fixed
arr = np.array(a, dtype=float)
print(arr)
print(arr.shape) # a tuple (here: (2, 3))
print(arr.dtype) # int32, float64, etc...
print(arr[0, 1]) # element in 1st row, 2nd column

mlist = [1, 2 , 0.5, 0, -1, "s"]
arr2 = np.array(mlist, dtype=bool) # all true except for 0

arr3 = np.ones(shape=(2,),dtype=int) # 1D array with 2 int elements
print(arr3)

arr4 = np.zeros(shape=(2, 4), dtype=float) # 2D array, each dimention has 4 float zero elements
print(arr4) #arr4.size == number of all elements in arr4
print(arr4.size) # == 2 * 4

print(np.array(range(5))) # a 1D array with elements in range 0 to 4
print(np.arange(6)) # 1D array with elements in range 0 to 5
arr5 = np.arange(25) # 1D array from 0 to 24
print(arr5[3])
arr6 = np.array([[1, 2], [3, 4]])
print(arr6[1, 1]) # so don't use [][]. just use one []. [D1, D2, D3,..., Dn]
print(arr6[0, :]) # everything in the first dimension a.k.a [1 2]
evens = (arr6 % 2) == 0 # only even numbers
print(arr6[evens])
print("***")
arr7 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr7[:][1])
print(arr7[:, 1]) # element in index1 of all rows
arr8 = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
arr8[:, 1:3] = [10, 10] # from all rows, elements between index 1 to 2 will be 10 and 10
print(arr8)
arr5 = np.arange(24)
reshaped = arr5.reshape(1, 4, 6) # 1 * 4 * 6 == 24 so it matches the og array's size!
print(arr5)
print(reshaped)
arr8 = np.array([[1,2,3], [4,5,6]])
shaped = arr8.shape
print(shaped[1])
arr9 = np.ones(shape=(3, 4))
print(arr9)
print(arr9.reshape(6, -1)) # you can use -1 in each of these places freely. if the other number is
# divisble by the product of the og shapes aka size (in arr9 case: 12), then numpy itself will find the
# acutal number for placeholder "-1". In this reshape case, you used -6, which is indeed divisible
# by 12. so you could use -1, and python found out this placeholder was actually 12 / 6 == 2.

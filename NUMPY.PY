import random
from array import array
import numpy as np
# lst =[5,3,7,8,9]

# arr = np.array([[5,7,8,4,3],[5,7,9,4],[2,3,4,6],[5,7,8,9]])
# print (type(arr))
# print(type(lst))
# print(arr.ndim)
# print(arr.dtype)
# print(arr.shape)




# arr =np.ones(shape=(4,3),dtype=np.int32)
# print(arr)

# arr = 17 *np.ones(shape=((3,2,2)))
# print(arr)


# arr = np.arange(5,100,2)
# print(arr)

# arr = np.linspace(1,50,10)
# print(arr)
#
# arr =np.arange(1,21).reshape((4,5))  #importtant
#
# print(arr)
# print(len(arr))
# print(arr.shape)
#                                    # print(arr[4:6])
# print(arr.T)

#which index we waNTR  WE CAN ALSO PROVISW as a list

# print(arr[[2,4,6,7,8,]])



#woh sara elemnt jo greateer than 15 hen samjha ka nhi 

# print(arr[arr>15])
# print(arr%3==0)


#this randomly change the numbers i give  rows and columns 
arr = np.random.randint(5,95,(3,4))
print(arr)

arr =np.random.randint(5,95).reshape(4,3)
print(arr)
# arr =np.random.randint



#EXERCISE SOLVING 

from ctypes import c_uint
from random import sample
import numpy as np
from array import array

#ques 1
# arr  =np.arange(100,200,10).reshape((5,2))
# print(arr)

#ques2>

# samplearray =np.array([[11,22,33],[44,55,66],[77,88,99]])
# print(samplearray[0:3,2])        

# sample =np.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])
# print(sample)
# print(sample[sample % 2==0])
# print(sample[sample%2 !=0])

#ques 4
# arr1 = np.random.randint(500,700,(4,4))
# print(arr1)

# arr2  =np.random.randint(500,700,(4,4))
# print(arr2)

# totarr =arr1+arr2
# print(totarr)
# print()
# print(totarr[totarr%5 ==0])

#ques 5

# array = np.random.randint(100,150,(10,10))
# print(array[array%5==0])


#electricity bill


#
# arr1 =np.random.randint(())
# print(arr1)



                                                                                                                                                                                                                                                                                                                       
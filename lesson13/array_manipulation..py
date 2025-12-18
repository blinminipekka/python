import numpy as np

arr_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element = arr_2d[1,2]
prnt(element)

dimension = arr_2d.ndim
print(dimension)

shape = arr_2d.shape
print(shape)

size=arr_2d.size
print(size)

sub_array=arr_2d[:2,:2]
print(sub_array)

sub_array_2=arr_2d[-4:,-4:]
print(sub_array_2)

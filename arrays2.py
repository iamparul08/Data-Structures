#python code to demonstrate pop() and remove()
#importing "array" for array

import array

arr = array.array('i', [1, 2, 3, 1, 5])
#printing original array
print("The new created array: ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")
print("\r")
#using pop() to remove element at 2nd position
print("The popped element is : ", end=" ")
print(arr.pop(2))
#printing array after popping the element
print("The array after popping is: ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")

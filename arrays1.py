#python code to demonstrate the working of array(), append(), insert()
#importing "array" for array operations

import array
#initializing array with array values
#initializing array with signed integers

arr = array.array('i', [1, 2, 3])

#printing original array
print("The new created array: ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")

print("\r")

#using append() to insert new value at the end
arr.append(4);
#printing appended array
print("The appended array is: ", end=" ")
for i in range(0, 4):
    print(arr[i], end=" ")

#using insert() to insert value at specified position
#inserts 5 at 2nd position
arr.insert(2, 5)
print("\r")

#printing array after insertion
print("The array after insertion: ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")

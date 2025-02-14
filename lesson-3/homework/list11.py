'''list1=[1,2,3,4,3,4,5,]
list2=list1.remove(3)
print(list2)
list3 = list2.remove(4)
print(list3)'''
list1 = [1, 2, 3, 4, 3, 4, 5]

list1.remove(3)  # Removes the first 3
print(list1)  # Output: [1, 2, 4, 3, 4, 5]

list1.remove(4)  # Removes the first 4
print(list1)  # Output: [1, 2, 3, 4, 5]
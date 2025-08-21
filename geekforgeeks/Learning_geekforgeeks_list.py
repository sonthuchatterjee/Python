import sys
import time
import functools

# list =list(map(int,input("Please enter the numbers as you wish: ").split()))
# print(f"the list is {list} and the type of the object 'list' is {type(list)}")

# x,y,z = input("Please enter the number you wish:").split()
# print('the numbers are {0} and {1} and {2}'.format(x,y,z))

# x = input("Please enter the number you wish:").split()
# print(type(x))
# list.append()
# list.insert(0,1) # list.insert(<position>,<value>)
# list.extend([1,2,3]) # for multiple inserts at the end
# list.remove()
# list.pop()
# list.index()
# list.count()
# list.sort() # list.sort(key=<function>,reverse=True) returns nothing but sorts the original 
# list.copy()
#list.reverse()

# list = [1, 3, 5, 6, 2]

def sum(a,b):
    return a+b
#print(functools.reduce(sum,list))


# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
 
 
# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
 
# # using filter function
# filtered = filter(fun, sequence)
# # for s in filtered:
# #     print(s)
# print(list(filtered))
list1=[1,2,3,4]
list2=[5,6,7,8]
additions=map(sum,list1,list2)
print(list(additions))

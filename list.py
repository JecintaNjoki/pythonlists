# 1. Write a Python program to sum all the items in a list.
list= [20,30,42,46,48]
def listsum(nums):
    numbers = 0
    for x in nums:
        numbers += x
    return numbers
print(listsum([-20,30,42,46,48]))
# 2. Write a Python program to multiply all the items in a list. 
def listmultiply(nums):
    numbers=1
    for x in nums:
        numbers*=x
    return numbers
print(listmultiply([22,8,7,15,4,9]))

# 3. Write a Python program to get the largest number from a list.
list=[12,24,26,15,37,56,78]
print("Largest number is", max(list))

# 4. Write a Python program to get the smallest number from a list. Go to the editor
list=[12,24,26,15,37,56,78]
print("smallest number is", min(list))

# 5. Write a Python program to count the number of strings from a given 
#list of strings. The string length is 2 or more and the first and last 
#characters are the same. 
list =['abc', 'xyz', 'aba', '1221']
print("number of strings",len(list))



# 6. Write a Python program to get a list, sorted in increasing
#  order by the last element in each tuple from a given list of 
# non-empty tuples. 
list = [(2, 5), (1, 2), (4, 4), (2, 3),(2, 1)]
print(list.sort())


# 7. Write a Python program to remove duplicates from a list. 
# Click me to see the sample solution
list =[10,20,30,40,50,10,20,30]
result = [] 
for i in list: 
    if i not in result: 
        result.append(i) 
print ("removed duplicates list" + str(result))


# 9. Write a Python program to clone or copy a list.

list = [3, 7, 2, 10, 31, 28]
list1 = list[slice(len(list))]
print("list:", list)
print("copy", list1)

#10 Given two lists, write a function to find the common elements 
# between them and return them in a new list.
def numbers(nums):
    list1 = [10, 11,12,13,14,20] 
    list2 = [20,30,42,10,11,12]
    print(list1.intersect(list2))
    
    
   
   

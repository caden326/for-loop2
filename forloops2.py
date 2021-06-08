"""1 Countdown - Create a function that accepts a number as an input.
Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)."""

def reverse(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list
print(reverse(5))

"""2 Print and Return 
- Create a function that will receive a list with two numbers.
Print the first value and return the second."""

def prntandret(list):
    print (list[0])
    return list[1]
print (prntandret([24,66]))

#3 Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def ifyourenotfirstyourelast(list):
    length_var = len(list)
    list_var = list[0]
    
    return  length_var + list_var
print(ifyourenotfirstyourelast([3,7,8,9]))


"""4 Write a function that accepts a list and creates a new list
containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. If the list has less than 2 elements, 
have the function return False"""
def greaterthansecond(list):
    if len(list)<2:
        return False

    list1 = []
    for val in list:
        if val>list[1]:
            list1.append(val)
    print(len(list1))    
    return list1
    
print(greaterthansecond([5,2,3,2,1,4]))
print(greaterthansecond([5]))

""" 5 Write a function that accepts two integers as parameters: size and value.
The function should create and return a list whose length is equal to the given size,
and whose values are all the given value."""

def lengthAndValue(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(lengthAndValue(4,7))
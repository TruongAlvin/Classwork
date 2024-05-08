#Alvin Truong
#5/8/2024

#Creating an empty list
lst = []

#using a for loop to add the numbers 1 through 100, to the list
for a in range (1,101):
    lst.append(a)

#printing the list
print(lst)

#creating an empty list named odd
odd = []

#using a for loop to add odd numbers 1-100 to the list odd
for b in range (1,101,2):
    odd.append(b)

#Printing the list odd
print(odd)

#creating the empty list even
even = []

#using a forlooop to add even numbers 1-100 to the list even
for c in range (2,101,2):
    even.append(c)

#printing the list even
print (even)

#create a variable named "b" that points to the first list that you created
b = lst

#create a variable named joined, and joins an even and odd list by using an operator
joined = lst
lst+[even,odd]
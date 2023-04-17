'''
2. Write a Python program to create a function that takes one argument,
 and that argument will be multiplied with an unknown given number. 
 
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75

'''

number = int(input("Enter the number:"))
double = lambda a : a * 2
triple = lambda a : a * 3
quadruple = lambda a : a * 4
quintuple = lambda a: a * 5
print(double(number))
print(triple(number))
print(quadruple(number))
print(quintuple(number))
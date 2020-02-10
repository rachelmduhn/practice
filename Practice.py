# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:35:56 2020

@author: rache
"""
#page 18 finger exercise: Write a program that examines three variables- x, y, and z- and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.
x = 19
y = 11
z = 13
if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x > y and x > z:
        print(x , 'is the largest odd number')
    elif y > z:
        print(y , 'is the largest odd number')
    else:
        print(z , 'is the largest odd number')
elif x%2 != 0 and y%2 != 0:
    if x > y:
        print(x , 'is the largest odd number')
    else:
        print(y , 'is the largest odd number')
elif x%2 != 0 and z%2 != 0:
    if x > z:
        print(x , 'is the largest odd number')
    else:
        print(z , 'is the largest odd number')
elif y%2 != 0 and z%2 != 0:
    if y > z:
        print(y , 'is the largest odd number')
    else:
        print(z , 'is the largest odd number')
elif x%2 != 0:
    print(x , 'is the largest odd number')
elif y%2 != 0:
    print(y , 'is the largest odd number')
elif z%2 != 0:
    print(z , 'is the largest odd number')
else:
    print(x , y , z , 'are not odd numbers')
            
            
    
    
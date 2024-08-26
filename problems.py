#1. Area of circle
"""
radies = int (input("Enter the radius: "))
area = 3.14 * (radies ** 2)
print(f"the area of cirle is:{area}")
"""
#2. qudradic eqation
"""
a= int(input("enter value a:"))
b= int(input("enter value b:"))
c= int(input("enter value c:"))
d= ((b**2) - 4*a*c)
root1 = (-b + d**(0.5))/2*a 
root2 = (-b - d**(0.5))/2*a 
print(f"the quadradic value is: {root1}" )
print(f"the quadradic value is: {root2}" )
"""
#3. swaping with and with out temp
"""
a=int(input("Enter value a"))
b=int(input("Enter value b"))

#with temp-----
temp=a
a=b
b=temp

#without temp--------
a= a+b
b= a-b
a= a-b
print(f"the swaped number a is {a}")
print(f"the swaped number b is {b}")
"""
"""
#converting temperature
c=int(input("Enter vaule of c: "))
f=(c*(9/5)+32)
k=273+c
print(f"converted f value is :{f}")
print(f"converted k value is :{k}")
"""

#simple project
"""
a=int(input("Enter the value 1: "))
b=int(input("Enter the value 2: "))
op=(input("Enter the operation: "))
if op == "+" :
    print(f"sum of two numbers is: {a+b}")
elif op == "-" :
    print(f"subtraction of two numbers is: {a-b}")
elif op == "*" :
    print(f"multiplation of two numbers is: {a*b}")
elif op == "/" :
    print(f"div of two numbers is: {a/b}")
else :
    print(f"worng in put {op}")
"""
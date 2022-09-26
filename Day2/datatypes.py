# Primitive Data Types

#string
print("Hello"[4])

#integer
x=10

#float
y=3.548

#boolean
values=True
otherValues=False

#type() function
#type function used to check the data type.

a=20
print(type(a))

#data type convertion/type casting(convert one data type to another data type)

a=20
print(type(str(a)))

z="123"
print(type(int(z)))

flo="145.856"
print(type(float(flo)))

#f-string- we can use where we have to print multiple data types without casting to string one by one.
age=35
height=1.75
win=True

print(f"My age is {age} , my height is {height} and my win is {win}")

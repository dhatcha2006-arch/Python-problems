# In the python the data types are selected automatically from the values.
# Incase we want to change any type we use the typecasting method.

# here the datatype will be choose depends on the value . 
# the value is 10. The 10 is an integer so the compiler will automatically know the datatype

a = 10 
b=10.00

print(type(a))
print(type(b))
b=int(b)            #here i change the type of the b value.
print(type(b))


a=True
print(type(a))
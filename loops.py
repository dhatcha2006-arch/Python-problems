 # for loop
 # while loop
 # break
 # continue
 # pass
 # Nested loops

i=j=1
for i in range(1,4):
    for j in range(i):
        print("*",end=" ")
    print()

# multiplication table

num = int(input("Enter a multiplier : "))
n=int(input("Enter n : "))
i=1
for i in range(1,n+1):
    mul=i*num
    print(i,"X",num,"=",mul)

# Factorial

num1 = int(input("Enter a num : "))
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)

# Reverce a number

num2=int(input("Enter a number : "))
reverse = 0
while num2>0:
    reverse = reverse*10+num2%10
    num2=num2//10
print(reverse)
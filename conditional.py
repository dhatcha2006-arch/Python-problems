mark = int(input("Enter your mark : "))

if mark<=100 and mark>=90:
    print(mark,"is A Grade...")
elif mark<90 and mark>=80:
    print(mark,"is B Grade...")
elif mark<80 and mark>=70:
    print(mark,"is C Grade...")
elif mark<70 and mark>=50:
    print(mark," is D Grade...")
elif mark>100:
    print("Invalid mark..")
else:
    print("Ur mark is",mark,",so Fail...")


name = input("Enter Your name : ")
password = int(input("Enter your password : "));

if name=="Dhatchanamoorthi" and password==1234:
    print("Login successful")

else:
    if name != "Dhatchanamoorthi":
        print("User_name error")
    if password != 1234:
        print("Incorrect password")
    

print("Dhatchanamoorhi" == name)
print("D" in name)



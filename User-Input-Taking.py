# here we write a code for taking user input like (Name, Age, City) as a input and store it to a variable and user can print it.

print("Hello user this side Yuvi here!")
print("Can you provide me your (Name, Age, City):")
user=str(input(print("If your our intrested just type ('Yes'or'No')")))
if user=="yes"or"Yes"or"YeS"or"YES":
    print("Got,it")
    name=str(input(print("Enter your Name:")))
    Age=int(input(print("Enter your Age:")))
    City=str(input(print("Enter your City:")))
    print("Uploding....")
    print(name,Age,City)
elif user=="No"or"NO":
    print("See you soon...")
else:
    print("Incorrect input")
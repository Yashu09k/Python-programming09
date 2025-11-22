#in this programe user can (+),(-),(x),(%) etc.
print("Welcome to Yuvi Calclutor program.")
print("What you want to perform")
print("Here is some method you can do with me:")
user=int(input(print("select the method",
      "1. Addition",
      "2. Subtraction",
      "3. Multiplation",
      "4. Divide",)))
num=int(input(print("Enter your first number:")))
num2=int(input(print("Enter your Second number:")))
add= num+num2
sub= num-num2
mul=num*num2
div=num/num2
result="This is your result:"

if user ==1:
    print(result,add)
elif user ==2:
    print(result,sub)
elif user ==3:
    print(result,mul)
elif user ==4:
    print(result,div)
else:
    print("please check your inputs")
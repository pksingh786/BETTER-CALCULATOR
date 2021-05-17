#this is a better calculatorin comparison of previous one
first_num=float(input("enter first number:"))
second_num=float(input("enter second number:"))
print("press + for addition")
print("press - for subtraction")
print("press * for Multiplication")
print("press / for division")
input=input("enter the symbol for which you want to perform a operation")
if input=="+":
    print(first_num+second_num)
elif input=="-":
    print(first_num-second_num)
elif input=="*":
    print(first_num*second_num)
elif input=="/":
    print(first_num/second_num)
else:
    print("invalid symbol")

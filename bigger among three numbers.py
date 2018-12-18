num1=input("Enter first number: ")
num2=input("Enter second number: ")
num3=input("Enter third number: ")
if(num1>num2 and num1>num3):
	print("number "+num1+" is bigger")
elif(num2>num1 and num2>num3):
	print("number "+num2+" is bigger")
else:
	print("number "+num3+" is bigger")
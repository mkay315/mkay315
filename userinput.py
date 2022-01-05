name = input("Please enter your name")
number1 = int(input("Please enter a number ")) #input() function takes the user input as string
number2 = int(input("Please enter next number "))
print(number1 + number2)



print("Sum is " + str(number1 + number2))
print("Sum of " + str(number1) + " and " + str(number2) + " is " + str(number1 + number2))
print("Sum of %d and %d is %d " %(number1, number2, number1 + number2))#%d - placeholder for integers, %f is placeholder for float, %s - string and boolean
print("Hello %s, Sum is %d" %(name, number1 + number2))


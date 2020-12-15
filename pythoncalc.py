# Asks for the inputs of the equation
one = int(input("What is the First Number:"))
two = int(input("What is the Second Number:"))


#Asks what you'd like to do to the numbers
print('Do you want it to "Multiply", "Divide", "Add", or "Subtract"?')
sign = input()
times = "MULTIPLY"
divide = "DIVIDE"
add = "ADD"
subtract = "SUBTRACT"

#^ marks the variables
# uses if statements to check and confirm then finish the equation

if sign.upper() == times:
 print(+ one * two)

if sign.upper() == divide:
    print( + one / two)

if sign.upper() == add:
    print(+ one + two)

if sign.upper() == subtract:
    print(+ one - two)

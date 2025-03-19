#Basic Calculator Program

#Create a simple Python program that asks the user to input two numbers 
#and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

numx=int(input('enter a number x:  '))
numy=int(input('enter a number y:  '))
operation=input('enter the opertion symbol e.g +, -, e.t.c:  ')
if operation=='+':
    results=numx+numy
    print(f'your results: {results}')
elif operation=='-':
    results=numx-numy
    print(f'your results: {results}')
elif operation=='*':
    results=numx*numy
    print(f'your results: {results}')
elif operation=='/':
    results=numx/numy
    print(f'your results: {results}')
else:
    print('unknown operand : hush i cannot help !')
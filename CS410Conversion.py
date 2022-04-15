'''
Created on Mar 10, 2022

@author: samir

This program uses an array to store as many numbers as the users inputs
Then will calculate similar to a calculator to add, subtract, divide and multiply all of the numbers
inputted into the program.
Then the program will return the total once the user has inputted a 0. The program will remove that
0 from the calculation to not interfere with the total returned.

The program will also ask for a username and password initially.
then it will encode the username and password and then decode them as well
If the username or password is incorrect the program will stop.
'''
import base64

'''
Creates all variables here with names that try to help explain what they are used for
'''
userInput = None
inputVals = []
num1 = None
num2 = 0
output = 0
username = "SNHU"
password = "student"
userUsername = None
userPassword = None

'''
Function used to multiply all numbers that are entered by the user.
This function starts with mulOutput = 1 to not zero out the multiplication by multiplying by 0
n = 0 to start the function by looping from the beginning of the array of inputs
then we remove the value of 0 because that is given to end the loop for inputs from the user so
that would also zero the function
'''
def multiply(arr):
    mulOutput = 1
    n = 0
    arr.remove(0)
    for i in range(len(arr)):
        n = arr[i]
        
        mulOutput *= n
    return mulOutput

'''
Function to divide all inputs from the user

divOutput is similar to the mulOutput in the multiplication function
set divOutput to the first variable input to start dividing from that number
Then remove 0 and the first number input so you don't divide by 0 or the first number
You'll remove 0 again to not divide by 0
'''
def divide(arr):
    divOutput = arr[len(arr) - 1]
    n = 0
    arr.remove (arr[len(arr) - 1])
    arr.remove(0)
    for i in range(len(arr)):
        n = arr[i]
        
        divOutput /= n
    return divOutput

#added encode the username and password stored above
username = base64.b64encode(username.encode("utf-8"))
password = base64.b64encode(password.encode("utf-8"))

#added from original program to check username/password
#encode user inputs
print("Input Username and Password for login")
userUsername = input("Username:")
#encodes username
userUsername = base64.b64encode(userUsername.encode("utf-8"))

userPassword = input("Password:")
#encodes password
userPassword = base64.b64encode(userPassword.encode("utf-8"))


#decode all inputs and stored data
username = base64.b64decode(username).decode("utf-8")
userUsername = base64.b64decode(userUsername).decode("utf-8")
password = base64.b64decode(password).decode("utf-8")
userPassword = base64.b64decode(userPassword).decode("utf-8")

#added to check inputs against stored data
if userUsername != username:
    print("Incorrect Username")
    quit()
if userPassword != password:
    print("incorrect password")
    quit()

#Infinite loop to allow user to continously check what the user has selected.
while True: 
    print("----------------")
    print("- 1)Add -")
    print("- 2)Subtract –")
    print("- 3)Multiply –")
    print("- 4)Divide -") #added from original program
    print("- 5)Exit –")
    print("----------------")
    #require integer input
    userInput = int(input())
    
    #First check the user input for entries that are not allowed
    if userInput == 5:
        break
    if (userInput > 5) or (userInput < 0):
        print("incorrect entry")
        break
    
    print("input 0 to end calculation")
    while num1 != 0:
        #require integer inputs only
        num1 = int(input("Enter integer:"))
        
        inputVals.insert(0, num1)
    #num2 = int(input("Enter the second number:"))
    
    if userInput == 1:
        #output = num1 + num2
        output = sum(inputVals)
        print(output)
    elif userInput == 2:
        output = inputVals[len(inputVals) - 1]
        for n in inputVals:
            output -= n
        output += inputVals[len(inputVals) - 1]
        print(output)
    elif userInput == 3:
        print(multiply(inputVals))
    elif userInput == 4:
        print(divide(inputVals))
    


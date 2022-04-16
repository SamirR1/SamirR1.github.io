//============================================================================
// Name        : CS410Module6.cpp
// Author      : sr
// Version     :
// Copyright   : Your copyright notice
// Description : C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int input;
	int num1;
	int num2;
	double output;
	while(true){
		cout << "----------------" << endl;
		cout << "- 1)Add -" << endl;
		cout << "- 2)Subtract –" << endl;
		cout << "- 3)Multiply –" << endl;
		cout << "- 4)Exit –" << endl;
		cout << "----------------" << endl;
		cin >> input;
//Security vulnerability corrected if input is not a int then the program will terminate
		if(cin.fail()){
			cout << "input is not a option." << endl;
			break;
		}

//Security vulneraility in the original C++ where if anything is input besides the numbers 1-5
//then the program breaks and will not stop running until the program is forcefully stopped.

//Vulnerability fixed by only accepting numbers 1-5 for the input statment that accepts the option used
			if(input == 5){
				break;
			}
			if(input == 4){
				continue;
			}
			cin >> num1;
//Security vulnerability corrected to only accept integers for the math portion.
			if(cin.fail()){
				cout << "input not a integer." << endl;
				break;
			}
			cin >> num2;
			if(cin.fail()){
				cout << "input not a integer." << endl;
				break;
			}
			if(input == 1){
				output = num1 - num2;
			}
			else if(input == 2){
				output = num1 + num2;
			}
			else if(input == 3){
				output = num1 / num2;
			}
			if(input > 5 || input < 0){
				cout << "incorrect entry" << endl;
				continue;
			}
//incorrect code. not really a vulnerability where the print statment isn't realtive to the number
//selected. if 1 is selected it should print +, if 2 then -, if 3 then /.
// the last print statement should say divide or the programming should multiply.
// not sure what they were going for with option 3.

		cout << num1 << " - " << num2 << " = " << output << endl;

	}
	return 0;
}



/*
 * '''
Created on Mar 10, 2022

@author: samir
'''
import base64

userInput = None
inputVals = []
num1 = None
num2 = 0
output = 0
username = "SNHU"
password = "student"
userUsername = None
userPassword = None

def multiply(arr):
    mulOutput = 1
    n = 0
    arr.remove(0)
    for i in range(len(arr)):
        n = arr[i]

        mulOutput *= n
    return mulOutput

def divide(arr):
    #set divOutput to the first variable input to start dividing from that number
    divOutput = arr[len(arr) - 1]
    n = 0
    #remove 0 and the first number input so you don't divide by 0 or the first number
    arr.remove (arr[len(arr) - 1])
    arr.remove(0)
    for i in range(len(arr)):
        n = arr[i]

        divOutput /= n
    return divOutput

#added encode the username and password stored above
username = base64.b64encode(username.encode("utf-8"))
password = base64.b64encode(password.encode("utf-8"))
#print(base64.b64encode(username.encode("utf-8")))
#print(base64.b64encode(password.encode("utf-8")))
#print(base64.b64decode(username).decode("utf-8"))
#print(base64.b64decode(password).decode("utf-8"))

#added from original program to check username/password
#encode user inputs
print("Input Username and Password for login")
userUsername = input("Username:")
userUsername = base64.b64encode(userUsername.encode("utf-8"))

userPassword = input("Password:")
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


 *
 **/
 */

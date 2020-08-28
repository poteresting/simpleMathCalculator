#Calculator that performs basic operations on entered equation (how eval() works)
import re

Equation = input('Enter an usolved equation (for example: - 1 + -2 - 3 * -4 / 5)\n')

Regnums = re.compile(r'\d+\.\d+|\d+') #Get the numbers here by pattern

Regop = re.compile(r'(\+|-|\*|/)\s*(\+|-)?') #Get the operators between numbers and the signs of the numbers as tuples (operator, sign of number)

matched_num = Regnums.findall(Equation)
print(matched_num) #prints the list of numbers in equation

matched_ops = Regop.findall(Equation)
print(matched_ops) #prints the list of operators in equation

if len(matched_ops) < len(matched_num): #adds an operator + to the first number if its positive
    matched_ops.insert(0, ('+', ''))
print(matched_ops)

operators_list = []
for i in range(len(matched_ops)):
    operators_list.append(matched_ops[i][0])
#print(operators_list) Creates the list of operators that needs to be operated

sign_list = []
for i in range(len(matched_ops)):
    sign_list.append(matched_ops[i][1])
#print(sign_list) Creates the sign of the number with which the operation must be performed

#In this block we concatenate the sign with the numbers, Note that these signs are not operators
for i in range(len(sign_list)):
    matched_num[i] = sign_list[i] + matched_num[i]
print(matched_num)

#This block will perform the operations with  * and / operators
index = 0
while index != len(operators_list):
    if len(operators_list) == 1: #If the user enters only 1 number to not perform any operation
        ans = matched_num[0]
    elif operators_list[index] == '*':
        ans = float(matched_num[index-1]) * float(matched_num[index])
        matched_num[index-1] = ans #replaces the number before operator by answer 
        matched_num.pop(index) #remove the number after the operator
        operators_list.remove('*') #remove the performed operator
        index -= 1
    elif operators_list[index] == '/':
        ans = float(matched_num[index-1]) / float(matched_num[index])
        matched_num[index-1] = ans
        matched_num.pop(index)
        operators_list.remove('/')
        index -= 1
    index +=1

#print(operators_list) #Removed all the * and / operators from the list
#print(matched_num) #Gives the numbers with operators + or -  

#This block will perform the final operations with + and - operators
if len(operators_list) == 1 and operators_list[0] == '+': #if all the operations have been performed and the only operator left at the front of the number will become its sign
    print(ans)
elif len(operators_list) == 1 and operators_list[0] == '-':
    print('-' + str(ans))
elif len(operators_list) > 1:
    answer = 0.0
    for val in range(0, len(matched_num)):
        if operators_list[val] == '+':
            answer = answer + float(matched_num[val])
        elif operators_list[val] == '-':
            answer = answer - float(matched_num[val])
    print("simpleMathCalculator's answer: ", answer)

print("Computer Calculator answer: ", eval(Equation)) #checks if the calculator's answer/ans is equal to actual answer.
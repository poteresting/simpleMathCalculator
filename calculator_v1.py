#Calculator that performs basic operations on entered equation (how eval() works)
import re

Equation = input('Enter an usolved equation (for example: - 1 + 2 - 3 * 4 / 5)\n')

Regnums = re.compile(r'\d+\.\d+|\d+') #Get the numbers here by pattern

Regop = re.compile(r'\+|-|\*|/') #Get the operators between numbers

matched_num = Regnums.findall(Equation)
print(matched_num) #prints the list of numbers in equation

matched_ops = Regop.findall(Equation)
print(matched_ops) #prints the list of operators in equation

if len(matched_ops) < len(matched_num): #adds an operator + to the first number if its positive
    matched_ops.insert(0, '+')

#This block will perform the operations with  * and / operators
index = 0
while index != len(matched_ops):
    if len(matched_num) == 1:
        ans = matched_num[0]
    elif matched_ops[index] == '*':
        ans = float(matched_num[index-1]) * float(matched_num[index])
        matched_num[index-1] = ans #replaces the number before operator by answer 
        matched_num.pop(index) #remove the number after the operator
        matched_ops.remove('*') #remove the performed operator
        index -= 1
    elif matched_ops[index] == '/':
        ans = float(matched_num[index-1]) / float(matched_num[index])
        matched_num[index-1] = ans
        matched_num.pop(index)
        matched_ops.remove('/')
        index -= 1
    index +=1

#print(matched_ops) #Removed all the * and / operators from the list
#print(matched_num) #Gives the numbers with operators + or -  

#This block will perform the final operations with + and - operators
if len(matched_ops) == 1:
    print(ans)
elif len(matched_ops) > 1:
    answer = 0.0
    for val in range(0, len(matched_num)):
        if matched_ops[val] == '+':
            answer = answer + float(matched_num[val])
        elif matched_ops[val] == '-':
            answer = answer - float(matched_num[val])
    print(answer)


print(eval(Equation))
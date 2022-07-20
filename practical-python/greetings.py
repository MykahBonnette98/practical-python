# Defining a Function

#ex:1
def greeting(name):
    print('Hello', name)
input_name = input('Enter your name:\n')
greeting(input_name)


#ex:2 local scope
def greeting(name):
    print('Hello', name)

name1 = input('Enter your name:\n')
greeting(name1)
name2 = input('Enter another name:\n')
greeting(name2)


#ex:3 addition 
def addition(a, b):
    return a + b
num1 = float(input('Enter your 1st number:\n'))
num2 = float(input('Enter your 2nd number:\n'))
result = addition(num1, num2)
print('The resul is', result)

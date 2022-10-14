# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# input
input_val = input()

# check
result = ""
if input_val != '6' and input_val != '7':
    result = "нет"
else:
    result = "да"

# output
print(result)

#Escreva um programa que resolva uma equação de segundo grau.  
# ax^2 + bx + c 
import math
a = float(input('Insira o valor de A da equação'))
b = float(input('Insira o vaBor de B da equação'))
c = float(input('Insira o valor de c da equação'))
delta = (b**2) - 4 * (a * c)
first_x = ((-1 * b) + (math.sqrt(delta)))/2 * a
print(math.sqrt(delta))
second_x = ((-1 * b) - (math.sqrt(delta)))/2 * a

print('X1 vale: ', first_x)
print('X2 vale: ', second_x)
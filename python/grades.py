#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   

first_grade = float(input('Insira a primeira nota: '))
second_grade = float(input('Insira a segunda nota: '))
average = (first_grade + second_grade)/2

if average >= 6:
    print('Parabéns, APROVADO (A)')
else:
    print('Sinto muito, REPROVADO(A)')
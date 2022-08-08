#1. Задайте натуральное число N. Напишите программу, 
#которая составит список простых множителей числа N.

def easyNumbers(n):
   i = 2
   easyNumber = []
   while i * i <= n:
       while n % i == 0:
           easyNumber.append(i)
           n = n / i
       i = i + 1
   if n > 1:
    n = int(n)
    easyNumber.append(n)
   return easyNumber

n = int(input('Введите число n: '))
answerOne = easyNumbers(n)
print(answerOne)

#2. Задайте последовательность чисел. 
#Напишите программу, которая выведет список 
#неповторяющихся элементов исходной последовательности.

answerTwo = []

for i in range(0, len(answerOne)):
    s = answerOne[i]
    if answerOne.count(s) < 2:
        answerTwo.append(s)
print(answerTwo)

#3. Задана натуральная степень k. 
#Сформировать случайным образом список 
#коэффициентов (значения от 0 до 100) многочлена 
#и записать в файл многочлен степени k.
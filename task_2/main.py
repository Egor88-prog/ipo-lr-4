number=input("Введите список чисел ").split() #создание списка
sqer_number=[pow(int(i),2) for i in number] #возведение чисел в квадрат
print("Cписок чисел в квадрате ",sqer_number)#Вывод нового списка
k = 0
while (True):
    quest1 = input('Какой язык мы изучаем? Ответ: ')
    if (quest1 == 'Python' or quest1 == 'python' or quest1 == 'PYTHON'):
        k +=1
        print ('Угадал!')
    elif:
        print ('Не угадал :(')
        
    quest2 = input('Как зовут преподавателя? Ответ: ')
    if (quest2 == 'Соболев Никита' or quest2 == 'Никита Соболев' or quest2 == 'соболев никита' or quest2 == 'никита соболев'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
    
    quest3 = input('Как пишется функция вывода? Ответ: ')
    if (quest3 == 'print()' or quest3 == 'print'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest4 = input('Как обозначается ложь в Python? Ответ: ')
    if (quest4 == 'False' or quest4 == 'false' or quest4 == '0'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest5 = input('Как обозначается истина в Python? Ответ: ')
    if (quest5 == 'True' or quest5 == 'true' or quest5 == '1'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest6 = input('Как обозначаются числа с плавающей точкой в Python? Ответ: ')
    if (quest6 == 'Float' or quest6 == 'float'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest7 = input('Как обозначаются целочисленные переменные в Python? Ответ: ')
    if (quest7 == 'Int' or quest7 == 'int'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest8 = input('Существует ли в Python конструкция if/else? Ответ: ')
    if (quest8 == 'Да' or quest8 == 'да'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest9 = input('Какая последняя версия Python на данный момент? Ответ: ')
    if (quest9 == '3' or quest9 == 'третья' or quest9 == 'три' or quest9 == 'Третья' or quest9 == 'Три'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    quest10 = input('Тебе понравилась первая пара по Python? Ответ: ')
    if (quest10 == 'Да' or quest10 == 'да'):
        k +=1
        print ('Угадал!')
    else:
        print ('Не угадал :(')
        
    Again = input("Повторить тест?")
    if(Again == 'да' or Again == 'Да'):
         continue
    elif (Again == 'Нет' or Again == 'нет'):
        print ('Количество праивльных ответов: ', k)
        print("Спасибо за пройденный тест!")
        break
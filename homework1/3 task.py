n = int(input("Введите число n = "))
list = []
for i in range(2, n+1):
    for j in list:
        if i % j == 0:
            break
    else:
        list.append(i)
print (list)
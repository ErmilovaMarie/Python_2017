def sort(list):
    for i in range(1, len(list)):
        last = list[i]
        k = i - 1
        while k >= 0:
            if list[k + 1] < list[k]:
                list[k + 1] = list[k]
                list[k] = last
                k = k - 1
            else:
                break
numb_list = [2,4,0,0,0,3,5,5,7,6]
sort(numb_list)
print(numb_list)

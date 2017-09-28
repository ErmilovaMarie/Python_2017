def selection_sort(array):
    a = array
    for i in range(len(a)):
        idxMin = i
        for j in range(i+1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a

arr = [0,2,0,1,2,8,5]
print(selection_sort(arr))
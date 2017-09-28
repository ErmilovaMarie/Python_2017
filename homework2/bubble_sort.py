numb_list = [4, 7, 8, 3, 0, 5, 1, 2, 9]
n = 1
while n < len(numb_list):
    for i in range(len(numb_list) - n):
	    if numb_list[i] > numb_list[i + 1]:
		    numb_list[i], numb_list[i + 1] = numb_list[i + 1], numb_list[i]
		    print(numb_list)
    n += 1		
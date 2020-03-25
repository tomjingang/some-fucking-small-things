

a = input()

alist = a.split(',')

alist = [list(alist[i]) for i in range(len(alist))]

print(alist)

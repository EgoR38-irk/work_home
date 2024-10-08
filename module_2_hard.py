n = int(input(f'Введите число от 3 до 20: '))
password=[]
for i in range(1,n):
    for j in range(1,n):
        if i >= j:
            continue
        else:
            b = n % (i + j)
        if b == 0:
            password.append([i, j])
            continue
print(f'{n} - {password}')


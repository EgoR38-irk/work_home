numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_primes = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        Primes.append(i)
    else:
        Not_primes.append(i)

print(f'Primes: {Primes}')
print(f'Not_primes: {Not_primes}')

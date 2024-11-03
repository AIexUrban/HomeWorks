numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(2, i):
        if numbers[i] % numbers[j - 1] == 0 or numbers[i] % 2 == 0:
            not_primes.append(numbers[i])
            break
    else:
        primes.append(numbers[i])

print(primes)
print(not_primes)
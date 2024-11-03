numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for i in range(1,len(numbers)): # объявляем цикл для перебора заданного списка
    if numbers[i] > 2 and numbers[i] % 2 == 0: # проверяем элемент списка на четность и >2
        not_primes.append(numbers[i]) # если нет, то элемент уходить в список к непростым
        continue
    j = numbers[i-1]
    for j in range(j,1,-1): # открываем цикл для перебора значений от эл-та меньшего на 1,
# в списке, назначенного во внешнем цикле, до второго эл-та в обратном порядке
        if numbers[i] % numbers[j-1] == 0:
            not_primes.append(numbers[i])
            break
    else:
        primes.append(numbers[i])

print(primes)
print(not_primes)
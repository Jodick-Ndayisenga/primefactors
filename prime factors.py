factors = []
number = int(input('Enter a number: '))
for i in range(1, number+1):
    if number % i != 0:
        pass
    else:
        factors.append(i)

print(factors)

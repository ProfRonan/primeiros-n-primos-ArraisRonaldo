def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Digite um número "))
count = 0
i = 2
while count < n:
    if is_prime(i):
        print(i)
        count += 1
    i += 1

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input("Введите трехзначное целое число: "))

a = n // 100
b = n % 100 // 10
c = n % 10

s = a + b + c
m = a * b * c

print(f"Сумма чисел равна {s}")
print(f"Произведение чисел равно {m}")
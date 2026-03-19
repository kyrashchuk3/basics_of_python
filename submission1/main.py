# Зчитування двох чисел
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Обчислення
sum_result = a + b
sub_result = a - b
mul_result = a * b

# Виведення результатів
print("Додавання:", sum_result)
print("Віднімання:", sub_result)
print("Множення:", mul_result)

if b != 0:
    div_result = a / b
    print("Ділення:", div_result)
else:
    print("Ділення: неможливе (ділення на нуль)")

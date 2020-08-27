''' Калькулятор '''
print("Вас приветствует калькулятор для произведения расчетов".upper())
a_1 = float(input("Введите первое число:"))
b_2 = input("Введите операцию: ")
c_3 = float(input("Введите второе число:"))
if b_2 == "/":
    if c_3 != 0:
        print((a_1) / (c_3))
    else:
        print("Деление на нуль не возможно")
elif b_2 == "+":
    print((a_1) + (c_3))
elif b_2 == "-":
    print((a_1) - (c_3))
elif b_2 == "*":
    print((a_1) * (c_3))
if b_2 == "mod":
    print((a_1) % (c_3))
if b_2 == "pow":
    print(a_1 ** c_3)
if b_2 == "div":
    print(a_1 // c_3)

mane = input("Введите ваше имя : ")
print("Здравствуйте " +mane+ " !")
print("\n\tБот РИТА приветствует Вас. Выберите машину,которая Вас заинтересовала: ".upper())
# Здесь я создал словарь. В который поместил марки машин
cars = {"1":"MAZDA",
        "2":"TESLA",
        "3":"BMW",
        "4":"LADA",}
# Затем вывел ключь и значение с помощью команды items()
for ca, car in cars.items():
    print(ca, car)
man = input("Введите цифру атомобиля,который вам приглянулся : ")
# После выведение словаря в терминале, я прировнял переменную cars с переменной man и тем самым
# прописал конструкцию if с значениями из списка cars
man == cars
if man == "1":
    print('Ваша заявка обрабатывается......ПИК.....ПИК...ВСЕ...Вашь автомобиль ' + cars["1"], " ждет вас на стоянке")
if man == "2":
    print('Ваша заявка обрабатывается......ПИК.....ПИК...ВСЕ...Вашь автомобиль ' + cars["2"], "ждет вас на стоянке")
if man == "3":
    print('Ваша заявка обрабатывается......ПИК.....ПИК...ВСЕ...Вашь автомобиль ' + cars["3"], " ждет вас на стоянке")
if man == "4":
    print('Ваша заявка обрабатывается......ПИК.....ПИК...ВСЕ...Вашь автомобиль ' + cars["4"], " ждет вас на стоянке")
# В этом блоке elif, я попробывал приравнять ее несовпадающиму значению в словаре cars.
# Т.е при выполнении команды input пользователь должен не вводить с компьютерв не какич символов.
elif man == "":
    print("Вы ничего не ввели".strip())
print('Бот РИТА Завершает свою работу. Покеда!!!')



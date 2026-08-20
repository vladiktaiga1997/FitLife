# Проект FitLife - MVP версия 1.0
print("-" * 40)
print("Добро пожаловать в FitLife.")
print("-" * 40)

# 1. Знакомство
user_name = input("как Вас зовут?")
user_age = int(input("сколько Вам лет?"))

# 2. Сбор данных
user_weight = float(input("укажите Ваш вес(в кг)"))
user_height = float(input("укажите Ваш Рост(в метрах(например, 1.75))"))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)
rounding_bmi = round(bmi, 1)


# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
# 30 - стандартная рекомендация для поддержания водного баланса
water_l = water_ml / 1000
rounding_water_l = round(water_l, 1)

# 4. Вывод красивого результата
print(f"Отчёт для пользователя: {user_name}  ({user_age} г.)")
print(f"Ваш индекс массы тела составляет: {rounding_bmi}")
print(f"Рекомендуемая норма воды: {rounding_water_l} литров воды в день.")
print("Расчёт окончен. Будьте здоровы!")

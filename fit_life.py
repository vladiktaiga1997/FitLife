# Проект FitLife - MVP версия 1.0
LINE_LENGTH = 40
STANDARD_RECOMMENDATION = 30
ML_IN_LITER = 1000
ROUNDING_DIGITS = 1

print("-" * LINE_LENGTH)
print("Добро пожаловать в FitLife.")
print("-" * LINE_LENGTH)

# 1. Знакомство
user_name = input("как Вас зовут?")
user_age = int(input("сколько Вам лет?"))

# 2. Сбор данных
user_weight = float(
    input("Укажите ваш вес в кг: ").replace(",", ".")
)
user_height = float(
    input(
        "Укажите ваш рост в метрах, например 1.75: "
    ).replace(",", ".")
)

# 3. Логика расчетов.
bmi = user_weight / (user_height ** 2)
rounding_bmi = round(bmi, ROUNDING_DIGITS)


# Подсчет воды.
water_ml = user_weight * STANDARD_RECOMMENDATION

water_l = water_ml / ML_IN_LITER
rounding_water_l = round(water_l, ROUNDING_DIGITS)

# 4. Вывод красивого результата.
print(
    f"Отчёт для пользователя: {user_name} ({user_age} г.) \n"
    f"Ваш индекс массы тела составляет: {rounding_bmi}\n"
    f"Рекомендуемая норма воды: {rounding_water_l} литра воды в день.\n"
    f"Расчёт окончен. Будьте здоровы!"
)

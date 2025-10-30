text = "   Python - отличный язык для начинающих! Python мощный.   "

# 1. Уберите лишние пробелы

# 2. Подсчитайте общее количество символов

# 3. Подсчитайте сколько раз встречается слово "Python"

# 4. Проверьте, начинается ли текст с "Python"

# 5. Переведите текст в нижний регистр

clean_text = text.strip()
total_chars = len(clean_text)
python_count = clean_text.count("Python")
starts_with_python = clean_text.startswith("Python")
lower_text = clean_text.lower()

print(f"Очищенный текст: '{clean_text}'")
print(f"Всего символов: {total_chars}")
print(f"Слов 'Python' найдено: {python_count}")
print(f"Начинается с 'Python': {starts_with_python}")
print(f"В нижнем регистре: {lower_text}")

user_data = "ivanov:Иван:Петров:25:Москва"

# 1. Разбейте строку по разделителю ":"
# 2. Извлеките отдельные данные

user_data = user_data.split(":")
username, first_name, last_name, age, city = (
    user_data[0],
    user_data[1],
    user_data[2],
    user_data[3],
    user_data[4],
)

print(f"Логин: {username}")
print(f"Имя: {first_name}")
print(f"Фамилия: {last_name}")
print(f"Возраст: {age}")
print(f"Город: {city}")

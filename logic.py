"""
Задачи на логические операции
"""

"""
Задача 1: Система авторизации для NLP-платформы

Контекст: Вы разрабатываете систему доступа к AI-моделям. Нужно проверить, может ли пользователь использовать модель

Инструкция: Заполните пропуски, используя логические операторы
"""
# Данные пользователя
user_role = "admin"
has_api_key = True
model_available = True
request_count_today = 95
daily_limit = 100

# ЗАДАНИЕ: Напишите условие доступа
# Пользователь имеет доступ если:
# - он администратор ИЛИ у него есть API-ключ
# - И модель доступна
# - И не превышен дневной лимит запросов

has_access = (
    (user_role == "admin" or has_api_key)
    and model_available
    and (request_count_today <= daily_limit)
)

print(f"Доступ есть: {has_access}")


"""
Задача 2: Валидатор текста для обработки

Контекст: Перед отправкой текста в NLP-модель нужно проверить его качество

Инструкция: Реализуйте проверки текста
"""

text = "Привет! Как дела?"
banned_words = ["мат", "оскорбление", "спам", "реклама"]

# ЗАДАНИЕ: Соберите финальную проверку
# Текст валиден если:
# - длина от 1 до 1000 символов
# - И не содержит запрещенных слов
# - И НЕ состоит только из английских символов

# Проверки (проверка мата и англоязычного текста написана, нужно реализовать логику)

text_lower = text.lower()
length_1_to_1000 = 1 <= len(text_lower) <= 1000
contains_banned_words = any(word in text_lower for word in banned_words)
is_english_only = all(ord(c) < 128 for c in text if c != " ")
is_valid = length_1_to_1000 and not contains_banned_words and not is_english_only

print(f"Текст валиден: {is_valid}")


"""
Задача 3: Система прав модератора

Контекст: Разрабатываем систему прав доступа для модерации контента

Инструкция: Определите права доступа
"""

# Данные пользователя и системы
user_permissions = ["read", "analyze", "moderate"]
content_categories = ["text", "image"]
current_content_type = "text"

# ЗАДАНИЕ: Определите возможности пользователя
# Может модерировать если:
# - есть права модератора И может обрабатывать текущий тип контента
# Может анализировать если:
# - есть права на анализ И доступен любой контент

can_moderate = (
    "moderate" in user_permissions and current_content_type in content_categories
)
can_analyze = (
    "analyze" in user_permissions
    and "text" in content_categories
    and "image" in content_categories
)

print(f"Доступ к модерации: {can_moderate}\nДоступ к анализу: {can_analyze}")


"""
Задача 4: Анализатор тональности отзывов

Контекст: Анализируем массив отзывов для выявления проблем

Инструкция: Проанализируйте тональность отзывов
"""

# Тональность отзывов от -1 (очень негативный) до +1 (очень позитивный)
reviews_sentiments = [0.8, 0.6, -0.3, 0.9, 0.7]

# ЗАДАНИЕ: Определите характеристики отзывов с помощью следующих проверок
# - Все отзывы позитивные: минимальное значение должно быть > 0
# - Есть хотя бы один негативный: минимальное значение должно быть < 0
# - Есть очень негативные отзывы: минимальное значение должно быть < -0.5
# - Большинство отзывов позитивные


# Здесь произведен расчет всех положительных отзывов
# Вам осталось произвести проверку: их сумма должна быть больше или равна
# максимально возможной оценке, которую можно получить по всем отзывам

positive_count = sum(1 for _ in filter(lambda x: x > 0, reviews_sentiments))

are_positive = min(reviews_sentiments) > 0
has_negative = min(reviews_sentiments) < 0
has_very_negative = min(reviews_sentiments) < -0.5
is_majority_positive = positive_count > len(reviews_sentiments) / 2

print(
    f"Все отзывы позитивные: {are_positive}\n"
    f"Есть хотя бы один негативный: {has_negative}\n"
    f"Есть очень негативные отзывы: {has_very_negative}\n"
    f"Большинство отзывов позитивные: {is_majority_positive}"
)


"""
Задача 5: Система подписок для NLP-сервиса

Контекст: Проверяем доступ к премиум-функциям AI-сервиса

Инструкция: Реализуйте проверку подписки
"""

# Данные пользователя и системы
user_tier = "premium"
subscription_active = True
available_models = ["gpt-3", "bert", "word2vec", "fasttext"]
premium_models = ["gpt-3", "bert", "gpt-4"]
user_quota = {"used": 45, "total": 100}

# ЗАДАНИЕ: Проверьте доступ к функциям
# Доступ к премиум-моделям если:
# - премиум-пользователь И активная подписка
# - И есть хотя бы одна премиум-модель
# - И не превышена квота
# Доступ к базовым функциям если:
# - есть любые модели И не превышена квота

# Эта проверка уже реализована. Напишите остальные и примените их
has_any_premium_model = any(model in available_models for model in premium_models)

access_to_premium = (
    user_tier == "premium"
    and subscription_active
    and has_any_premium_model
    and user_quota["used"] <= user_quota["total"]
)

access_to_basic = available_models and user_quota["used"] <= user_quota["total"]


print(
    f"Доступ к Premium: {access_to_premium}\n"
    f"Доступ к базовым функциям: {access_to_basic}"
)

"""Задача 2, слайд 20"""

api_response = {
    "text": "I really enjoyed the movie, the acting was amazing!",
    "sentiment": {"label": "positive", "score": 0.95, "confidence": "high"},
    "entities": [
        {"entity": "movie", "type": "ENTERTAINMENT", "confidence": 0.89},
        {"entity": "acting", "type": "SKILL", "confidence": 0.92},
    ],
    "language": "en",
    "processed_in": 0.45,
}

# 1: получаем оценку тональности (score) и выводим
print(f"SENTIMENT SCORE: {api_response["sentiment"]["score"]}\n")

# 2: проходим по сущностям, выводим только их названия
print(f"ENTITIES: {[entity["entity"] for entity in api_response["entities"]]}\n")

# 3: находим сущность с максимальной уверенностью (сonfidence), выводим,
# здесь считаю без lambda, в 4-ой задаче - через lambda
max_confidence_entity = api_response["entities"][0]

for entity in api_response["entities"]:
    max_confidence_entity = (
        entity
        if entity["confidence"] > max_confidence_entity["confidence"]
        else max_confidence_entity
    )

print(f"ENTITY WITH MAX CONFIDENCE: {max_confidence_entity}\n")

# 4: добавляем в поле ответа "model_version": "2.1.0"
# мне не совсем было понятно, что значит "поле ответа"
# в данном случае, я добавляю новую пару ключ-значение к api_response и ещё принтю его,
# после фильтрации в пункте 5 эти ключ и значение не будут учитываться, т.к. значение - str
api_response["model_version"] = "2.1.0"
print(f"MODEL VERSION: {api_response["model_version"]}\n")

# проверка, как выглядит api_response до фильтрации:
# print(api_response, "\n")

# 5: отфильтровываем все поля, значения которых - строки
filtered_api_response = {}
for key, value in api_response.items():
    if not isinstance(value, str):
        filtered_api_response[key] = value

# вывожу результат:
print(f"FILTERED RESPONSE: {filtered_api_response}")

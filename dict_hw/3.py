"""Задача 3, слайд 21"""

import copy

pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True},
    },
    "input_encoding": "utf-8",
    "output_format": "tokens",
}

# 1: включаем stemming, установив "enabled": True
pipeline_config["steps"]["stemming"]["enabled"] = True

# 2: добавляем "numbers" в custom_words для стоп-слов
pipeline_config["steps"]["stopwords"]["custom_words"].append("numbers")

# 3: получаем список всех включенных шагов пайплайна
enabled_steps = [
    step for step, setting in pipeline_config["steps"].items() 
    if setting["enabled"] == True
]

# 4: изменяем output_format на "vectors"
pipeline_config["output_format"] = "vectors"

# 5: создаём упрощенную конфигурацию только с включенными шагами,
# т.е. удаляем все НЕвключённые шаги, но правда в том, что
# в данном случае все шаги включены
pipeline_config_light = copy.deepcopy(pipeline_config)
for step in pipeline_config["steps"].keys():
    if step not in enabled_steps:
        del pipeline_config_light["steps"][step]

print(f"LIGHT PIPELINE CONFIG: {pipeline_config_light}")
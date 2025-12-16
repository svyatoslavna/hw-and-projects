"""Задача 4, слайд 23"""

models_stats = {
    "bert-base": {
        "accuracy": 0.92,
        "f1_score": 0.91,
        "inference_time": 120,
        "size_mb": 440,
    },
    "distilbert": {
        "accuracy": 0.89,
        "f1_score": 0.88,
        "inference_time": 65,
        "size_mb": 250,
    },
    "roberta-large": {
        "accuracy": 0.94,
        "f1_score": 0.93,
        "inference_time": 210,
        "size_mb": 1600,
    },
}

# 1: находим модель с максимальной точностью (accuracy),
# выводим её имя
max_accuracy_model_name, max_accuracy_model_stats = max(
    models_stats.items(), key=lambda x: x[1]["accuracy"]
)
print(f"THE MOST ACCURATE MODEL: {max_accuracy_model_name}\n")

# 2: рассчитываем среднее время инференса по всем моделям
all_inference_time = sum(
    stats["inference_time"] 
    for stats in models_stats.values()
    )
mean_inference_time = all_inference_time / len(models_stats)
print(f"MEAN INFERENCE TIME: {mean_inference_time:.2f}\n")

#3: создаём новый словарь только с метриками 
# accuracy и f1_score для каждой модели, 
# и получается, в данный список не попадает albert-base, 
# т.к. она будет добавлена в исходный список только на пятом шаге задачи
models_accuracy_f1 = {
    model: {"accuracy": stats["accuracy"], "f1_score": stats["f1_score"]}
    for model, stats in models_stats.items()
}
print(f"ACCURACY, F1-SCORE: {models_accuracy_f1}\n")

# 5: добавляем новую модель "albert-base" с данными: 
# accuracy=0.87, f1_score=0.86, inference_time=55, size_mb=180
models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180,
}

# 5: отфильтруем модели, размер которых меньше 500 МБ
filtered_models = {
    model: stats 
    for model, stats in models_stats.items() 
    if stats["size_mb"] >= 500
}
print(f"FILTERED MODELS STATS: {filtered_models}")

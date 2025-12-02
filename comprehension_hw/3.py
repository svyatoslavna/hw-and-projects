products = ["футболка", "кружка", "блокнот"]
colors = ["красный", "синий", "зеленый"]
combinations = [(product + " - " + color) for product in products for color in colors]

print(combinations)

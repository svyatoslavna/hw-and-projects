# 1
celsius = [0, 15, 25, 30, 40, 100]
fahrenheit = [(cel * 1.8 + 32) for cel in celsius]

print(fahrenheit)

# 2
grades = [45, 85, 92, 33, 67, 78, 90, 55, 29, 88]
passed = [grade for grade in grades if grade >= 60]

print(passed)

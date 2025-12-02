#1

numbers = [3, 7, 2, 9, 5]
print([num * 2 for num in numbers])

#2 
animals = ["cat", "elephant", "dog", "butterfly"]
print([animal for animal in animals if len(animal) > 3])

#3
fio = ("Иванов", "Иван", "Иванович")
print(*[name.lower() for name in fio])
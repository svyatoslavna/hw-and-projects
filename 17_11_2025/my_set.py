my_list = [0, 1, 2, 3]
my_list[2] = "two"
print(my_list)
print(type(my_list))
# 0, 1, two, 3

my_tuple = (0, 1, 2, 3)
my_tuple[2] = "two"  # ошибка!
print(type(my_tuple))

my_set = {0, 1, 2, 2, 3}
print(my_set)
# 0, 1, 2, 3
print(type(my_set))

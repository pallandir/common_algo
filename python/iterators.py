my_list = [1, 2, 3, 4, 5, 6]

iterator = iter(my_list)

while True:
    try:
        print(next(iterator))
    except StopIteration as e:
        break


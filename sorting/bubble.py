def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == "__main__":
    my_list = [3, 2, 6, 5, 7, 1, 8]
    print(f"before : {my_list}")
    bubble_sort(my_list)
    print(f"\nafter : {my_list}")
    print(my_list)

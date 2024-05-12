def insertion_sort(array):
    array_size = len(array)

    for array_index in range(array_size):
        smaller_item_index = array_index

        for current_index in range(array_index + 1, array_size):
            if array[current_index] < array[smaller_item_index]:
                smaller_item_index = current_index

        # at the end of each iteration, swap array's smaller_item_index with array's array_index
        array[array_index], array[smaller_item_index] = (
            array[smaller_item_index],
            array[array_index],
        )


if __name__ == "__main__":
    my_list = [3, 2, 6, 5, 7, 1, 8]
    print(f"before : {my_list}")
    insertion_sort(my_list)
    print(f"\nafter : {my_list}")

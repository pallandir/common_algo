# can you spot all the errors ?

def binary_search(
    array: list[int], left_cursor: int, right_cursor: int, element_to_find: int
):
    while left_cursor < right_cursor:
        middle = left_cursor + (left_cursor - right_cursor) // 2

        if array[middle] == element_to_find:
            return middle

        if array[middle] > element_to_find:
            left_cursor = middle + 1

        else:
            right_cursor = middle - 1

    return False


if __name__ == "__main__":
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 10, 14, 17]

    result = binary_search(numbers_list, numbers_list[0], len(numbers_list) - 1, 1)

    if result:
        print(f"item found at index : {result}")

    else:
        print("nothing found in this list")

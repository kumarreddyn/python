def merge_sort(data_list):
    print(data_list)
    if len(data_list) > 1:
        mid = len(data_list)//2
        left_array = data_list[:mid]
        right_array = data_list[mid:]
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                data_list[k] = left_array[i]
                i += 1
            else:
                data_list[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            data_list[k] = left_array[i]
            k = k+1
            i = i+1

        while j < len(right_array):
            data_list[k] = right_array[j]
            k = k+1
            j = j+1


# numbers = [75, 35, 63, 57, 21, 9, 46, 99, 17, 6]
numbers = [7, 5, 9]
merge_sort(numbers)
print(numbers)

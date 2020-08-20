def bubble_sort(data_list):
    for i in range(len(data_list)):
        # print('outer loop')
        has_change = False
        for j in range(len(data_list)):
            # print('inner loop')
            if data_list[i] > data_list[j]:
                has_change = True
                temp = data_list[i]
                data_list[i] = data_list[j]
                data_list[j] = temp
        if not has_change:
            break
        print(data_list)

    print(data_list)


# [42, 35, 35, 21, 15, 12, 10, 8]
# [10, 20, 30, 40, 50, 60]
numbers = [42, 35, 35, 21, 15, 12, 10, 8]
bubble_sort(numbers)



def selection_sort(data_list):
    for i in range(len(data_list)):
        min_index = i;
        for j in range(i+1, len(data_list)):
            if data_list[min_index] > data_list[j]:
                min_index = j;

        temp = data_list[i]
        data_list[i] = data_list[min_index]
        data_list[min_index] = temp
        print(data_list)


numbers = [75, 35, 63, 57, 21, 9, 46, 99, 17, 6]
selection_sort(numbers)

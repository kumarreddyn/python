def quick_sort(data, low, high):
    print(data)
    pi = partition(data, low, high)
    quick_sort(data, low, pi-1)
    quick_sort(data, pi+1, high)


def partition(data, low, high):
    print(data)
    pivot = data[high]
    i = low-1
    for j in (low, high-1):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i+1], data[high] = data[high], data[i+1]
    return i+1


data_list = [3, 7, 1, 32, 16, 50, 67, 45]
quick_sort(data_list, 0, len(data_list)-1)

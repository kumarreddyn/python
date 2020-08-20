def insertion_sort(numbers):
    print(numbers)
    if len(numbers) > 1:
        for i in range(1, len(numbers)):
            k = i
            while k > 0 and numbers[k] < numbers[k-1]:
                temp = numbers[k]
                numbers[k] = numbers[k-1]
                numbers[k-1] = temp
                k -= 1


data_list = [12, 11, 13, 5, 6]
insertion_sort(data_list)
print(data_list)

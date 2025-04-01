lis_unsorted = [2, 5, 83, 95, 22, 84, 18, 38, 96]


def selection_sort(list):
    result = []
    while list:
        smallest = list[0]
        for item in list:
            if item < smallest:
                smallest = item
        result.append(smallest)
        list.remove(smallest)
        print(result)
    list = result
    return list


def merge_sort(list):
    if len(list) == 1:
        return list
    else:
        middle = len(list) // 2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right[0])
            right = right[1:]
        else:
            result.append(left[0])
            left = left[1:]
    result.extend(left)
    result.extend(right)
    return result


print(merge_sort(lis_unsorted))


def binary_search(list, value):
    def limits(low, high):
        if low > high:
            return "Not found"
        middle = (low + high) // 2
        if value == list[middle]:
            return f"Found {value} at position {middle}"
        elif value > list[middle]:  # right side
            print('right', list[middle])
            return limits(middle + 1, high)
        else:  # left or equal
            print('left', list[middle])
            return limits(0, middle - 1)

    return limits(0, len(list))


print(binary_search(merge_sort(lis_unsorted), 5))

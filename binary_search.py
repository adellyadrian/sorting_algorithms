data = [10, 15, 22, 35, 42, 50, 61, 72, 84]

def binary_search(number, data, start, end):
    if start > end:
        return f'{number} was not found in the list'
    mid = (start + end) // 2
    if number == data[mid]:
        return f'Number {number} found at index {mid}'
    elif number > data[mid]:
        return binary_search(number, data, mid + 1, end)
    else:
        return binary_search(number, data, start, mid - 1)



print(binary_search(3, data, 0, len(data) - 1))
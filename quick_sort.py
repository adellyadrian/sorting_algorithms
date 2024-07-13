data = [3, 5, 2, 7, 6, 8, 1, 4]

def qs_easy(data):
    if len(data) < 2:
        return data
    pivot = data.pop()
    smaller, larger = [], []
    for item in data:
        if item < pivot:
            smaller.append(item)
        else:
            larger.append(item)
    return qs_easy(smaller) + [pivot] + qs_easy(larger)

def sort(data, l, r):
    pivotIndex = r
    pivotValue = data[r]
    data[l], data[pivotIndex] = data[pivotIndex], data[l]
    border = l
    for i in range(l, r + 1):
        if data[i] < pivotValue:
            border += 1
            data[border], data[i] = data[i], data[border]
    data[l], data[border] = data[border], data[l]
    return border

def qs_inplace(data, l, r):
    if l < r:
        border = sort(data, l, r)
        qs_inplace(data, l, border - 1)
        qs_inplace(data, border + 1, r)

def quick_sort(data):
    qs_inplace(data, 0, len(data) - 1)

quick_sort(data)
print(data)
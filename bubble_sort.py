def bubble_sort(list):
    copy = list.copy()

    for i in range(len(list), 1, -1):
        for j in range(i-1):
            print(copy)
            if copy[j+1] < copy[j]:
                copy[j], copy[j+1] = copy[j+1], copy[j]
    return copy


unordered = [5,3,8,1,7,9,6,4,2]

sorted = bubble_sort(unordered)

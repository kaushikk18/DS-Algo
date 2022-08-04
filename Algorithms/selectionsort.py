# selection sort -> sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning

def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i  # we are initially assuming the first index to be the minimum index

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

            # if the minimum index is not the same after looping, we swap the values of the i position with the new minimum value
            # that is the minimum value will be pushed to the starting in the first loop and the process continues
            if min_value != i:
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a


print(selection_sort([6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 6, 7, 8, 9, 7, 9, 0]))

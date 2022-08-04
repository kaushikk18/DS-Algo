# insertion sort ->  The array is virtually split into a sorted and an unsorted part.
# Values from the unsorted part are picked and placed at the correct position in the sorted part.
# the left array is sorted and the right array is unsorted
# initially the left array contains the first element and the right array contains elements from position two to the end

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1

    return list_a


print(insertion_sort([7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8]))

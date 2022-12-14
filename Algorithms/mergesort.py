def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merging
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if (left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i = i+1
            else:
                arr[k] = right_arr[j]
                j = j+1
            k = k+1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1


arr = [3, 34, 35, 521, 312, 47, 33, 579, 0, 2, 1]
merge_sort(arr)
print(arr)

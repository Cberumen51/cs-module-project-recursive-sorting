# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    left = right = 0
    while left <len(arrA) and right < len(arrB):
        if arrA[left] <=arrB[right]:
            merged_arr[left + right] = arrA[left]
            left += 1
        else:
            merged_arr[left + right] = arrB[right]
            right += 1
            
    for left in range(left, len(arrA)):
        merged_arr[left + right] = arrA[left]

    for right in range(right, len(arrB)):
        merged_arr[left + right] = arrB[right]


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        # Divide the array into two halves
        left = arr[:mid]
        right = arr[mid:]
        # Sort both halves
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        # Merge the two sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Copy remaining elements from left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # Copy remaining elements from right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Taking input from user
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

print("Original array:", arr)

merge_sort(arr)

print("Sorted array:", arr)

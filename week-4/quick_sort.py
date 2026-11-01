def quick_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Choose the first element as pivot
    pivot = arr[0]

    # Divide the array
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Recursive calls
    return quick_sort(left) + [pivot] + quick_sort(right)


# Main Program
n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

# Call Quick Sort
arr = quick_sort(arr)

print("Sorted Array:")
for element in arr:
    print(element, end=" ")

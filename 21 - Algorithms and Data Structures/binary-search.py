# binary-search


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 5]
target = 3
result = binary_search(arr, target)
print(result)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

# Output:
# 2
# Element 3 found at index 2

# Time complexity: O(log n)
# Space complexity: O(1)

# Binary search is a divide and conquer algorithm that works by repeatedly dividing the search space in half until the target element is found or the search space is empty.

# It is a very efficient algorithm for finding elements in a sorted array.

# ex4-Binary-Search.py
# Placeholder for Binary Search example


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print(binary_search(numbers, 7))

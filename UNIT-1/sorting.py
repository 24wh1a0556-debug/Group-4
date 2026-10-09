# sorting.py
# This file contains the implementations of Merge Sort and Quick Sort
# Written from scratch without using Python's built-in sort() or sorted()

# ─────────────────────────────────────────────
#  MERGE SORT
# ─────────────────────────────────────────────

def merge_sort(arr):
    """
    Merge Sort uses the Divide and Conquer strategy.
    1. Divide the array into two halves.
    2. Recursively sort each half.
    3. Merge the two sorted halves back together.

    Time Complexity:
        Best Case    : O(n log n)
        Average Case : O(n log n)
        Worst Case   : O(n log n)
    """

    # Base case: an array of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to split the array
    mid = len(arr) // 2

    # Recursively sort the left half
    left_half = merge_sort(arr[:mid])

    # Recursively sort the right half
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves and return
    return merge(left_half, right_half)


def merge(left, right):
    """
    Helper function to merge two sorted arrays into one sorted array.
    Compares elements one by one and places the smaller one first.
    """

    merged = []   # This will store the merged result
    i = 0         # Pointer for the left array
    j = 0         # Pointer for the right array

    # Compare elements from both arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If any elements remain in the left array, add them
    while i < len(left):
        merged.append(left[i])
        i += 1

    # If any elements remain in the right array, add them
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# ─────────────────────────────────────────────
#  QUICK SORT
# ─────────────────────────────────────────────

def quick_sort(arr):
    """
    Quick Sort also uses Divide and Conquer.
    1. Pick a pivot element (we use the last element).
    2. Partition the array: elements smaller than pivot go left,
       elements greater go right.
    3. Recursively sort the left and right partitions.

    Time Complexity:
        Best Case    : O(n log n)
        Average Case : O(n log n)
        Worst Case   : O(n²)  — happens when pivot is always smallest/largest
    """

    # Base case: array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot as the last element of the array
    pivot = arr[-1]

    # Elements smaller than or equal to the pivot
    left = [x for x in arr[:-1] if x <= pivot]

    # Elements greater than the pivot
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort left and right, then combine with pivot in the middle
    return quick_sort(left) + [pivot] + quick_sort(right)

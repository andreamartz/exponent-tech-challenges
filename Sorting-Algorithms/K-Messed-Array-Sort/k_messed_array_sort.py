# https://www.tryexponent.com/courses/software-engineering/swe-practice/k-messed-array-sort

# K-Messed Array Sort
# Save
# Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

# Analyze the time and space complexities of your solution.

# Example:

# input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# My assumptions / questions for the interviewer:
  # if the array is empty, return the empty array
  # if the array has only one element, return the array; no sorting is needed

# Plan:
  # More examples:
    # arr = [1, 4, 5, 3, 8, 7, 10, 9]

  # Edge cases:
    # arr is empty

  # Use insertion sort because the data is partially sorted. Insertion sort is adaptive, so runtime complexity can be as low as O(n) when the data is partially sorted.


def sort_k_messed_array(arr, k):
    # Handle edge cases and avoid index error if arr is empty
    if len(arr) <= 1:
        return arr

    # consider the first element arr[0] to be the sorted part of the array at the beginning. 
    # Loop over the array, each time adding the next element to the sorted part of the array in its correctly sorted position.
    for idx in range (1, len(arr)):
        curr = idx
        prev = idx - 1
        # is the next item sorted?
            # yes: continue to next iteration
            # no: move it left one position repeatedly until it is sorted

        while(arr[curr] < arr[prev]):
            [arr[idx - 1], arr[idx]] = [arr[idx], arr[idx - 1]]
            if curr - 1 >= 0:
                curr -= 1
            else:
                break
            if prev - 1 >= 0:
                prev -= 1
            else:
                break

    return arr

# TIME AND SPACE COMPLEXITY ANALYSIS

# Runtime complexity is O(n * k).
    # There are nested loops here.
        # The for loop has runtime complexity of O(n).
        # We know that the while loop will need to make at most 2 swaps PER ITERATION when k = 2, regardless of the length of arr. So the while loop is actually running in O(k) time with respect to the size of the input array, and there will be n iterations in the worst case.
        # O(n) for for loop and O(k) for the while loop => O(n * k)

# Space complexity is O(1), because we are sorting the array in place.

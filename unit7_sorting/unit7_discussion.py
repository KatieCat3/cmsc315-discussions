"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # create copy of the original list.
    sorted_list = lst.copy()

    # compare adjacent elements.
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:

                # swap elements when they are out of order.
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    # return sorted list.
    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <= 1:
        return lst

    # divide list into smaller halves.
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    # sort each half recursively.
    left = merge_sort(left)
    right = merge_sort(right)

    # merge sorted halves together and return sorted list.
    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    # compare values from left and right lists.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # append any remaining values.
    result.extend(left[left_index:])

    result.extend(right[right_index:])

    # return merged sorted list.
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    dataset1 = [5, 2, 7, 1, 6, 3, 4]

    print("Original list: ", dataset1)
    print("Bubble sort: ", bubble_sort(dataset1))
    print("Merge sort: ", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.



    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    dataset2 = [10, 8, 12, 9, 14, 11, 13]

    print("Original list: ", dataset2)
    print("Bubble sort: ", bubble_sort(dataset2))
    print("Merge sort: ", merge_sort(dataset2))

    # compare results
    print("Both algorithms produced the same result: ", bubble_sort(dataset2) == merge_sort(dataset2))



# ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Empty list.
    empty_list = []

    print("Empty list: ", empty_list)
    print("Bubble sort: ", bubble_sort(empty_list))
    print("Merge sort: ", merge_sort(empty_list))
    print("The empty list stays empty because there are no values to sort.")

    # Already sorted list.
    sorted_list = [1, 2, 3, 4, 5]

    print("Already sorted list: ", sorted_list)
    print("Bubble sort: ", bubble_sort(sorted_list))
    print("Merge sort: ", merge_sort(sorted_list))
    print("The list stays the same because it is already sorted.")




if __name__ == "__main__":
    main()
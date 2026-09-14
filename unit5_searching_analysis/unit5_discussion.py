"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each value in the list from beginning to end.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Linear search has O(n) time complexity because it might need to check every value in the list before finding the target.
    return -1



def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Start with first and last indexes of the list.
    low = 0
    high = len(lst) - 1

    while low <= high:
        # Find the middle index of the current search area.
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # Remove the lower half from the search.
            low = mid + 1
        else:
            # Remove the upper half from the search.
            high = mid - 1
    return -1



def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Small sorted dataset.
    small_dataset = [10, 20, 30, 40, 50]

    # Search for value that exists.
    target = 30
    print("Linear search for 30: ", linear_search(small_dataset, target))
    print("Binary search for 30: ", binary_search(small_dataset, target))

    # Search for value that does not exist.
    target = 60
    print("Linear search for 60: ", linear_search(small_dataset, target))
    print("Binary search for 60: ", binary_search(small_dataset, target))

    # Returns the index when value is found and -1 when value is not found.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Large dataset
    large_dataset = list(range(1, 101))

    # Search for value
    target = 99
    print("Linear search for 99: ", linear_search(large_dataset, target))
    print("Binary search for 99: ", binary_search(large_dataset, target))

    # Linear search might need to check many values one at a time.
    # Binary search reduces search space by half with each iteration making it more efficient as it grows larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1 - empty list
    empty_list = []
    print("Linear search empty list: ", linear_search(empty_list, 10))
    print("Binary search empty list: ", binary_search(empty_list, 10))
    # No values to search so both searches return -1

    # Edge case 2 - single-element list
    single_element = [10]
    print("Linear search single-element list: ", linear_search(single_element, 10))
    print("Binary search single-element list: ", binary_search(single_element, 10))
    # Value exists at index 0 so both searches return 0.

    # Real world search scenario
    # A sorted list of book library book titles.
    book_titles = [
        "Of Mice and Men",
        "Pride and Prejudice",
        "The Rules of Magic",
        "The Woman in the Window"
    ]

    # Search for a book that exists in the list.
    target_book = "The Rules of Magic"

    print("Linear search for book: ",
          linear_search(book_titles, target_book))
    print("Binary search for book: ",
          binary_search(book_titles, target_book))
    # Both searches return the book index. Binary search can search a large sorted collection more efficiently.


if __name__ == "__main__":
    main()
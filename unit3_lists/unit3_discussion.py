"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # insert() adds the value at the index.
    # existing elements at or after the index shift one place to the right.
    # inserting near the beginning may require more elements to shift.
    # inserting near the end requires fewer elements to shift.

    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    pass

    # index validation is important because it prevents the program from attempting to delete an item at a position that does not exist.
    # safely returning none for an invalid index prevents an index error and allows the program to continue running.


    if index < 0 or index >= len(lst):
        return None

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    pass
    # this is a linear search because the list is searches sequentially
    # each element is checked one at a time from the beginning until the value is found

    for index in range(len(lst)):
        if lst[index] == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # create a list containting several starting values and display original list
    num_list = [10, 20, 30, 40]
    print("Original list: ", num_list)

    # insert 5 to the beginning of the list.
    insert_at(num_list, 0, 5)
    print("After inserting 5 at the beginning: ", num_list)

    # insert 25 into the middle of the list.
    insert_at(num_list, 3, 25)
    print("After inserting 25 in the middle: ", num_list)

    # insert 50 at the end of the list.
    insert_at(num_list, len(num_list), 50)
    print("After inserting 50 at the end: ", num_list)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # remove first item in the list.
    removed_value = delete_at(num_list, 0)
    print("Removed from the beginning: ", removed_value)
    print("List after deleting the beginning: ", num_list)

    # remove the middle item in the list.
    middle_index = len(num_list) // 2
    removed_value = delete_at(num_list, middle_index)
    print("Removed from the middle: ", removed_value)
    print("List after deleting the middle item: ", num_list)

    # remove the end item in the list.
    removed_value = delete_at(num_list, len(num_list) -1)
    print("Removed from the end: ", removed_value)
    print("List after deleting the end item: ", num_list)


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # search for 20 which exists in the list.
    search_result = search_value(num_list, 20)
    print("Search for 20 returned: ", search_result)

    # search for 100 which is a value that does not exist.
    # returns -1 when the value cannot be found.
    search_result = search_value(num_list, 100)
    print("Search for 100 returned: ", search_result)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Edge case 1: Delete using an invalid index.
    # This function safely returns none instead of causing an index error.
    invalid_delete = delete_at(num_list, 100)
    print("Delete using invalid index returned: ", invalid_delete)

    # Edge case 2: Insert into an empty list.
    # The inserted value becomes the first item in the list.
    empty_list = []
    print("Empty list before insertion: ", empty_list)
    insert_at(empty_list, 0, 75)
    print("Empty list after inserting 75: ", empty_list)



if __name__ == "__main__":
    main()
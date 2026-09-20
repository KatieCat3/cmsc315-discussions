"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Empty dictionary that will store students names and grades.
    student_grades = {}

    # Dictionary behaves like a hash table by storing information as key-value pairs.
    student_grades["Ben"] = 95
    student_grades["Tyler"] = 90
    student_grades["Daniel"] = 85
    student_grades["Stewart"] = 80
    student_grades["Luke"] = 75

    # Display contents of the dictionary.
    print("Student grade hash table: ", student_grades)


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Look up student grades using their name as keys.
    print("Ben's grade: ", student_grades["Ben"])
    print("Luke's grade: ", student_grades["Luke"])

    print("TODO: Demonstrate successful key lookups.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    # Display dictionary before updating the grade.
    print("Before update: ", student_grades)

    # Assign new value to an existing key will replace the old value.
    student_grades["Daniel"] = 88

    # Display dictionary after updating the grade.
    print("After update: ", student_grades)

    print("TODO: Demonstrate updating an existing key.")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    # Display the dictionary before deleting the student.
    print("Before deletion: ", student_grades)

    # Delete a key-value pair from the dictionary.
    del student_grades["Stewart"]

    # Display the dictionary after deleting the student.
    print("After deletion: ", student_grades)

    print("TODO: Demonstrate deleting a key-value pair.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Look up a student who is not in the dictionary.
    missing_grade = student_grades.get("Matt")
    print("Grade for missing student: ", missing_grade)

    # Check if student exists.
    if "John" in student_grades:
        del student_grades["John"]
    else:
        print("John was not found and cannot be deleted.")

    print("TODO: Demonstrate and explain edge cases.")



if __name__ == "__main__":
    main()
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The root might change when inserting into an empty tree so the returned node is assigned back to self.root.
        self.root = self._insert_recursive(self.root, value)


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Null position meaning the correct insertion point was found.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored.
        return node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST can reduce the search space at each step because smaller values are stored on the left and larger values on the right.
        return self._search_recursive(self.root, value)


    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If search reaches an empty position the value is not present.
        if node is None:
            return False

        # If the value was found at the current node.
        if value == node.value:
            return True

        # Search the side of the tree where the value could exist.
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values


    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        # Visiting the left, current, and right produces sorted output because smaller values are stored on the left and larger values on the right.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")


    tree = BST()
    inserted_values = [2, 1, 4, 3, 6, 5, 7]

    for value in inserted_values:
        tree.insert(value)

    # BST reduces the possible search area after each comparison because values smaller than a node are on the left and larger values are on the right.
    print("Values inserted: ", inserted_values)

    # ===============================

    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")
    # In-order traversal visits the left subtree, current node, and right subtree so the values appear in sorted order.
    traversal_result = tree.inorder()
    print("In-order traversal: ", traversal_result)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # The values exist in the tree so the search should return True.
    print("Search for 3: ", tree.search(3))
    print("Search for 6: ", tree.search(6))

    # The values were never inserted so the search should return False.
    print("Search for 8: ", tree.search(8))
    print("Search for 10: ", tree.search(10))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")


    # Searching an empty tree should return False because there are no nodes to search.
    empty_tree = BST()
    print("Search empty tree for 2: ", empty_tree.search(2))

    # Traversing an empty tree returns an empty list.
    print("Empty tree traversal: ", empty_tree.inorder())



if __name__ == "__main__":
    main()
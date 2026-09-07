# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

- I stored the node's value and initialized references to the left and right child nodes.
- I initiated an empty Binary Search Tree.
- I inserted a value into the BST and used the recursive helper method. 
- I implemented recursive BST insertion.
- I created a new node when a position was found.
- I inserted smaller values into the left subtree and larger values into the right subtree.
- I returned the updated node reference.
- I searched for a value in the BST.
- I implemented recursive BST search.
- I returned a list containing the values from an in-order traversal.
- I implemented an in-order traversal.
- I built a tree.
- I created a BST and inserted multiple values.
- I displayed traversal results.
- I demonstrated BST searching.
- I demonstrated an edge case.

    While completing this assignment, I learned how to build a BST and use recursive tree operations. I learned how to insert values recursively by
placing smaller values in the left subtree and larger values in the right subtree. I also learned how to search recursively and perform an in-order
traversal. The in-order traversal visits the left subtree, current node, and right subtree, which puts the values in sorted order.
    One challenge I encountered was understanding how the order that values are inserted changes the structure of the tree. I overcame this by using
the values 2, 1, 4, 3, 6, 5, 7 and reviewing where each value was placed. I also tested an empty tree to demonstrate an edge case. Searching the 
empty tree returned false, and traversing it returned an empty list.
    A BST can make searching more efficient because it reduces the possible search area at each step. Other data structures may need to check each
value to find the one being searched for. A BST can instead use whether a value is smaller or larger than the current node to decide which side of the
tree to search.
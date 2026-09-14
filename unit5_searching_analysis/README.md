# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

While completing this assignment, I learned how to implement linear search and binary search algorithms. I learned that linear search checks each value
in a list from beginning to end. Linear search has O(n) time complexity because it might need to check every value in the list before finding the target.
I learned that binary search repeatedly reduces the search space by half, making it more efficient as datasets grow larger. 

One challenge I encountered was during the real-world search scenario using book titles. Linear search found the book, but binary search returned -1 even
though the book was in the list. I realized that the list of book titles was not sorted correctly. I overcame this by putting the book titles in
alphabetical order. 

Linear search is useful when a list is not sorted or when searching a smaller dataset. Binary search is more efficient for a large sorted dataset because
it reduces the search space by half with each iteration. However, binary search requires the list to already be sorted before it can be used.






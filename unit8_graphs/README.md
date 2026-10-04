# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

While completing this assignment, I learned how graphs can be represented using an adjacency lists and how BFS can be used to move through a graph. I also learned how a queue is used to keep track of which node should be visited and how a 
visited set prevents the same node from being visited more than once. BFS also helped me understand how nodes are visited level by level based on their connections.
One challenge I encountered was understanding how the queue manages the traversal order. I overcame this by going through the BFS traversal and seeing how the neighbors are added to the queue and visited level by level. 
BFS visits nearby nodes first and moves through the graph level by level while DFS follows one path deeper before moving to another path. In my classroom graph, BFS could be used to visit the classrooms with direct hallway connections first
before moving farther away. DFS could be used when following one hallway path through the classrooms before going back and following another path.
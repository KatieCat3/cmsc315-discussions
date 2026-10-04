"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # use a queue to manage the traversal order
    # a queue is used to allow BFS to visit nodes in the order they are discovered.
    queue = deque([start])

    # track visited nodes to prevent revisiting nodes.
    visited = set()

    # store order the nodes are visited in.
    traversal_order = []

    while queue:

        # remove first node
        node = queue.popleft()

        if node not in visited:
            # mark node as visited
            visited.add(node)
            traversal_order.append(node)

            # neighbors are added to the queue so they are visited level by level.
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    # BFS visits nearby nodes first, while DFS follows one path deeper first.
    return traversal_order



def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # create a graph of classrooms in a school using an adjacency list.
    # nodes represent classrooms and edges represent a direct hallway connection.
    graph = {
        "Classroom 6": ["Classroom 7", "Classroom 8"],
        "Classroom 7": ["Classroom 6", "Classroom 9"],
        "Classroom 8": ["Classroom 6", "Classroom 10"],
        "Classroom 9": ["Classroom 7", "Classroom 11"],
        "Classroom 10": ["Classroom 8", "Classroom 11"],
        "Classroom 11": ["Classroom 9", "Classroom 10"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")
    # clearly display the classrooms and their connections
    for classroom, connections in graph.items():
        print(classroom, "->", connections)




    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    # select classroom 6
    start = "Classroom 6"

    # perform BFS starting at classroom 6.
    # BFS visits directly connected classrooms before moving to the next level.
    traversal = bfs(graph, start)

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # display traversal order of classrooms visited.
    print("Starting classroom:", start)
    print("BFS traversal order:", traversal)

    # add classroom 12 and connect it to classroom 11.
    graph["Classroom 12"] = ["Classroom 11"]
    graph["Classroom 11"].append("Classroom 12")

    # perform BFS again after adding the new classroom
    updated_traversal = bfs(graph, start)

    print(" Updated BFS Traversal ")
    print("Added Classroom 12 connected to Classroom 11.")
    print("Updated BFS traversal order:", updated_traversal)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1 - start from a different classroom
    # BFS will begin at classroom 9 instead of classroom 6.
    different_start = bfs(graph, "Classroom 9")
    print("BFS starting from Classroom 9:", different_start)

    # Edge case 2 - use a disconnected graph
    # classroom 13 has no connections so BFS can only visit classroom 13
    disconnected_graph = {
        "Classroom 6": ["Classroom 7"],
        "Classroom 7": ["Classroom 6"],
        "Classroom 13": []
    }
    disconnected_traversal = bfs(disconnected_graph, "Classroom 13")
    print("BFS with disconnected Classroom 13:", disconnected_traversal)




if __name__ == "__main__":
    main()
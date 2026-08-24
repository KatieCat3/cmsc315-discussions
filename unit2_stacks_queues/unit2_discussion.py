"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # create empty list
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # This operation supports LIFO behavior because the newest value will be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # It should return a message that the "stack is empty" and should not try and remove a value if the stack is empty.
        if self.is_empty():
            return "Stack is empty."

        # Remove and return the most recent value.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the top value without removing the stack.
        if self.is_empty():
            return "Stack is empty."

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # This operation supports FIFO behavior because the older values stay at the front and are removed before newer values.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # if self.is_empty() will return the message "Queue is empty."
        if self.is_empty():
            return "Queue is empty."
        # Removes and returns value from front of queue
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # The front returns the oldest value.
        if self.is_empty():
            return "Queue is empty."

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(slef.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== Library Book Return ===")

# Stack for returned library books.
book_stack = Stack()

# 4 returned books to the stack.
book_stack.push("Pride and Prejudice")
book_stack.push("The Rules of Magic")
book_stack.push("The Woman in the Window")
book_stack.push("Harry Potter")

print("TODO: Create Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

# Improved print statements.
print("Library books are added to the stack as they are returned.")
print("      The last book returned is the first book removed.")
print("      This demonstrates LIFO behavior.")
print("      Empty and single-item stack cases will also be tested.")

# Last book added is the first book removed.
print("\nDemonstrating LIFO behavior: ")
print("Removed: ", book_stack.pop())
print("Removed: ", book_stack.pop())
print("Removed: ", book_stack.pop())
print("Removed: ", book_stack.pop())

# Test popping from an empty stack.
print("\nTesting pop from an empty stack: ")
print(book_stack.pop())

# Test peeking at an empty stack.
print("\nTesting peek from an empty stack: ")
print(book_stack.peek())

# Create a single-item stack.
single_book_stack = Stack()
single_book_stack.push("Lord of the Rings")

# Remove item and verify the stack is empty.
print("\nTesting a single-item stack: ")
print("Removed: ", single_book_stack.pop())
print("Is the stack empty?", single_book_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== Library Checkout Line ===")

# Queue for customers waiting in line at the library checkout.
checkout_queue = Queue()

# 4 customers in checkout line.
checkout_queue.enqueue("Customer 1")
checkout_queue.enqueue("Customer 2")
checkout_queue.enqueue("Customer 3")
checkout_queue.enqueue("Customer 4")

print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

# Improved print statements.
print("Library checkout line demonstrates FIFO behavior,")
print("      testing dequeue from an empty queue,")
print("      testing front on an empty queue,")
print("      and verifying a single-item queue is empty after removal.")

# Demonstrate FIFO behavior.
print("\nDemonstrating FIFO behavior: ")
print("Checked out: ", checkout_queue.dequeue())
print("Checked out: ", checkout_queue.dequeue())
print("Checked out: ", checkout_queue.dequeue())
print("Checked out: ", checkout_queue.dequeue())

# Test dequeue from an empty queue.
print("\nTesting dequeue from an empty queue: ")
print(checkout_queue.dequeue())

# Test viewing the front of an empty queue.
print("\nTesting front on an empty queue: ")
print(checkout_queue.front())

# Create a queue with only one customer.
single_customer_queue = Queue()
single_customer_queue.enqueue("Customer 5")

# Remove the customer and verify the queue is empty.
print("\nTesting a single-item queue: ")
print("Checked out: ", single_customer_queue.dequeue())
print("Is the queue empty?", single_customer_queue.is_empty())


if __name__ == "__main__":
    main()

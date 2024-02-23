from collections import deque
from python_queue import LifoQueue
# Python program to
# demonstrate stack implementation
# using list
stack = []

# append() function to push
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack')
print(stack)
# pop() function to pop
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print('\nStack after elements are popped:')
print(stack)

# Python program to
# demonstrate stack implementation
# using collections.deque

stack = deque()
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
print('Initial stack:')
print(stack)
# pop() function to pop
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)


# Initializing a stack
stack = LifoQueue(maxsize=3)
# qsize() show the number of elements
print(stack.qsize())
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
print("Full: ", stack.full())
print("Size: ", stack.qsize())
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())


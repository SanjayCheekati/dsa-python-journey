# Stack implementation using List
stack = []

stack.append(2)      # Push 2
stack.append(3)      # Push 3
stack.append(5)      # Push 5
print(stack)         # Current stack: [2, 3, 5]

print(stack[-1])     # Peek: returns top element (5)

stack.pop()          # Pop: removes top element (5)
print(stack)         # Stack after pop: [2, 3]

from collections import deque

# Regular Queue implementation (FIFO)
print("Regular Queue:")
queue = deque()

queue.append(1)      # Enqueue at rear
queue.append(2)
queue.append(3)
print(queue)          # deque([1, 2, 3])

queue.popleft()       # Dequeue from front
print(queue)          # deque([2, 3])

# Double-Ended Queue implementation
print("\nDouble-Ended Queue:")
dq = deque()

dq.append(1)          # Add to right
dq.appendleft(2)      # Add to left
dq.append(3)
dq.appendleft(4)
print(dq)             # deque([4, 2, 1, 3])

dq.pop()              # Remove from right
dq.popleft()          # Remove from left
print(dq)             # deque([2, 1])

print(dq[0]) #peek front
print(dq[-1]) #peek rear
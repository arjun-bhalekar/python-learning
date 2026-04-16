from collections import deque

queue = deque([1,2,3,4,5])

print(queue)
# pop element
print(queue.pop())
print(queue.popleft())

print(queue)
# add element
queue.append(6)
print(queue)
queue.appendleft(7)
print(queue)


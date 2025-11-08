from collections import deque
list = deque()
list.append(1)
list.append(5)
list.append(3)

print(f'the element poped {list.popleft()}')
print(list)

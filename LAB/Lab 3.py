
from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Target reached")
            return

        moves = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),
            (x + min(y, cap1 - x), y - min(y, cap1 - x))
        ]

        for state in moves:
            if state not in visited:
                queue.append(state)

    print("Solution not possible")

water_jug(4, 3, 2)

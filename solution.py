from collections import deque

n = int(input())

grid = []
brick_type = []
brick_id = 0

for i in range(n):
    line = input()

    row = []
    types = []

    j = 0

    while j < len(line):

        num = 0

        while j < len(line) and line[j].isdigit():
            num = num * 10 + int(line[j])
            j += 1

        ch = line[j]
        j += 1

        brick_id += 1

        for k in range(num):
            row.append(brick_id)
            types.append(ch)

    grid.append(row)
    brick_type.append(types)


# Find source and destination
start = 0
end = 0

for i in range(n):
    for j in range(n):

        if brick_type[i][j] == 'S':
            start = grid[i][j]

        if brick_type[i][j] == 'D':
            end = grid[i][j]


# Find which bricks are connected
graph = {}

for i in range(n):
    for j in range(n):

        current = grid[i][j]

        if current not in graph:
            graph[current] = set()

        # Down
        if i + 1 < n:
            other = grid[i + 1][j]

            if current != other:
                graph[current].add(other)
                graph.setdefault(other, set()).add(current)

        # Right
        if j + 1 < n:
            other = grid[i][j + 1]

            if current != other:
                graph[current].add(other)
                graph.setdefault(other, set()).add(current)


# 0-1 BFS
distance = {}

for brick in graph:
    distance[brick] = 999999

distance[start] = 0

queue = deque()
queue.append(start)

while queue:

    current = queue.popleft()

    for next_brick in graph[current]:

        if next_brick == end:
            cost = 0

        elif brick_type[
            next(
                i for i in range(n)
                if next_brick in grid[i]
            )
        ][grid[
            next(
                i for i in range(n)
                if next_brick in grid[i]
            )
        ].index(next_brick)] == 'R':
            continue

        else:
            cost = 1

        new_cost = distance[current] + cost

        if new_cost < distance[next_brick]:

            distance[next_brick] = new_cost

            if cost == 0:
                queue.appendleft(next_brick)
            else:
                queue.append(next_brick)


print(distance[end])

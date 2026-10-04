from heapq import heappush, heappop

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def greedy(start):
    visited = set()
    pq = []
    heappush(pq, (heuristic(start), start))

    while pq:
        h, state = heappop(pq)
        key = str(state)
        if key in visited:
            continue

        visited.add(key)
        print("Heuristic =", h)
        for row in state:
            print(row)
        print()

        if state == goal:
            print("Goal Reached!")
            return

        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                heappush(pq, (heuristic(neighbor), neighbor))

start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

greedy(start)

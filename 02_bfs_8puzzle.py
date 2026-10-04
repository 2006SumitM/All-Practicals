from collections import deque

def print_puzzle(state):
    for row in state:
        print(row)
    print()

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_moves(state):
    moves = []
    x, y = find_zero(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)

    return moves

def bfs(start, goal):
    queue = deque()
    visited = []

    queue.append((start, []))
    visited.append(start)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal:
            return path + [current_state]

        for move in generate_moves(current_state):
            if move not in visited:
                visited.append(move)
                queue.append((move, path + [current_state]))

    return None

start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = bfs(start, goal)

print("Solution Path:\n")
for step in solution:
    print_puzzle(step)

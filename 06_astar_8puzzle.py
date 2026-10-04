from heapq import heappush, heappop

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x = (value - 1) // 3
                y = (value - 1) % 3
                h += abs(i - x) + abs(j - y)
    return h

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_blank(state)
    moves = [(1,0),(0,1),(0,-1),(-1,0)]
    result = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)

    return result

def astar(start):
    pq = []
    visited = set()

    g = 0
    h = heuristic(start)
    f = g + h

    heappush(pq, (f, g, start))

    while pq:
        f, g, state = heappop(pq)

        if str(state) in visited:
            continue

        visited.add(str(state))

        print("g =", g, ", h =", heuristic(state), ", f =", f)
        for row in state:
            print(row)
        print()

        if state == goal:
            print("Goal Reached!")
            return

        for next_state in neighbors(state):
            if str(next_state) not in visited:
                new_g = g + 1
                new_h = heuristic(next_state)
                new_f = new_g + new_h
                heappush(pq, (new_f, new_g, next_state))

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

astar(start)

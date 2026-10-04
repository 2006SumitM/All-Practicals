# jug1 = 4
# jug2 = 3
# target = 2

# visited = set()

# def dfs(x, y):
#     if (x, y) in visited:
#         return False

#     print((x, y))
#     visited.add((x, y))

#     if x == target or y == target:
#         print("Target reached!")
#         return True

#     return (
#         dfs(jug1, y) or 
#         dfs(x, jug2) or 
#         dfs(0, y) or  
#         dfs(x, 0) or 
#         dfs(x - min(x, jug2-y), y + min(x, jug2-y)) or
#         dfs(x + min(y, jug1-x), y - min(y, jug1-x))
#     )

# dfs(0, 0)
























jug1 = 4
jug2 = 3
target = 2

visited = set()

def dfs(x,y):
    if (x,y) in visited:
        return False
    print (x,y)
    visited.add((x,y))

    if x == target or y == target:
        print("target reached")
        return True

    pour1 = min(x,jug2-y)
    pour2 = min(y,jug1-x)

    return(
        dfs(jug1,y)or
        dfs(x,jug2)or
        dfs(0,y)or
        dfs(x,0)or
        dfs(x-pour1,y+pour1)or
        dfs(x+pour2,y-pour2)
    )

dfs(0,0)
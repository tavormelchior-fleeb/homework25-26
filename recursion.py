# add and mult are only used for factorial, so we won't negative number proof it
def add(x, y):
    if y == 0:
        return x
    else:
        return 1 + add(x, y-1)


def mult(x, y):
    if y == 1:
        return x
    else:
        return add(x, mult(x, y-1))


def factorial(x):
    if x < 0:
        print("factorial must be of non negative number")
        raise ValueError
    if x == 0:
        return 1
    else:
        return mult(x, factorial(x-1))


def maze_solve(maze):
    rows, cols = len(maze), len(maze[0])

    if maze[0][0] == 0 or maze[rows - 1][cols - 1] == 0:
        return False, []

    visited = [[False] * cols for i in range(rows)]
    path = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if (r, c) == (rows - 1, cols - 1):
            path.append((r, c))
            return True

        visited[r][c] = True
        path.append((r, c))

        for change_in_r, change_in_c in directions:
            new_r, new_c = r + change_in_r, c + change_in_c
            # make sure to stay in maze
            if 0 <= new_r < rows and 0 <= new_c < cols:
                # check valid step (no wall)
                if maze[new_r][new_c] == 1 and not visited[new_r][new_c]:
                    # recursive call
                    if dfs(new_r, new_c):
                        return True
        # reset if failed, to last good position
        path.pop()
        return False

    # run dfs on maze
    solvable = dfs(0, 0)
    return solvable, path if solvable else []


print(factorial(7))

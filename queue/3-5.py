inp = input("Enter width, height, and room: ").split(' ')

width = int(inp[0])
height = int(inp[1])

grid = []

if len(inp) > 2:
    map_row = inp[2].split(',')
    for i in map_row:
        grid.append(list(i))

start_pos = None
exit_pos = None

if len(grid) != height:
    print("Invalid map input.")
    exit()

for i in grid:
    if len(i) != width:
        print("Invalid map input.")
        exit()

for row_idx in range(height):
    for col_idx in range(width):
        if grid[row_idx][col_idx] == 'F':
            start_pos = (row_idx, col_idx)
        elif grid[row_idx][col_idx] == 'O':
            exit_pos = (row_idx, col_idx)

if start_pos is None:
    print("Invalid map input.")
    exit()

queue = [start_pos]
visited = set()
visited.add(start_pos)
dr = [-1, 0, 1, 0] # up, right, down, left
dc = [0, 1, 0, -1] # up, right, down, left
found = False

print(f"Queue: {[(col, row) for row, col in queue]}")

while queue and not found:
    row, col = queue.pop(0)

    if exit_pos is not None:
        for i in range(4):
            neighbor_row = row + dr[i]
            neighbor_col = col + dc[i]
            if (neighbor_row, neighbor_col) == exit_pos:
                found = True
                break
    
    if found:
        break

    for i in range(4):
        neighbor_row = row + dr[i]
        neighbor_col = col + dc[i]

        if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
            neighbor_char = grid[neighbor_row][neighbor_col]
            # This is the corrected logic: only '_' or 'O' are walkable.
            if (neighbor_char == '_' or neighbor_char == 'O') and (neighbor_row, neighbor_col) not in visited:
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))

    if queue:
        print(f"Queue: {[(col, row) for row, col in queue]}")

if found:
    print("Found the exit portal.")
else:
    print("Cannot reach the exit portal.")
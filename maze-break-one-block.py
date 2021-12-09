'''
    Given a map containing a maze where 0 is passable, 1 is a wall, and you can remove 1 wall block from the maze,
    give the length of the shortest path to get from the start to the exit using only up,down,left,right moves.
    The start is always (0,0) and the end is always (w-1, h-1)

    A* search from front and back, storing the steps to each wall block from both sides.
    then for each mutually populated and corresponding element in each set, look for 
    the one with the lowest combined values from the front to the back. subtract one at the
    end to remove the double counting of the selected block.
'''

def solution(map):
    
    def shortest_path(_start_x, _start_y, _maze, _w, _h):
        nodes = [[None for i in range(_w)] for i in range(_h)];
        nodes[_start_x][_start_y] = 1;
    
        stack = [(_start_x, _start_y)]
        while stack:
            x, y = stack.pop(0);
            for i in ((1,0),(-1,0),(0,-1),(0,1)):
              new_x, new_y = x + i[0], y + i[1];
              if 0 <= new_x < _h and 0 <= new_y < _w:
                if nodes[new_x][new_y] is None:
                    nodes[new_x][new_y] = nodes[x][y] + 1;
                    if _maze[new_x][new_y] == 1 :
                      continue;
                    stack.append((new_x, new_y));
                      
        return nodes;

    w = len(map[0]);
    h = len(map);
    to_exit = shortest_path(0, 0, map, w, h);
    to_start = shortest_path(h-1, w-1, map, w, h);
    
    answer = 4294967296;
    for i in range(h):
        for j in range(w):
            if to_exit[i][j] and to_start[i][j]:
                answer = min(to_exit[i][j] + to_start[i][j], answer);
    return answer - 1;
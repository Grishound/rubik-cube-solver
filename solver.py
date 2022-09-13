import rubik

parent_f = {}
parent_b = {}
def f_BFS(start, parent_f, parent_b):
    if type(start) != list:
        frontier = [start]
    else:
        frontier = start
    next1 = []
    for u in frontier:
        for move in rubik.quarter_twists:
            v = rubik.perm_apply(move, u)
            if v not in parent_f:
                parent_f[v] = u
                next1.append(v)
            if v in parent_b:
                return (1, v)
    frontier = next1
    return (0, frontier)

def b_BFS(end, parent_f, parent_b):
    if type(end) != list:
        frontier = [end]
    else:
        frontier = end
    next1 = []
    for u in frontier:
        for move in rubik.quarter_twists:
            v = rubik.perm_apply(move, u)
            if v not in parent_b:
                parent_b[v] = u
                next1.append(v)
            if v in parent_f:
                return (1, v)
    frontier = next1
    return (0, frontier)

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 
    Assumes the rubik.quarter_twists move set.
    """
    flag = 0
    count = 0
    parent_f[start] = None
    parent_b[end] = None
    answer = []
    f_value = start
    b_value = end
    if f_value == b_value:
        return answer

    while flag == 0 and count < 15:
        f_bit, f_value = f_BFS(f_value, parent_f, parent_b)
        count += 1
        if f_bit == 1:
            check = 'f'
            flag = 1
        if flag == 0:
            b_bit, b_value = b_BFS(b_value, parent_f, parent_b)
            count += 1
            if b_bit == 1:
                check = 'b'
                flag = 1

    if count >= 15:
        return None

    if check == 'f':
        value = f_value
        save = f_value
    else:
        value = b_value
        save = b_value
    while parent_f[value] is not None:
        answer.append(value)
        value = parent_f[value]

    answer = answer[::-1]

    value = save
    while parent_b[value] is not None:
        value = parent_b[value]
        answer.append(value) 

    parent_b.clear()
    parent_f.clear()

    return answer

if __name__ == '__main__':
    start = rubik.I
    middle1 = rubik.perm_apply(rubik.F, start)
    middle2 = rubik.perm_apply(rubik.F, middle1)
    end = rubik.perm_apply(rubik.Li, middle2)
    ans = shortest_path(start, end)
    print ans

    start = rubik.I
    middle1 = rubik.perm_apply(rubik.F, start)
    middle2 = rubik.perm_apply(rubik.L, middle1)
    middle3 = rubik.perm_apply(rubik.F, middle2)
    end = rubik.perm_apply(rubik.L, middle3)
    ans = shortest_path(start, end)
    print(ans)

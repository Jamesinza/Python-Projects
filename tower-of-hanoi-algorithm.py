def hanoi_solver(num):
    left = list(range(num, 0, -1))
    middle = []
    right = []
    moves = []
    moves.append(f"{left} {middle} {right}")
    def move_disks(n, l, m, r):
        if n == 1:
            r.append(l.pop())
            moves.append(f"{left} {middle} {right}")
        else:
            move_disks(n - 1, l, r, m)
            r.append(l.pop())
            moves.append(f"{left} {middle} {right}")
            move_disks(n - 1, m, l, r)
    move_disks(num, left, middle, right)
    return "\n".join(moves)

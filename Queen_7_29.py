# 7. Implement a solution for a Constraint Satisfaction Problem using Branch and    Bound and Backtracking for n-queens problem.


def solve_n_queens(n):
    def is_safe(r, c):
        return not cols[c] and not diag1[r + c] and not diag2[r - c + n - 1]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if is_safe(r, c):
                board[r][c] = "Q"
                cols[c] = diag1[r + c] = diag2[r - c + n - 1] = True
                backtrack(r + 1)
                board[r][c] = "."
                cols[c] = diag1[r + c] = diag2[r - c + n - 1] = False

    board = [["."] * n for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # '/'
    diag2 = [False] * (2 * n - 1)  # '\'
    res = []
    backtrack(0)
    return res

# ---- Main ----
n = int(input("Enter number of queens (N): "))
solutions = solve_n_queens(n)

for i, sol in enumerate(solutions, 1):
    print(f"\nSolution {i}:")
    for row in sol:
        print(row)
print(f"\nTotal solutions: {len(solutions)}")

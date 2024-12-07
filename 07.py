from aoctools.Input import Input


ans1, ans2 = 0, 0


def solve(numbers, x, final, p2):
    if x > final:
        return x, False
    if x == final and len(numbers) == 0:
        return x, True
    if x < final and len(numbers) == 0:
        return x, False
    # make + or *
    mn = numbers[0]
    x1 = x + mn
    nx, solved = solve(numbers[1:], x1, final, p2)
    if not solved:
        x2 = x * mn
        nx, solved = solve(numbers[1:], x2, final, p2)
        if solved:
            return nx, True
        elif p2:
            x3 = int(str(x) + str(mn))
            nx, solved = solve(numbers[1:], x3, final, p2)
            if solved:
                return nx, True
        else:
            return x, False
    else:
        return nx, True
    return x, False


task = Input().get_input().splitlines()

for line in task:
    solution, numbers = line.split(": ")
    solution = int(solution)
    numbers = list(map(int, numbers.split()))

    ans1 += solve(numbers, 0, solution, False)[0]
    ans2 += solve(numbers, 0, solution, True)[0]

print(ans1)
print(ans2)

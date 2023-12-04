from collections import defaultdict


def read_task(filename="test.txt"):
    with open(filename, "r") as file:
        return file.read().splitlines()


def build_graph(task):
    graph = defaultdict(list)
    start, end = (0, 0), (0, 0)

    for y, line in enumerate(task):
        for x, height in enumerate(line):
            if height == "S":
                start = (x, y)
                height = "a"
            elif height == "E":
                end = (x, y)
                height = "z"

            if y + 1 < len(task) and abs(ord(height) - ord(task[y + 1][x])) <= 1 or (
                    y + 1 < len(task) and line[y + 1] == "E"):
                graph[(x, y)].append((x, y + 1))
            if y - 1 >= 0 and abs(ord(height) - ord(task[y - 1][x])) <= 1 or (y - 1 >= 0 and line[y - 1] == "E"):
                graph[(x, y)].append((x, y - 1))
            if x - 1 >= 0 and abs(ord(height) - ord(task[y][x - 1])) <= 1 or (x - 1 >= 0 and line[x - 1] == "E"):
                graph[(x, y)].append((x - 1, y))
            if x + 1 < len(line) and abs(ord(height) - ord(line[x + 1])) <= 1 or (
                    x + 1 < len(line) and line[x + 1] == "E"):
                graph[(x, y)].append((x + 1, y))

    return graph, start, end


def search(graph, start_cord, target_cord):
    def recursive_search(current_cord, way, step=0):
        nonlocal min_steps, best_way
        way.append(current_cord)

        if current_cord == target_cord:
            if step < min_steps:
                min_steps = step
                best_way = way.copy()
            return

        if step >= len(task[0]) * len(task):
            return

        connections = graph[current_cord]
        for c in connections:
            if c not in walked:
                walked.add(c)
                recursive_search(c, way, step + 1)
                walked.remove(c)

    min_steps = len(task) * len(task[0])
    best_way = []
    walked = set()

    recursive_search(start_cord, [])

    return min_steps, best_way


task = read_task()
graph, start, end = build_graph(task)
result = search(graph, start, end)
print(result)

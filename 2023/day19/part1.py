from datetime import datetime
import os
import math
from get_input import GetInput

time_start = datetime.now()


def get_input(inp):
    if os.stat("input.txt").st_size == 0:
        session = os.environ.get("AOC_SESSION")
        data = GetInput().get_today()
        with open("input.txt", "w") as f:
            f.write(data)
    if inp:
        return open("input.txt").read()
    else:
        return open("test.txt").read()


def parse_data():
    sorters, inputs = get_input(True).split("\n\n")
    workflows = {}
    given_inputs = []
    for sorter in sorters.splitlines():
        temp_flow = []
        name, workflow = sorter.split("{")
        workflow = workflow[:-1]
        workflow = workflow.split(",")
        final_destination = workflow.pop(-1)
        for w in workflow:
            condition, destination = w.split(":")
            if ">" in condition:
                label, number = condition.split(">")
                number = int(number)
                temp_flow.append((label, ">", number, destination))
            else:
                label, number = condition.split("<")
                number = int(number)
                temp_flow.append((label, "<", number, destination))
        workflows[name] = (temp_flow, final_destination)
    for inp in inputs.splitlines():
        temp_inputs = []
        inp = inp[1:-1]
        inp = inp.split(",")
        for inpu in inp:
            label, number = inpu.split("=")
            number = int(number)
            temp_inputs.append((label, number))
        given_inputs.append(temp_inputs)
    return workflows, given_inputs


def get_new_workflow(data, starting_label):
    flow = workflow[starting_label]
    final = flow[-1]
    for f in flow[0]:
        if f[0] == "x":
            value = data[0][1]
        elif f[0] == "m":
            value = data[1][1]
        elif f[0] == "a":
            value = data[2][1]
        else:
            value = data[3][1]
        if f[1] == ">":
            if value > f[2]:
                return f[3]
        else:
            if value < f[2]:
                return f[3]
    return final

ans = 0
workflow, inputs = parse_data()
for line in inputs:
    start_label = "in"
    start_label = get_new_workflow(line, start_label)
    while start_label not in "AR":
        start_label = get_new_workflow(line, start_label)
    if start_label == "R":
        continue
    else:
        ans += sum([x[1] for x in line])
print(ans)
print(datetime.now() - time_start)

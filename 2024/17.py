from aoctools.TextGrid import TextGrid
from aoctools.Input import Input
import re
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

ans = 0

# line by line input
registers, program = Input().get_input().split("\n\n")

registers = registers.splitlines()
new_registers = defaultdict(int)
for register in registers:
    register = register[9:]
    letter, number = register.split(": ")
    number = int(number)
    new_registers[letter] = number
registers = new_registers
registers[0] = 0
registers[1] = 1
registers[2] = 2
registers[3] = 3
program = list(map(int, program.split()[1].split(",")))
combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: "A", 5: "B", 6: "C"}
akk = 0
pointer = 0
operand = 0
output = []
while True:
    try:
        opcode = program[pointer]
        operand = program[pointer + 1]
    except IndexError:
        break
    combo_operand = registers[combo[operand]]
    if opcode == 0:
        numerator = registers["A"]
        denominator = 2 ** combo_operand
        registers["A"] = numerator // denominator
    elif opcode == 1:
        registers["B"] = registers["B"] ^ operand
    elif opcode == 2:
        registers["B"] = combo_operand % 8
    elif opcode == 3:
        if registers["A"] != 0:
            pointer = operand
            continue
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif opcode == 5:
        temp = combo_operand % 8
        output.append(temp)
    elif opcode == 6:
        numerator = registers["A"]
        denominator = 2 ** combo_operand
        registers["B"] = numerator // denominator
    elif opcode == 7:
        numerator = registers["A"]
        denominator = 2 ** combo_operand
        registers["C"] = numerator // denominator
    pointer += 2
print(",".join(list(map(str, output))))


def calculate(a):
    b = a % 8
    b = b ^ 5
    c = a >> b
    b = b ^ c
    b = b ^ 6
    return a, b


def part2(program, ans):
    if len(program) == 0:
        return ans
    for i in range(8):
        a = ans << 3 | i
        a, b = calculate(a)
        if b % 8 == program[-1]:
            temp = part2(program[:-1], a)
            if not temp:
                continue
            return temp


print(part2(program, 0))

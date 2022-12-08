input = open("input.txt").read().splitlines()
input = [feld for feld in input if feld != '']
first_line = open("commandInput.txt").read().split(",")

commandCounter = 0
bingo = []
commands = []


def create_board():
    for i in range(len(input)):
        field = []
        x = i % 5
        if x == 0:
            for j in range(5):
                field.append(input[i + j].split())
                bingo.append(field)
                print(bingo)


def who_is_the_winner():
    create_board()
    board = []
    summe = 0
    command = []
    answers = []
    for lastID in range(5, len(first_line)):
        numbers = first_line[:lastID]
        last_number = numbers[-1]

        for bID in range(len(bingo)):
            board = bingo[bID]
            for i in range(5):
                x = 0
                for j in range(5):
                    akk_number = board[i][j]
                    if akk_number in numbers:
                        x += 1
                        if x == 5:
                            summe = 0
                            for b in board:
                                for c in b:
                                    numbs = numbers
                                    if c not in numbs:
                                        summe += int(c)
                            answers.append([int(last_number) * summe])

    return answers


answer = who_is_the_winner()
print(answer[15])


# 5429 too low
# 250511520 too high
input = open("Input.txt").read().splitlines()

co2 = ""
oxygen = ""
able = []


def get_able():
    able.clear()
    for i in input:
        able.append(i)


def get_oxygen():
    global able
    get_able()
    able2 = []
    for i in range(len(input[0])):
        able2 = []
        numbers = []
        for lines in range(len(able)):
            numbers.append(able[lines][i])
        null_rate = numbers.count(str(0))
        one_rate = numbers.count(str(1))
        print(null_rate, one_rate)
        if null_rate > one_rate:
            for lID in range(len(able)):
                if able[lID][i] == "0":
                    able2.append(able[lID])
        elif null_rate <= one_rate:
            for lID in range(len(able)):
                if able[lID][i] == "1":
                    able2.append(able[lID])
        able = able2
        print(able)
        if len(able) == 1:
            return able[0]


def get_co2():
    global able
    get_able()
    able2 = []
    for i in range(len(input[0])):
        able2 = []
        numbers = []
        for lines in range(len(able)):
            numbers.append(able[lines][i])
        null_rate = numbers.count(str(0))
        one_rate = numbers.count(str(1))
        print(null_rate, one_rate)
        if null_rate <= one_rate:
            for lID in range(len(able)):
                if able[lID][i] == "0":
                    able2.append(able[lID])
        elif null_rate > one_rate:
            for lID in range(len(able)):
                if able[lID][i] == "1":
                    able2.append(able[lID])
        able = able2
        print(able)
        if len(able) == 1:
            return able[0]



dec_oxygen = int(get_oxygen(), 2)
dec_co2 = int(get_co2(), 2)
print(get_oxygen(), get_co2())
print(dec_oxygen * dec_co2)

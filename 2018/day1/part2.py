task = open("input.txt").read().splitlines()

n=0
ans = 0
answers = {}
while True:
    n+=1
    for i in task:
        ans += int(i)
        if ans in answers:
            print(ans, n)
            exit()
        #answers.add(ans)
        answers[ans] = 1


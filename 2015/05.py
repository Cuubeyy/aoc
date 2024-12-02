task = open("05.in").read().splitlines()
ans = 0
voels = "aeiou"
for line in task:
    vc = 0
    double = False
    fit = True
    lastc = "."
    for ch in line:
        if ch in voels:
            vc += 1
        if ch == lastc:
            double = True
        lastc = ch
    for c in ["ab", "cd", "pq", "xy"]:
        print(c, line, line.find(c) >= 0)
        if line.find(c) >= 0:
            fit = False
    if vc >= 3 and double and fit:
        ans += 1
print(ans)

"""
    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
"""

# 274 too high
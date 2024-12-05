import networkx as nx
G = nx.Graph()
test = """abcccccccaaaaaccccaaaaaaaccccccccccccccccccccccccccccccccccccaaaaa
abaacccaaaaaaccccccaaaaaaaaaaaaaccccccccccccccccccccccccccccaaaaaa
abaacccaaaaaaaccccaaaaaaaaaaaaaacccccccccccccaacccccccccccccaaaaaa
abaacccccaaaaaacaaaaaaaaaaaaaaaacccccccccccccaacccccccccccccacacaa
abaccccccaaccaacaaaaaaaaaacccaacccccccccccccaaacccccccccccccccccaa
abcccccccaaaacccaaaaaaaaacccccccccccccaaacccaaacccccccccccccccccaa
abccccccccaaaccccccccaaaacccccccccccccaaaaacaaaccacacccccccccccccc
abccccccccaaacaaacccccaaacccccccccccccaaaaaaajjjjjkkkcccccaacccccc
abcccccaaaaaaaaaacccccaaccccccccccciiiiiijjjjjjjjjkkkcaaaaaacccccc
abcccccaaaaaaaaacccccccccccccccccciiiiiiijjjjjjjrrkkkkaaaaaaaacccc
abcccccccaaaaaccccccccccccccccccciiiiiiiijjjjrrrrrppkkkaaaaaaacccc
abcccaaccaaaaaacccccccccccaacaaciiiiqqqqqrrrrrrrrpppkkkaaaaaaacccc
abccaaaaaaaaaaaaccccacccccaaaaaciiiqqqqqqrrrrrruuppppkkaaaaacccccc
abcccaaaaaaacaaaacaaacccccaaaaaahiiqqqqtttrrruuuuupppkkaaaaacccccc
abcaaaaaaaccccaaaaaaacccccaaaaaahhqqqtttttuuuuuuuuuppkkkccaacccccc
abcaaaaaaaaccccaaaaaacccccaaaaaahhqqqtttttuuuuxxuuuppkklcccccccccc
abcaaaaaaaacaaaaaaaaaaacccccaaachhhqqtttxxxuuxxyyuuppllllccccccccc
abcccaaacaccaaaaaaaaaaaccccccccchhhqqtttxxxxxxxyuupppplllccccccccc
abaacaacccccaaaaaaaaaaaccccccccchhhqqtttxxxxxxyyvvvpppplllcccccccc
abaacccccccccaaaaaaacccccccccccchhhpppttxxxxxyyyvvvvpqqqlllccccccc
SbaaccccccaaaaaaaaaaccccccccccchhhppptttxxxEzzyyyyvvvqqqlllccccccc
abaaaaccccaaaaaaaaacccccccccccchhhpppsssxxxyyyyyyyyvvvqqqlllcccccc
abaaaacccccaaaaaaaacccccccccccgggpppsssxxyyyyyyyyyvvvvqqqlllcccccc
abaaacccaaaacaaaaaaaccccccccccgggpppsswwwwwwyyyvvvvvvqqqllllcccccc
abaaccccaaaacaaccaaaacccccccccgggppssswwwwwwyyywvvvvqqqqmmmccccccc
abaaccccaaaacaaccaaaaccaaaccccggpppssssswwswwyywvqqqqqqmmmmccccccc
abcccccccaaacccccaaacccaaacaccgggpppssssssswwwwwwrqqmmmmmccccccccc
abcccccccccccccccccccaacaaaaacgggppooosssssrwwwwrrrmmmmmcccccccccc
abcccccccccccccccccccaaaaaaaacggggoooooooorrrwwwrrnmmmdddccaaccccc
abaccccccccccccaacccccaaaaaccccggggoooooooorrrrrrrnmmddddcaaaccccc
abaccccccccaaaaaaccccccaaaaaccccggfffffooooorrrrrnnndddddaaaaccccc
abaacccccccaaaaaacccccaaaaaacccccffffffffoonrrrrrnnndddaaaaaaacccc
abaaccccccccaaaaaaaccacaaaacccccccccffffffonnnnnnnndddaaaaaaaacccc
abccccccccccaaaaaaaaaaaaaaaccccccccccccfffennnnnnnddddccaaaccccccc
abcccccccccaaaaaaacaaaaaaaaaacccccccccccffeennnnnedddccccaaccccccc
abcccccccccaaaaaaccaaaaaaaaaaaccccccccccaeeeeeeeeeedcccccccccccccc
abccccccccccccaaaccaaaaaaaaaaaccccccccccaaaeeeeeeeecccccccccccccaa
abcccccccaaccccccccaaaaaaaacccccccccccccaaaceeeeecccccccccccccccaa
abaaccaaaaaaccccccccaaaaaaaacccccccccccccaccccaaacccccccccccaaacaa
abaaccaaaaacccccaaaaaaaaaaacccccccccccccccccccccacccccccccccaaaaaa
abaccaaaaaaaaccaaaaaaaaaaaaaacccccccccccccccccccccccccccccccaaaaaa""".split("\n")


abc = "SabcdefghijklmnopqrstuvwxyzE"

grid = [list(r) for r in test]
n, m = len(grid), len(grid[0])
s = (0, 0)
e = (0, 0)
for x in range(n):
    for y in range(m):
        ch = grid[x][y]
        if grid[x][y] == 'S':
            s = (x, y)

        elif grid[x][y] == 'E':
            e = (x, y)

        adjasent = []
        if 0 <= x < n-1:
            adjasent.append((grid[x + 1][y], (x+1, y)))
        if 0 < x <= n:
            adjasent.append((grid[x - 1][y], (x-1, y)))
        if 0 <= y < m-1:
            adjasent.append((grid[x][y + 1], (x, y+1)))
        if 0 < y <= m:
            adjasent.append((grid[x][y - 1], (x, y-1)))

        ch_index = abc.find(ch)
        for a in adjasent:
            a_index = abc.find(a[0])
            if abs(a_index - ch_index) <= 1:
                G.add_edge((x, y), (a[1][0], a[1][1]))

print(nx.shortest_path(G, s, e))
print(len(nx.shortest_path(G, s, e))-1)

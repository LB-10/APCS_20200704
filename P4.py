tree = []
RNAs = []
n = m = 0
def dfs(root):
    global tree, RNAs, n, m
    if tree[root]:
        modsum = 0
        for ch in tree[root]:
            modsum += dfs(ch)

        j = 0
        while j < m:
            if RNAs[root][j] == '@':
                letters = [0 for i in range(26)]
                for ch in tree[root]:
                    letters[ord(RNAs[ch][j]) - ord('A')] += 1
                RNAs[root][j] = chr(letters.index(max(letters)) + ord('A'))
                continue # j will not increse
            else:
                for ch in tree[root]:
                    if RNAs[ch][j] == '@':
                        continue
                    elif RNAs[ch][j] != RNAs[root][j]:
                        modsum += 1
            j += 1

        return modsum
    else:
        return 0
while True:
    try:
        n, m = (int(num) for num in input().strip().split())
    except:
        break
    else:
        roots = []
        tree = [[] for i in range(n+1)]
        RNAs = [[] for i in range(n+1)]
        for i in range(n):
            id, father, rna = (v for v in input().strip().split())
            id = int(id)
            father = int(father)
            rna = list(rna)
            if id == father:
                roots.append(id)
            else:
                tree[father].append(id)
            RNAs[id] = rna
        modsum = 0
        for root in roots:
            modsum += dfs(root)
        print(modsum)
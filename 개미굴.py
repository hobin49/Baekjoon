# import sys

# class Trie:
#     def __init__(self):
#         self.root = {}

#     def add(self, foods):
#         cur = self.root

#         for food in foods:
#             if food not in cur:
#                 cur[food] = {}
#             cur = cur[food]
#         cur[0] = True

#     def travel(self, level, cur):

#         if 0 in cur:
#             return

#         cur_child = sorted(cur)

#         for ch in cur_child:
#             print("--" * level + ch)
#             self.travel(level+1, cur[ch])


# input = sys.stdin.readline

# n = int(input())

# trie = Trie()

# for _ in range(n):
#     data = list(input().split())
#     trie.add(data[1:])

# trie.travel(0, trie.root)


import sys

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, feeds):
        cur = self.root

        for feed in feeds:
            if feed not in cur:
                cur[feed] = {}
            cur = cur[feed]

        cur[0] = True

    def travel(self, level, cur):
        if 0 in cur:
            return

        cur_child = sorted(cur)

        for c in cur_child:
            print("--" * level + c)

            self.travel(level+1, cur[c])


input = sys.stdin.readline

n = int(input())
trie = Trie()

for _ in range(n):
    data = list(input().split())
    trie.insert(data[1:])

trie.travel(0, trie.root)

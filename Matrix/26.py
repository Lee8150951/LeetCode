from typing import List
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         ans = list()
#         alphaDictory = dict()
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 alphaDictory[str(i) + "," + str(j)] = board[i][j]
#         for word in words:
#             wordMap = list()
#             for i in word:
#                 # 获取坐标
#                 position = [k for k, v in alphaDictory.items() if v == i]
#                 wordMap.append(position)
#             for position in wordMap:
#                 for i in range(len(position)):
#                     cur = position[i]
#                     s_array = cur.split(',')
#                     correct01 = str(int(s_array[0]) + 1) + "," + str(s_array[1])
#                     correct02 = str(s_array[0]) + "," + str(int(s_array[1]) + 1)
#                     if correct01 in position[i + 1] or correct02 in position[i + 1]:
                        

from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)

if __name__=="__main__":
    board = [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]]
    words = ["oath", "pea", "eat", "rain"]
    method = Solution()
    answer = method.findWords(board, words)
    print(answer)
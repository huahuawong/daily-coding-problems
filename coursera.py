# Given a 2D board of characters and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# Explanation, the idea is to use a DFS approach
# We can first start by keep iterating through the characters in the word, and if the length of the word becomes zero, return True because that means all the characters are checked
# Of course, we have to check if i is less than 0 or larger than length of board, likewise for j, and if word[0] is the same as board[i][j]
# We use a variable "tmp" such that we can keep track of visited elements and re-insert it back

def exist(board, word):
    if not board:
        return False
    if len(word) > len(board)*len(board[0]):
      return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False


def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]
    board[i][j] = "#"
    result = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) \
             or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return result


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exist(board, "ABPD")

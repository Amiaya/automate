# Chapter 4


# def comma(spam):
#     x = ""
#     for cha in range(len(spam)):
#         if cha == len(spam) - 1:
#             x += "and " + spam[cha]
#         else:
#             x += spam[cha] + ", "
#     return x
#
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
# print(comma(spam))


# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
#
#
# for i in range(6):
#     for a in range(9):
#         print(grid[a][i], end="")
#     print()

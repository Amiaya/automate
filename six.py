
# Chapter 6

# def PrintTable(tableData):
#     colWidth = [0] * len(tableData)
#     for i in range(3):
#         for j in range(4):
#             if len(tableData[i][j]) > colWidth[i]:
#                 colWidth[i] = len(tableData[i][j])
#     for y in range(4):
#         for x in range(3):
#             print(tableData[x][y].rjust(colWidth[x]), end=" ")
#         print()
#
#
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
# PrintTable(tableData)

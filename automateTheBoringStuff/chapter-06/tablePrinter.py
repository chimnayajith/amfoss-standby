def printTable(data):
    for i in range(0 , 4):
        for each in data:
            print( each[i].rjust(10) , end="")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

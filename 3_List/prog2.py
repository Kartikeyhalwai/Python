matrix =[]
for i in range(int(input())):
        name = input()
        score = float(input())
        matrix.append([])
        for j in range(2):
            matrix[i][j].append(name)
            matrix[i].append(name)


print(matrix)
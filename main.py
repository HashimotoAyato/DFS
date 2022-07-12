n, m = map(int, input().split())
stage = []
for i in range(n):
    stage.append(list(input()))

count = 0
stack = []
for i in range(n):
    for j in range(m):
        if stage[i][j] == 'W':
            stack.append([i,j])
            count += 1

            while 0 < len(stack):
                x = stack.pop()
                if stage[x[0]][x[1]] == 'W':

                    stage[x[0]][x[1]] = str(count)
                    if 0 < x[0]:
                        stack.append([x[0]-1, x[1]])
                        if 0 < x[1]:
                            stack.append([x[0]-1, x[1]-1])
                    
                    if 0 < x[1]:
                        stack.append([x[0], x[1]-1])
                        if x[0] < n-1:
                            stack.append([x[0]+1, x[1]-1])

                    if x[0] < n-1:
                        stack.append([x[0]+1, x[1]])
                        if x[1] < m-1:
                            stack.append([x[0]+1, x[1]+1])
                        
                    if x[1] < m-1:
                        stack.append([x[0], x[1]+1])
                        if 0 < x[0]:
                            stack.append([x[0]-1, x[1]+1])
                else:
                    pass

print('ans={}'.format(count))
for i in range(n):
    for j in range(m):
        print(stage[i][j], end='')
    print()

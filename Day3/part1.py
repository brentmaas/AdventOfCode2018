import numpy as np

claims = np.zeros((1000, 1000))

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        x = int(line[line.index('@')+2:line.index(',')])
        y = int(line[line.index(',')+1:line.index(':')])
        w = int(line[line.index(':')+2:line.index('x')])
        h = int(line[line.index('x')+1:])
        claims[x:x+w,y:y+h] += 1

print(np.sum(claims > 1))
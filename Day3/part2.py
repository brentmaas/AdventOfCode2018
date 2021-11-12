import numpy as np

claims = np.zeros((1000, 1000))
ixywh = []

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        id = int(line[1:line.index('@')-1])
        x = int(line[line.index('@')+2:line.index(',')])
        y = int(line[line.index(',')+1:line.index(':')])
        w = int(line[line.index(':')+2:line.index('x')])
        h = int(line[line.index('x')+1:])
        claims[x:x+w,y:y+h] += 1
        ixywh.append((id, x, y, w, h))

for i in range(len(ixywh)):
    id, x, y, w, h = ixywh[i]
    if np.all(claims[x:x+w,y:y+h] == 1):
        print(id)
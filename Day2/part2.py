ids = []

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        ids.append(line)

for i in range(len(ids) - 1):
    for j in range(i + 1, len(ids)):
        diff = 0
        at = 0
        for k in range(len(ids[i])):
            if ids[i][k] != ids[j][k]:
                diff += 1
                at = k
            if diff > 1:
                break
        if diff == 1:
            print(ids[i][:at] + ids[i][at+1:])
lines = []
with open("Input.txt", "r") as f:
    while line := f.readline():
        lines.append(line.rstrip())
lines.sort()

guards = {}
shifts = {}

guard = -1
start = -1
asleep = 0
shift = [0] * 60
for line in lines:
    if line.endswith("begins shift"):
        if guard != -1:
            if not (guard in guards):
                guards[guard] = asleep
                shifts[guard] = [shift]
            else:
                guards[guard] += asleep
                shifts[guard].append(shift)
        guard = int(line[line.index("#")+1:line.index(" begins")])
        asleep = 0
        start = -1
        shift = [0] * 60
    elif line.endswith("falls asleep"):
        start = int(line[line.index(":")+1:line.index("]")])
    elif line.endswith("wakes up"):
        end = int(line[line.index(":")+1:line.index("]")])
        asleep += end - start
        shift[start:end] = [1] * (end - start)
        start = -1
if not (guard in guards):
    guards[guard] = asleep
    shifts[guard] = [shift]
else:
    guards[guard] += asleep
    shifts[guard].append(shift)

sums = [0] * 60
guard = list(guards.keys())[[guards[g] for g in guards].index(max([guards[g] for g in guards]))]
for shift in shifts[guard]:
    for i in range(60):
        sums[i] += shift[i]
print(sums.index(max(sums)) * guard)
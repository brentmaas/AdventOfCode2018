two = 0
three = 0

with open("Input.txt", "r") as f:
    while line := f.readline().rstrip():
        counts = {}
        for c in line:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        nums = [counts[c] for c in counts]
        if 2 in nums:
            two += 1
        if 3 in nums:
            three += 1

print(two * three)
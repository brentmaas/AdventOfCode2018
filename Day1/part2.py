import numpy as np

data = np.loadtxt("Input.txt", dtype=np.int32)
freqs = np.array([0])
dfreq = np.sum(data)
curr = 0
for i in data:
    curr += i
    if curr in freqs:
        print(curr)
        exit()
    freqs = np.append(freqs, curr)

newfreqs = freqs[1:] + dfreq
while True:
    for i in newfreqs:
        if i in freqs:
            print(i)
            exit()
        freqs = np.append(freqs, i)
    newfreqs += dfreq
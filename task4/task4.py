from filereader import nums

nums.sort()

diap = list(range(nums[0], (nums[-1]+1)))

steps = []

for i in diap:
    s = 0
    for j in nums:
        t = 0
        if j > i:
            t = j - i
        if j < i:
            t = i - j

        s = s + t
    steps.append(s)


steps.sort()

print(steps[0])

import re
import sys


print('hello')

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = input('Пожалуйста, введите адрес файла: ')

with open(file, encoding="utf8") as myFile:
    all_p = myFile.readlines()
    fp = []
    nums = []

    for a in all_p:
        value = re.findall(r"[+-]?\d*\.\d+|\d+", a)

        if value:
            fp.extend(value)

    for p in fp:
        nums.append(int(p))

print(nums)

import re
import sys


if len(sys.argv) > 1:
    file1 = sys.argv[1]
else:
    file1 = input("Пожалуйста, введите адрес файла1: ")

with open(file1, encoding="utf8") as myFile:
    s1 = list(myFile.readline().split())
    c = []

    for n in s1:
        c.append(float(n))

    r = float(myFile.readline())


if len(sys.argv) > 2:
    file1 = sys.argv[2]
else:
    file2 = input("Пожалуйста, введите адрес файла2: ")

with open(file2, encoding="utf8") as myFile:
    all_p = myFile.readlines()
    points = []
    fp = []
    pt = []
    x = 0

    for a in all_p:
        value = re.findall(r"[+-]?\d*\.\d+|\d+", a)

        if value:
            fp.extend(value)

    for p in fp:
        pt.append(float(p))

    while x <= pt[-2]:
        t = pt[x:x+2]
        if t:
            points.append(t)

        x += 2
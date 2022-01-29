import sys


print("hello")


if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = int(input('Пожалуйста, введите число, задающее длинну массива: '))
if len(sys.argv) > 2:
    m = int(sys.argv[2])
else:
    m = int(input('Пожалуйста, введите число, задающее длинну обхода: '))

nums = list(range(1, n + 1))

# print("массив будет задан числом {0} и будет иметь длинну обхода {1}".format(n, m))


i = 0
x = 0
way = [1, ]
stp = m-1

while x != nums[0]:
    try:
        step = list(range(nums[i], nums[i + stp] + 1))

    except IndexError as e:
        if x == nums[-1]:
            i = 0
            step.extend(list(range(nums[i], nums[i+stp])))
        else:
            t = nums.index(x)
            j = t - n
            s = j + m
            step = [(nums[j]), ]
            while j != s:
                step.append(nums[j])
                j += 1
    finally:
        x = step[-1]
        i = x-1
        if x != nums[0]:
            way.append(x)

print(way)


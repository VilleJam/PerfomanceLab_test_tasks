import json
import sys


print('hello')

if len(sys.argv) > 1:
    if 'tests.json' in sys.argv[1]:
        tests_file = sys.argv[1]
else:
    tests_file = input("Пожалуйста, введите адрес test.json: ")
if len(sys.argv) > 2:
    if 'values.json' in sys.argv[2]:
        values_file = sys.argv[2]
else:
    values_file = input("Пожалуйста, введите адрес values.json: ")

with open(values_file) as myValues:
    values = json.load(myValues)

v = values
v0 = list(values.values())
v1 = v0[0]

with open(tests_file) as myTests:
    tsts = json.load(myTests)

t = tsts.values()
tk = tsts.keys()
t1 = list(t)[0]


def stepper(m):
    for i in v1:
        i_iter = iter(i)
        p = list(range(0, len(m)))
        for j in p:
            if i['id'] == m[j]['id']:
                    m[j]['value'] = i['value']
            try:
                if m[j]['values']:
                    t = m[j]['values']
                    stepper(t)
            except KeyError as e:
                pass
            finally:
                j += 1
        next(i_iter)
    return m


stepper(t1)

print(t1)

with open('report.json', 'w', encoding='utf8') as f:
    json.dump(t1, f, ensure_ascii=False, indent=4)

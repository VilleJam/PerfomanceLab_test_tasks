print('hello')

from filereader import c, r, points


for point in points:
    p = (point[0]-c[0])**2 + (point[1]-c[1])**2

    if p < r**2:
        print('1 \n')
    elif p == r**2:
        print('0 \n')
    else:
        print('2 \n')

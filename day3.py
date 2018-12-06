import numpy as np


def fabric_counter(n, fabric):
    counter = 0

    for element in n:
        for i in range(element[-1]):
            fabric[element[2] + i][element[1]:element[1] + element[-2]] += 1

    for element in fabric:
        for i in element:
            if i > 1:
                counter += 1
    return counter


if __name__ == '__main__':
    fabric = np.zeros((1000,1000))
    n = [x.replace(",", " ").replace(":","").replace("x", " ").replace("@", "").split() for x in map(str,input().split('#'))]
    n = [[int(x) for x in element] for element in n]
    n.pop(0)
    print("Result star 1 day 3: {}".format(fabric_counter(n, fabric)))








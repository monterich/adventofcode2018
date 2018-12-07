import numpy as np

def star1(n,fabric):
    fabric_claim = fabric
    counter = 0
    for element in n:
        for i in range(element[-1]):
            fabric_claim[element[2]+i][element[1]:element[1] + element[-2]] += 1

    for element in fabric_claim:
        for i in element:
            if i > 1:
                counter += 1
    return counter


def star2(n, fabric):
    for element in n:
        for i in range(element[-1]):
            for pos in range(element[-2]):
                if fabric[element[2]+i][element[1]+pos] == 0:
                    fabric[element[2]+i][element[1] + pos] = element[0]
                else:
                    fabric[element[2] + i][element[1] + pos] = 'NaN'

def counter(n,fabric):
    for line in n:
        c = (fabric == line[0]).sum()
        if c == line[-1]*line[-2]:
            result = line[0]
    return result

if __name__ == '__main__':
    fabric = np.zeros((1000,1000))
    fabric2 = np.zeros((1000,1000))

    n = [x.replace(",", " ").replace(":","").replace("x", " ").replace("@", "").split() for x in map(str,input().split('#'))]
    n = [[int(x) for x in element] for element in n]
    n.pop(0)

    print("Result star 1 day 3: {}".format(star1(n,fabric)))
    star2(n,fabric2)
    print("Result star 2 day 3: {}".format(counter(n,fabric2)))

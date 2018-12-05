import collections
def star1(n):
    two = 0
    three = 0
    counter = [[collections.Counter(i)[x] for x in collections.Counter(i)] for i in n]
    for i in counter:
        if 2 in i and 3 in i:
            two+=1
            three+=1
        elif 2 in i:
            two+=1
        elif 3 in i:
            three += 1

    print("Result star one day 2: " + str(two*three))


def hamdist(str1, str2):
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1

    return diffs

def star2(n):

    for element in n:

        for x in n:
            if hamdist(element, x) == 1:
                ID1 = element
                ID2 = x
    results =""
    for i in range(len(ID1)):
        if ID1[i] == ID2[i]:
            results += str(ID1[i])
    return results


if __name__ == '__main__':
    n = list(map(str,input().split()))
    print(star1(n))
    print(star2(n))

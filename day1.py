def first_star(n, start):
    for i in n:
        start += i
    print("Result first start day 1: " + str(start))


def second_star(n, start):
    counter = 0
    for i in n:
        start += i
        if start in result:
            print("Result second star day 1: " + str(start))
            break
        else:
            result.append(start)
            counter += 1
            if counter == len(n):
                second_star(n, start)

n = list(map(int,input().split()))
start = 0
result = []

first_star(n,start)
second_star(n, start)

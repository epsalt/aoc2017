from collections import deque

## Part 1
def captcha(n):
    string = list(str(n))
    deq = deque(string)
    deq.append(deq.popleft())
    pairs = zip(string, deq)

    total = 0
    for pair in pairs:
        i, j = map(int, pair)
        if i == j:
            total = total + i

    return(total)

## Part 2
def captcha2(n):
    string = list(str(n))
    deq = deque(string)

    for i in range(len(deq)//2):
        deq.append(deq.popleft())
    pairs = zip(string, deq)

    total = 0
    for pair in pairs:
        i, j = map(int, pair)
        if i == j:
            total = total + i

    return(total)

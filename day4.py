from collections import deque

def passphrase(string, part2 = False):
    words = string.split(" ")
    if part2:
        words = [''.join(sorted(word)) for word in words]
    deq = deque(words)

    for i in range(len(deq)):
        word = deq.pop()
        if word in deq:
            return False
        else:
            deq.appendleft(word)
    return True

def main(INPUT):
    with open(INPUT) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        ok_count = 0
        for line in content:
            if passphrase(line): ok_count = ok_count + 1
            else: pass
        return(ok_count)

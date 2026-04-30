t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    coins = []
    for ai in a:
        w = 100 // ai
        coins.append((w, ai))
    
    coins.sort()
    
    reachable = 0
    ok = True
    
    for w, cnt in coins:
        if w > reachable + 1:
            ok = False
            break
        reachable += w * cnt
    
    if reachable >= 100 * n and ok:
        print("Yes")
    else:
        print("No")
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 1
    
    for m in set(a):
        pref = 0
        last_pref = 0
        seen_m = False
        cnt = 0
        
        for x in a:
            if x >= m:
                pref += 1
            else:
                pref -= 1
            
            if x == m:
                seen_m = True
            
            if seen_m and pref >= last_pref:
                cnt += 1
                last_pref = pref
                seen_m = False
        
        ans = max(ans, cnt)
    
    print(ans)
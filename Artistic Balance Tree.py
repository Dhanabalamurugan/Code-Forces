t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    
    odd_vals = []
    even_vals = []
    
    for i in range(n):
        if (i + 1) % 2 == 1:
            odd_vals.append(a[i])
        else:
            even_vals.append(a[i])
    
    odd_vals.sort(reverse=True)
    even_vals.sort(reverse=True)
    
    cnt_odd = sum(1 for xi in x if xi % 2 == 1)
    cnt_even = m - cnt_odd
    
    take = 0
    take += sum(odd_vals[:cnt_odd])
    take += sum(even_vals[:cnt_even])
    
    print(sum(a) - take)
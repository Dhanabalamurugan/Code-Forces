t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    two = []
    three = []
    both = []
    none = []
    
    for x in a:
        if x % 6 == 0:
            both.append(x)
        elif x % 2 == 0:
            two.append(x)
        elif x % 3 == 0:
            three.append(x)
        else:
            none.append(x)
    
    print(*(two + none + three + both))
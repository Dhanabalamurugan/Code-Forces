for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        r = i
        c = row.index(1) 

# Manhattan Distance Formula
# 2 instead of 3 because of indexing
print(abs(r - 2) + abs(c - 2))  
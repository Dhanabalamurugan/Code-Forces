points = []
n=int(input())
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
visited = [False]*n

def dfs(i):
    visited[i] = True
    for j in range(n):
       if not visited[j]:
          if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
              dfs(j)

components = 0

for i in range(n):
   if not visited[i]:
      dfs(i)
      components += 1

print(components - 1)

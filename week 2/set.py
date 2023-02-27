n = int(input())
arr = map(int, input().split())

s=set()
for i in arr:
    s.add(i)
s.remove(max())
print(s.max())
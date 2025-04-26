t = int(input())
while t:
    a, b, c = map(int,input().split())
    if a + b == c or a + c == b or b + c ==a:
        print("YES")
    else:
        print("NO")
    t = t-1
#https://codeforces.com/contest/1742/problem/A

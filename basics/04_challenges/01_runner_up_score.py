n=int(input())
arr=map(int,input().split())
result=sorted(set(arr))[-2]
print(result)

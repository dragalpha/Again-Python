#n=int(input())
arr=list(map(int,input().split()))
result=sorted(set(arr))[1]
print(result)

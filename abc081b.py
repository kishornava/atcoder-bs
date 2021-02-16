n=int(input())
num = list(map(int,input().split()))
num_div=0
list1 = True
while list1 :
    for i in range(n):
        if num[i]%2 == 1:
            list1 = False
            break
        else:
            num[i]=num[i]//2
    if list1:
        num_div +=1

print(num_div)
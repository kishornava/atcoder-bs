# a = int(input())
# b,c=map(int,input().split())
# s= input()
# print(a+b+c,s)

a = int(input())
s= input()
tokens = s.split()
b= int(tokens[0])
c= int(tokens[1])
s = input()

print(a+b+c,s)
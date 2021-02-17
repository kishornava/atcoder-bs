A = int(input())
B = int(input())
C = int(input())
X = int(input())

num_combination = 0

for n_500 in range (0,A+1):
    for n_100 in range(0,B+1):
        n_50 = (X-n_500*500-n_100*100)//50
        if n_50 <= C and n_50 >= 0:
            num_combination+=1

print(num_combination)

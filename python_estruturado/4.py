num = int(input())
sum = 0
flag = False

while num != 0:
    sum += num%10
    if flag == True:
        break
    num = num//10
    if num//10 < 1:
        flag = True
    
print("A soma é", sum)
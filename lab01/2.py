s = str (input())
num_vogais = 0

for i in range(len(s)):
    if(s[i] == "a"
    or s[i] == "e"
    or s[i] == "i"
    or s[i] == "o"
    or s[i] == "u"):
        num_vogais += 1
        
print("O número de vogas é", num_vogais)
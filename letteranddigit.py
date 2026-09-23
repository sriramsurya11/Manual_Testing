n=input()
letter=0
digit=0
for ch in n:
    if(ch.isalpha()):
        letter+=1
    elif(ch.isalnum()):
        digit+=1
print(letter)
print(digit)
words = ["north", "south", "west", "east", "center", "upward", "downward", "forward", "backward", "sideward"]

numw = int(input("Number of letters: "))

disword = []
x = 0
for i in range(10):
    if len(words[x]) >= numw:
        disword.append(words[x])
    x+=1
print(disword)
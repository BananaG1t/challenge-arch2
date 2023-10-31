tekst = "IF YOU COPY THIS SENTENCE TWO HUNDRED TIMES AND REMOVE ALL WORDS WITH EXACTLY ONE LETTER E IN IT WHAT WILL BE THE THOUSANDTH WORD FOLLOWED BY THE HUNDREDTH WORD. " * 200

words = tekst.split(" ")
newwords = []
for word in words:
    if word.count("E") != 1:
        newwords.append(word)

print(newwords[999])
print(newwords[99])

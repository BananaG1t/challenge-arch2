numb = 0
cnt = 0
switch = False
while True:
    if numb % 10 == 0:
        switch = not switch
    if switch:
        if cnt % 2:
            numb += cnt
        else:
            numb -= cnt
    elif cnt % 4 == 0:
        numb -= cnt
    else:
        numb += cnt
    if cnt == 1000:
        break
    print(numb)
    cnt+=1


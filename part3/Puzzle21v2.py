numb = 0
cnt = 1
switch = False
while True:
    if switch:
        for i in range(4):
            if cnt % 2 == 0:
                numb -= cnt
            else:
                numb += cnt
            print(numb)
            #print(cnt)
            if cnt == 1000:
                break
            cnt += 1
    else:
        for i in range(7):
            if cnt % 4 == 0:
                numb -= cnt
            else:
                numb += cnt
            print(numb)
            #print(cnt)
            if cnt == 1000:
                break
            cnt += 1
    if cnt == 1000:
        break
    switch = not switch
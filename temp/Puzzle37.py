from textwrap import wrap

encrypted_message = "TRIEHERTSUOSELCEHAOTHTESNRUIOEABWR"
combos = []


for first in range(1,10):
    for sec in range(1,10):
        for thr in range(1,10):
            for fourth in range(1,10):
                for fifth in range(1,10):
                    combos.append(f"{fifth}{fourth}{thr}{sec}{first}")


def thingy(text, lenght):
    new_messagelist = wrap(text, lenght)
    new_message = ""
    for each in new_messagelist:
        new_message += each[::-1]
    return new_message


for combo in combos:
    new_message = encrypted_message
    for number in combo:
        new_message = thingy(new_message, int(number))
    if "" in new_message:
        print(new_message, combo[::-1])
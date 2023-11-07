encrypted = "CIJLRMAQFUPVEKHSMUEZFULZGLYFWJOSVMJNFGAXWNARWQFOFGDXKFQ"


for startnumb in range(26):
    for add in range(26):
        newstring = ""
        numb = startnumb
        for char in encrypted:
            asci = ord(char) - numb
            while asci < 65:
                asci += 26
            newstring += chr(asci)
            numb += add
        print(newstring, startnumb, add)
def rot13(message):
    i=0
    r = ''
    mini_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    maxi_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for item in message:
        if message[i].islower():
            if mini_alph.index(item)+13 < 26:
                r = r + mini_alph[mini_alph.index(item)+13]
            else:
                r = r + mini_alph[mini_alph.index(item) - 13]
        elif message[i].isupper():
            if maxi_alph.index(item) + 13 < 26:
                r = r + maxi_alph[maxi_alph.index(item)+13]
            else:
                r = r + maxi_alph[maxi_alph.index(item) - 13]
        else:
            r = r + message[i]
        i+=1
    return r
a = "abcdefghijklmnopqrstuvwxyz"
print(rot13(a))

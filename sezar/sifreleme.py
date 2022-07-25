k=3

mesaj="serkan"

alfabe="abcçdefgğhıijklmnoöprsştuüvyz"

boyut=len(alfabe)

sifreli_mesaj=""

print("mesaj:",mesaj)
print("\n\n\n")

for i in mesaj:
    for c in alfabe:
        if i == c:
            konum=alfabe.index(c) 
            konum+=k

            sifreli_mesaj+=alfabe[konum % boyut]


print("sifreli mesaj:",sifreli_mesaj)
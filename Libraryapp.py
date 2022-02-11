

import sqlite3





print("Kütüphane Uygulamanıza Hoşgeldiniz")


def addbook():


    while True:

        kitapadi = input("lütfen kitap adı giriniz : ")
        kitapyazar = input("lütfen yazar adı giriniz : ")
        kitapkodu = input("lütfen kitap kodunu giriniz : ")

        baglanti = sqlite3.connect("mylibrary.db")

        isaretci = baglanti.cursor()
        isaretci.execute("""INSERT INTO kitaplar
                            (kitap_adi,kitap_yazar,kitap_kodu)
                            VALUES
                            ('{}','{}',{})


                            """.format(kitapadi,kitapyazar,kitapkodu))
        baglanti.commit()
        baglanti.close()
        print("kayıt işlemi başarıyla tamamlandı")
        opt=input("lütfen çıkmak istiyorsanız 'Ç ' tuşuna basınız ")
        if opt == "Ç":
            break


def searchbook():
    while True:

        print("Kitap sorgulama alanındasınız ")

        baglanti = sqlite3.connect("mylibrary.db")

        isaretci = baglanti.cursor()

        kitapadisorgu=input("lütfen kitap adını giriniz : ")

        kitapyazarsorgu=input("lütfen kitap yazarını giriniz : ")

        kitapkodusorgu = input("lütfen kitap kodu  giriniz : ")
        if kitapadisorgu:

            getir=isaretci.execute("SELECT * from kitaplar WHERE kitap_adi = '{}' ".format(kitapadisorgu))
        elif kitapkodusorgu:

            getir = isaretci.execute("SELECT * from kitaplar WHERE kitap_kodu = '{}' ".format(kitapkodusorgu))
        elif kitapyazarsorgu:

            getir = isaretci.execute("SELECT * from kitaplar WHERE kitap_yazar = '{}' ".format(kitapyazarsorgu))


        fetch=getir.fetchall()
        adet=len(fetch)
        for i in range(0,len(fetch)):
            print(adet," adet sonuç bulundu")
            print("""{} kitabının : 
                    yazarı : {} 
                    kodu : {}""".format(fetch[i][0],fetch[i][1],fetch[i][2]))

        opt1=input("lütfen çıkmak istiyorsanız 'Ç' tuşuna basınız : ")
        if opt1 == "Ç":
            break





while True:
    print("Kitap eklemek :1 | Kitap sorgulamak : 2 ")

    secenek=int(input("lütfen yapmak istediğiniz şeyi belirtin: "))
    print(type(secenek))

    if secenek == 1:
        addbook()

    elif secenek == 2 :
        searchbook()

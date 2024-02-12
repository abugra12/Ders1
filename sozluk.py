bilinmeyen_sozcukler = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SUS": "Eğer bir şey şüpheliyse bu sözcük kullanılır",
            "SHEESH": "Onaylamamak"
            }
while True : 
    kelime = input("""Bu kelimelerden hangisini bilmiyorsunuz :
    Cringe
    Lol
    Sus
    Sheesh
    
Lütfen yazacağınız kelimenin harflerinin hepsini büyük yazınız
-->""")

    if kelime in bilinmeyen_sozcukler.keys():
        print("Bilmedigininz ",kelime," sozcugunun anlami : \n")
        print(bilinmeyen_sozcukler[kelime])
        break
        
    else : 
        print("Girdiğiniz kelime sözlükte yok lütfen tekrar deneyeniz.")

import random
import time

simgeler = ['Karo', 'Maça', 'Sinek', 'Kupa']  # Simgeleri yaziyoruz.
sayılar = ['1    ', '2    ', '3    ', '4    ', '5    ', '6    ', '7    ', '8    ', '9    ', '10    ', 'Vale', 'Kız',
           'Papaz']  # Simgelerin icinde yer alacak degerleri  yaziyoruz.
kartlar = []  # Bos bir kartlar dizisi yazıyoruz.Burada sayılar ve simgeler birlesecek.
oync1 = []  # 1. oyuncuya dagitilacak kartlari tutacak bir  dizi yazıyoruz.Hepsi için tekrarlıyoruz.
oync2 = []  # 2. oyuncu icin.
oync3 = []  # 3. oyuncu icin.
oync4 = []  # 4. oyuncu icin.

for i in simgeler:
    for j in sayılar:
        kartlar.append(i + ' ' + str(j))  # Sayilari ve simgeleri birbiriyle karıstırıp kartlar dizisine gönderiyoruz.

krtsayisi = 52
while krtsayisi != 39:
    atama = random.choice(kartlar)  # Kartların icinden rastgele kart secer.
    time.sleep(0.1)  # "random.choice'in" her seciminin arasina 0.1 saniye bekleme atıyoruz(alıntıdır).
    oync1.append(atama)  # İlk cekilen rastgele 13 kartı oync1 dizisine ekliyoruz.
    kartlar.remove(atama)  # Cekilen kart kartlar dizisinden siliniyor.
    krtsayisi = krtsayisi - 1

while krtsayisi != 26:
    atama = random.choice(kartlar)  # Kartların icinden rastgele kart secer.
    time.sleep(0.1)  # "random.choice'in" her seciminin arasina 0.1 saniye bekleme atıyoruz(alıntıdır).
    oync2.append(atama)  # İkinci cekilen rastgele 13 kartı oync2 ekliyoruz.
    kartlar.remove(atama)  # Cekilen kart kartlar dizisinden siliniyor.
    krtsayisi = krtsayisi - 1

while krtsayisi != 13:
    atama = random.choice(kartlar)  # Kartların icinden rastgele kart secer.
    time.sleep(0.1)  # "random.choice'in" her seciminin arasina 0.1 saniye bekleme atıyoruz(alıntıdır).
    oync3.append(atama)  # ucuncu cekilen rastgele 13 kartı oync3 dizisine ekliyoruz.
    kartlar.remove(atama)  # Cekilen kart kartlar dizisinden siliniyor.
    krtsayisi = krtsayisi - 1

while krtsayisi != 0:
    atama = random.choice(kartlar)  # Kartların icinden rastgele kart secer.
    time.sleep(0.1)  # "random.choice'in" her seciminin arasina 0.1 saniye bekleme atıyoruz(alıntıdır).
    oync4.append(atama)  # dorduncu cekilen rastgele 13 kartı oync4 dizisine ekliyoruz.
    kartlar.remove(atama)  # Cekilen kart kartlar dizisinden siliniyor.
    krtsayisi = krtsayisi - 1


def dagit():
    print('Oyuncu 1 \tOyuncu 2 \tOyuncu 3 \tOyuncu 4')  # Dagitilan kartlari ekrana  yazıyoruz.
    for i in range(0,
                   13):  # 0 dan  13 ' e kadar dagittigimiz butun dizilerin sirasiyla 0.1.2.3...12. indislerini ekrana yazdiriyoruz.

        print(oync1[i] + '\t' + oync2[i] + '\t' + oync3[i] + ' \t' + oync4[i])


dagit()  # Calıstırıyoruz.
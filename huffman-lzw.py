import time

#21100011010 METİN FURKAN YAMAN
#lzw

start=time.perf_counter()


kelime=open("C:/Users/windows-10/Desktop/21100011010_odev4/lzw_baslangic.txt","r")
kelime=kelime.read()
liste=[]
dict={}
sc=""
output_syc=0
syc=1
sayac=0
us_sayac=0
us_sayac2=0

#harfleri başlangıçta sözlüğe ekleyen kısım.
for i in kelime:
    if i in liste:
        pass
    else:
        liste.append(i)

harf_sayisi=len(liste)
tut=harf_sayisi


baslangic_uzunluk=len(kelime)


# bit hesaplama 
while harf_sayisi % 2 == 0:
    harf_sayisi = harf_sayisi / 2
    

if harf_sayisi == 1:
    while(tut>1):
        tut=tut/2
        us_sayac+=1
    us_sayac+=1
else:
    while(tut>1):
        tut=tut/2
        us_sayac+=1

for i in liste:
    dict[i]=syc
    syc+=1
    

#lzw çalışma kısmı
for i in kelime:
    if sayac==0:
        sc=i
        temp=i
        sayac+=1
    else:
        sc=temp+i
        if sc in dict:
            temp=sc
        else:
            temp=i
            dict[sc]=syc
            syc+=1
            output_syc+=1
output_syc+=1 #en sondaki tempi outputa eklemek için.

harf_sayisi=output_syc
tut=harf_sayisi


while harf_sayisi % 2 == 0:
    harf_sayisi = harf_sayisi / 2
    
if harf_sayisi == 1:
    while(tut>1):
        tut=tut/2
        us_sayac2+=1
    us_sayac2+=1
else:
    while(tut>1):
        tut=tut/2
        us_sayac2+=1

        
baslangic=us_sayac*baslangic_uzunluk
son=output_syc*us_sayac2

finish=time.perf_counter()
zaman=finish-start

#dosyaya yazdırma kısmı
lzw_yazdir=open("C:/Users/windows-10/Desktop/21100011010_odev4/lzw.txt","a")
lzw_yazdir.write("Başlangıç boyutu: "+str(baslangic)+" Sıkıştırılmış Boyut: "+str(son)+" Çalışma Süresi: "+str(zaman)+"\n")
lzw_yazdir.close()




#huffman
start2=time.perf_counter()

kelime=open("C:/Users/windows-10/Desktop/21100011010_odev4/huffman_baslangic.txt","r")
kelime=kelime.read()
liste=[]
dict={}
boyut_listesi=[]
toplam=0
sayac=0
tut=""

#8 bit olarak parçaladım.
for i in kelime:
    if sayac%8==0:
        if(i==0):
            continue
        liste.append(tut)
        tut=""
        sayac+=1
    else:
        tut+=i
        sayac+=1
del liste[0]

#frekans hesaplama

for i in liste:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

toplam_frekans=0
for i in dict:
    boyut_listesi.append(dict[i])
    toplam_frekans+=int(i)

boyut_listesi.sort()

baslangic=toplam_frekans*8


son=toplam_frekans*4  #hocam bu kısmı ağaç çizmeden yaptıramadım son bulma kısmı yanlış

finish2=time.perf_counter()

zaman2=finish2-start2
huffman_yazdir=open("C:/Users/windows-10/Desktop/21100011010_odev4/huffman.txt","a")
huffman_yazdir.write("Başlangıç boyutu: "+str(baslangic)+" Sıkıştırılmış Boyut: "+str(son)+" Çalışma Süresi: "+str(zaman2)+"\n")
huffman_yazdir.close()
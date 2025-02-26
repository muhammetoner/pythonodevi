# Merhaba arkadaşlar,

# Bu hafta öğrendiğimiz değişkenler, döngüler ve fonksiyonlar konularını pekiştirmek için iki farklı problem üzerinde çalışacağız. Her iki problemi de fonksiyon kullanarak çözmelisiniz.

# 1. Asal Sayı Kontrolü

def asalami():
    sayi1 = int(input("Lütfen asal sayı olup olmadığını öğrenmek istediğiniz sayıyı giriniz: "))

    if sayi1 < 2:  
        print("Lütfen 2 veya daha büyük bir sayı giriniz.")
        return

    for i in range(2, sayi1):  
        if sayi1 % i == 0:  
            print("Sayınız asal değildir.")
            return

    print("Sayınız asaldır.")  

asalami()




# Kurallar:
#Asal sayı, sadece kendisine ve 1’e bölünebilen 1’den büyük pozitif sayılardır.
#Fonksiyon, kullanıcıdan bir sayı almalı ve asal olup olmadığını kontrol etmelidir.
#Örnek Kullanım:
#asal_mi(7)  # Çıktı: 7 bir asal sayıdır.
#asal_mi(10) # Çıktı: 10 bir asal sayı değildir.
# 2. Basit Hesap Makinesi
 
#kullanıcıdan iki sayı ve bir işlem türü alarak sonucu döndüren bir fonksiyon yazın   
#Kurallar:
#Kullanıcı +, -, *, / işlemlerinden birini seçmelidir.
#Bölme işleminde, ikinci sayı 0 olursa "Bölme işlemi için ikinci sayı 0 olamaz!" şeklinde uyarı verin.
#Kullanıcı geçersiz bir işlem girerse, "Geçersiz işlem türü!" mesajı gösterin.
# Örnek Kullanım:
#hesap_makinesi(5, 3, '+')  # Çıktı: 5 + 3 = 8
#hesap_makinesi(10, 2, '/')  # Çıktı: 10 / 2 = 5.0
#hesap_makinesi(4, 0, '/')   # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
#hesap_makinesi(6, 2, '%')   # Çıktı: Geçersiz işlem türü!
def hesapla(sayi1, sayi2):
    if islem == "+":
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == "-":
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == "x":
        return f"{sayi1} X {sayi2} = {sayi1 * sayi2}"
    elif islem == "/":
        if sayi2 == 0:
            return "Bölme işleminde ikinci sayı 0 olamaz, maalesef :("
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Üzgünüm, geçersiz işlem türü!"

islem = input("Lütfen hangi işlemi yapmak istiyorsanız seçiniz\n"
              "(+) Toplama\n(-) Çıkartma\n(x) Çarpma\n(/) Bölme\nİşlem: ")

sayi1 = int(input("Lütfen 1. sayıyı giriniz: "))
sayi2 = int(input("Lütfen 2. sayıyı giriniz: "))

sonuc = hesapla(sayi1, sayi2)
print(sonuc)


                
          
 

   


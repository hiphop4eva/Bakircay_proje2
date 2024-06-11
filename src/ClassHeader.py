#Dosya yüklenmesini denetlemek için try/except

try:
    from Classes.Personel import *
except:
    print("Personel.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
    raise Exception("Personel.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
try:
    from Classes.Doktor import *
except:
    print("Doktor.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
    raise Exception("Doktor.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
try:
    from Classes.Hemsire import *
except:
    print("Hemsire.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
    raise Exception("Hemsire.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
try:
    from Classes.Hasta import *
except:
    print("Hasta.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
    raise Exception("Hasta.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
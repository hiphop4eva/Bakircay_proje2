#Dosya ve module yüklenmesini denetlemek için try/except
try:
    from ClassHeader import *
except:
    print("ClassHeader.py dosyası yüklenemedi. Lütfen tekrar deneyin.")
    raise Exception("ClassHeader.py dosyası yüklenemedi. Lütfen tekrar deneyin.")

try:
    from pandas import DataFrame, Series
except:
    print("Pandas kütüphanesi yüklenemedi. Lütfen tekrar deneyin.")
    raise Exception("Pandas kütüphanesi yüklenemedi. Lütfen tekrar deneyin.")

#Dataframe oluşturma
mainDataFrame = DataFrame({
    "Personel No":  [],
    "Ad":           [],
    "Soyad":        [],
    "Departman":    [],
    "Maas":         [],
    "Uzmanlik":     [],
    "Deneyim Yili": [],
    "Hastane":      [],
    "Calisma Saati":[],
    "Sertifika":    [],
    "Hasta No" :    [],
    "Dogum Tarihi" :[],
    "Hastalik" :    [],
    "Tedavi" :      []
    }
)

#Gerekli objeleri oluşturma
personel1 = Personel(1, "Ahmet", "Yılmaz", "A Departman", 12000)
personel2 = Personel(2, "Mehmet", "Demir", "B Departman", 5000)

doktor1 = Doktor(3, "Ali", "Yıldırım", "A Departman", 8000, "Cerrahi", 4, "Hastane 1")
doktor2 = Doktor(4, "Veli", "Yıldırım", "B Departman", 6000, "Cerrahi", 3, "Hastane 2")
doktor3 = Doktor(5, "Ayşe", "Çelik", "C Departman", 8500, "Pedologi", 5, "Hastane 3")

hemsire1 = Hemsire(5, "Fatma", "Kutlu", "B Departman", 6000, 40, "Sertifika 1", "Hastane 2")
hemsire2 = Hemsire(6, "Murat", "Sapan", "C Departman", 4750, 38, "Sertifika 2", "Hastane 1")
hemsire3 = Hemsire(7, "Tarık", "Kuru", "B Departman", 3000, 30, "Sertifika 3", "Hastane 3")

hasta1 = Hasta(1, "Belgüm", "Kılıç", "2000/01/01", "Grip", "Hızlı Tedavi")
hasta2 = Hasta(2, "Ulvi", "Işık", "1985/07/25", "Enfeksiyon", "Dengeli Tedavi")
hasta3 = Hasta(3, "Sevda", "Bayrak", "1990/02/02", "Kanser", "Dikkatli Tedavi")

#Objelerin pandas DataFrame'e aktarılması için seri oluşturma
personelList = [
    Series({
        "Personel No":  personel1.getPersonelNo(),
        "Ad":           personel1.getAd(),
        "Soyad":        personel1.getSoyad(),
        "Departman":    personel1.getDepartman(),
        "Maas":         personel1.getMaas(),
    }),

    Series({
        "Personel No":  personel2.getPersonelNo(),
        "Ad":           personel2.getAd(),
        "Soyad":        personel2.getSoyad(),
        "Departman":    personel2.getDepartman(),
        "Maas":         personel2.getMaas(),
    })
]

doctorList = [
    Series({
        "Personel No":  doktor1.getPersonelNo(),
        "Ad":           doktor1.getAd(),
        "Soyad":        doktor1.getSoyad(),
        "Departman":    doktor1.getDepartman(),
        "Maas":         doktor1.getMaas(),
        "Uzmanlik":     doktor1.getUzmanlik(),
        "Deneyim Yili": doktor1.getDeneyimYili(),
        "Hastane":      doktor1.getHastane(),
    }),

    Series({
        "Personel No":  doktor2.getPersonelNo(),
        "Ad":           doktor2.getAd(),
        "Soyad":        doktor2.getSoyad(),
        "Departman":    doktor2.getDepartman(),
        "Maas":         doktor2.getMaas(),
        "Uzmanlik":     doktor2.getUzmanlik(),
        "Deneyim Yili": doktor2.getDeneyimYili(),
        "Hastane":      doktor2.getHastane(),
    }),

    Series({
        "Personel No":  doktor3.getPersonelNo(),
        "Ad":           doktor3.getAd(),
        "Soyad":        doktor3.getSoyad(),
        "Departman":    doktor3.getDepartman(),
        "Maas":         doktor3.getMaas(),
        "Uzmanlik":     doktor3.getUzmanlik(),
        "Deneyim Yili": doktor3.getDeneyimYili(),
        "Hastane":      doktor3.getHastane(),
    })
]

nurseList = [
    Series({
        "Personel No":  hemsire1.getPersonelNo(),
        "Ad":           hemsire1.getAd(),
        "Soyad":        hemsire1.getSoyad(),
        "Departman":    hemsire1.getDepartman(),
        "Maas":         hemsire1.getMaas(),
        "Calisma Saati": hemsire1.getCalismaSaati(),
        "Sertifika":    hemsire1.getSertifika(),
        "Hastane":      hemsire1.getHastane(),
    }),

    Series({
        "Personel No":  hemsire2.getPersonelNo(),
        "Ad":           hemsire2.getAd(),
        "Soyad":        hemsire2.getSoyad(),
        "Departman":    hemsire2.getDepartman(),
        "Maas":         hemsire2.getMaas(),
        "Calisma Saati": hemsire2.getCalismaSaati(),
        "Sertifika":    hemsire2.getSertifika(),
        "Hastane":      hemsire2.getHastane(),
    }),

    Series({
        "Personel No":  hemsire3.getPersonelNo(),
        "Ad":           hemsire3.getAd(),
        "Soyad":        hemsire3.getSoyad(),
        "Departman":    hemsire3.getDepartman(),
        "Maas":         hemsire3.getMaas(),
        "Calisma Saati": hemsire3.getCalismaSaati(),
        "Sertifika":    hemsire3.getSertifika(),
        "Hastane":      hemsire3.getHastane(),
    })
]

sicklyList = [
    Series({
        "Hasta No":  hasta1.getHastaNo(),
        "Ad":           hasta1.getAd(),
        "Soyad":        hasta1.getSoyad(),
        "Dogum Tarihi": hasta1.getDogumTarihi(),
        "Hastalik":    hasta1.getHastalik(),
        "Tedavi":      hasta1.getTedavi(),
    }),

    Series({
        "Hasta No":  hasta2.getHastaNo(),
        "Ad":           hasta2.getAd(),
        "Soyad":        hasta2.getSoyad(),
        "Dogum Tarihi": hasta2.getDogumTarihi(),
        "Hastalik":    hasta2.getHastalik(),
        "Tedavi":      hasta2.getTedavi(),
    }),

    Series({
        "Hasta No":  hasta3.getHastaNo(),
        "Ad":           hasta3.getAd(),
        "Soyad":        hasta3.getSoyad(),
        "Dogum Tarihi": hasta3.getDogumTarihi(),
        "Hastalik":    hasta3.getHastalik(),
        "Tedavi":      hasta3.getTedavi(),
    })
]

#Döngüyle serileri dataframe'e ekleme
for personel in personelList:
    mainDataFrame.loc[len(mainDataFrame)] = personel

for doctor in doctorList:
    mainDataFrame.loc[len(mainDataFrame)] = doctor

for nurse in nurseList:
    mainDataFrame.loc[len(mainDataFrame)] = nurse

for sickly in sicklyList:
    mainDataFrame.loc[len(mainDataFrame)] = sickly

#Boş verileri 0 ile dolurma ve istenilen sütunlar ile yeni dataframe oluşturma
mainDataFrame = mainDataFrame.fillna(0)
newDataFrame = mainDataFrame.get(["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastalik", "Tedavi"])

#İşlemler için gerekli değişkenleri oluşturma
rowCount = mainDataFrame.shape[0]
uzmanlikDict = {}
experiencedCount = 0
sickNameList = []
youngSickList = []

#Dataframe'in her satırını gezme
for i in range(rowCount):
    instance = mainDataFrame.iloc[i]
    uzmanlik = instance["Uzmanlik"]
    deneyim_yili = instance["Deneyim Yili"]
    name = instance["Ad"]
    sickness = instance["Hastalik"]
    salary = instance["Maas"]
    birthDate = str(instance["Dogum Tarihi"])

    #Doktorların uzmanlık alanlarını listeleme ve deneyim yılına bakma
    if uzmanlik != 0:
        if uzmanlik not in uzmanlikDict:
            uzmanlikDict[uzmanlik] = 1
        else:
            uzmanlikDict[uzmanlik] += 1
    
        if deneyim_yili > 5:
            experiencedCount += 1

    #Hasta olanları listeleme
    if name not in sickNameList and sickness != 0:
        sickNameList.append(name)

    #1990'dan önceki hastaları listeleme
    if birthDate.split("/")[0] >= "1990" and sickness != 0:
        youngSickList.append(i)

sickNameList.sort()

print(f"Uzmanlık alanları ve üye sayısı: {uzmanlikDict}")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print(f"5 yıldan daha uzun süre deneyimli doktor sayısı: {experiencedCount}")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("Hastaların alfabe sırasına göre adları:")
for name in sickNameList:
    print(mainDataFrame.loc[mainDataFrame["Ad"] == name])
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("Maaşı 7000 üzerinde olan personeller:")
print(mainDataFrame.loc[mainDataFrame["Maas"] > 7000])
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("1990'dan sonra doğan hastalar:")
print(mainDataFrame.iloc[youngSickList])
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("Yeni kayıtlar:")
print(newDataFrame)
print("----------------------------------------------------------------------------------------------------------------------------------------------")

from ClassHeader import *

from pandas import DataFrame, Series

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

personelList = [
    Series({
        "Personel No":  1,
        "Ad":           "Ahmet",
        "Soyad":        "Yılmaz",
        "Departman":    "A Departman",
        "Maas":         5000,
    }),

    Series({
        "Personel No":  2,
        "Ad":           "Mehmet",
        "Soyad":        "Demir",
        "Departman":    "B Departman",
        "Maas":         5500,
    })
]

doctorList = [
    Series({
        "Personel No":  3,
        "Ad":           "Ali",
        "Soyad":        "Yıldırım",
        "Departman":    "A Departman",
        "Maas":         8000,
        "Uzmanlik":     "Cerrahi",
        "Deneyim Yili": 4,
        "Hastane":      "Hastane 1",
    }),

    Series({
        "Personel No":  4,
        "Ad":           "Veli",
        "Soyad":        "Yıldırım",
        "Departman":    "A Departman",
        "Maas":         9000,
        "Uzmanlik":     "Cerrahi",
        "Deneyim Yili": 6,
        "Hastane":      "Hastane 3",
    }),

    Series({
        "Personel No":  5,
        "Ad":           "Ayşe",
        "Soyad":        "Çelik",
        "Departman":    "C Departman",
        "Maas":         8500,
        "Uzmanlik":     "Pedologi",
        "Deneyim Yili": 12,
        "Hastane":      "Hastane 1",
    })
]

nurseList = [
    Series({
        "Personel No":  6,
        "Ad":           "Fatma",
        "Soyad":        "Kutlu",
        "Departman":    "B Departman",
        "Maas":         6000,
        "Calisma Saati": 40,
        "Sertifika":    "Sertifika 1",
        "Hastane":      "Hastane 2",
    }),

    Series({
        "Personel No":  7,
        "Ad":           "Murat",
        "Soyad":        "Sapan",
        "Departman":    "C Departman",
        "Maas":         4750,
        "Calisma Saati": 38,
        "Sertifika":    "Sertifika 2",
        "Hastane":      "Hastane 1",
    }),

    Series({
        "Personel No":  8,
        "Ad":           "Tarık",
        "Soyad":        "Kuru",
        "Departman":    "B Departman",
        "Maas":         3000,
        "Calisma Saati": 30,
        "Sertifika":    "Sertifika 2",
        "Hastane":      "Hastane 3",
    })
]

sicklyList = [
    Series({
        "Hasta No":  1,
        "Ad":           "Belgüm",
        "Soyad":        "Kılıç",
        "Dogum Tarihi": "2000/01/01",
        "Hastalik":    "Hastalık 1",
        "Tedavi":      "Tedavi 1",
    }),

    Series({
        "Hasta No":  2,
        "Ad":           "Ulvi",
        "Soyad":        "Işık",
        "Dogum Tarihi": "1985/07/25",
        "Hastalik":    "Hastalık 2",
        "Tedavi":      "Tedavi 2",
    })
]

for personel in personelList:
    mainDataFrame.loc[len(mainDataFrame)] = personel

for doctor in doctorList:
    mainDataFrame.loc[len(mainDataFrame)] = doctor

for nurse in nurseList:
    mainDataFrame.loc[len(mainDataFrame)] = nurse

for sickly in sicklyList:
    mainDataFrame.loc[len(mainDataFrame)] = sickly

mainDataFrame = mainDataFrame.fillna(0)
newDataFrame = mainDataFrame.get(["Ad", "Soyad", "Departman", "Maas", "Uzmanlik", "Deneyim Yili", "Hastalik", "Tedavi"])

rowCount = mainDataFrame.shape[0]
uzmanlikDict = {}
experiencedCount = 0
nameList = []
youngList = []

for i in range(rowCount):
    instance = mainDataFrame.iloc[i]
    uzmanlik = instance["Uzmanlik"]
    deneyim_yili = instance["Deneyim Yili"]
    name = instance["Ad"]
    sickness = instance["Hastalik"]
    salary = instance["Maas"]
    birthDate = str(instance["Dogum Tarihi"])

    if uzmanlik != 0:
        if uzmanlik not in uzmanlikDict:
            uzmanlikDict[uzmanlik] = 1
        else:
            uzmanlikDict[uzmanlik] += 1
    
        if deneyim_yili > 5:
            experiencedCount += 1

    if name not in nameList and sickness != 0:
        nameList.append(name)

    if birthDate.split("/")[0] > "1990" and sickness != 0:
        youngList.append(i)

nameList.sort()

print(f"Uzmanlık alanları ve üye sayısı: {uzmanlikDict}")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print(f"5 yıldan daha uzun süre deneyimli doktor sayısı: {experiencedCount}")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("Hastaların alfabe sırasına göre adları:")
for name in nameList:
    print(mainDataFrame.loc[mainDataFrame["Ad"] == name])
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("Maaşı 7000 üzerinde olan personeller:")
print(mainDataFrame.loc[mainDataFrame["Maas"] > 7000])
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("1990'dan sonra doğan hastalar:")
for i in youngList:
    print(mainDataFrame.iloc[i])
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("Yeni kayıtlar:")
print(newDataFrame)
print("----------------------------------------------------------------------------------------------------------------------------------------------")

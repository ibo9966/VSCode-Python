# region kargs_giris
"""
Argüman olarak → int, float, string, tuple, list gönderebiliyorum, peki
Argüman olarak → dictionary gönderebilir miyim? Cevabı, Evet
"""
# endregion





"""def pDilleri(**kargs):
    print(type(kargs))
pDilleri(
    programlamaDili="python",
    seviye = "yüksek",
    interpterer = True,
    version = 3.10
)"""




"""
dilPython ={
    "programlamaDili" :"python",
    "seviye" : "yüksek",
    "interpterer" : True,
    "version" : 3.10
}
dilCSharp ={
    "programlamaDili" :"c#",
    "seviye" : "yüksek",
    "interpterer" : False,
    "version" : 8.0
}
def dilBilgisi(dil):
    # print(type(dil))
    print(f"{dil['programlamaDili']}\t\t{dil['seviye']}\t\t{dil['interpterer']}\t\t{dil['version']}")
print("Prg.Dili\tSeviye\t\tInterprt.\tVers.")
print("------\t\t-------\t\t-------\t\t------")
dilBilgisi(dilPython)
dilBilgisi(dilCSharp)"""





# araba = {
#     "marka":"toyota",
#     "motor":1.6,
#     "renk":"kırmızı",
#     "fiyat":1000
# }


# def satinAl(arg, musteri, butce, favListe):
#     print(f"{musteri} isimli müşteri {arg['marka']} marka araba satın almak istiyor")
#     if butce>= arg["fiyat"]:
#         print("bütçe yeterli tabiki de")
#     else:
#         print(f"bütçe yeterli değil, {arg['fiyat']-butce} TL eksik")


# satinAl(araba, "burak", 1500, ["gri", "beyaz", "siyah"])


def galeri(kargs):
    # print(f'{kargs["motor"]}\t{kargs["sasiNo"]}\t{kargs["renk"]}\t{kargs["marka"]}\t')
    print("Motor\tŞasi\tRenk\tMarka")
    print("-------\t-----\t-----\t------")
    for i in range(len(kargs)):
        print(f'{kargs[i]["motor"]}\t{kargs[i]["sasiNo"]}\t{kargs[i]["renk"]}\t{kargs[i]["marka"]}')
arabaHyndai={
"motor":1.4,
"sasiNo":"h11233",
"renk":"kırmızı",
"marka":"hyndai"

}

arabaHonda={
"motor":1.8,
"sasiNo":"ho1454",
"renk":"beyaz",
"marka":"honda"
}

arabalar=[arabaHonda,arabaHyndai]
galeri(arabalar)

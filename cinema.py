normal_bilet_fiyatı = 200
kids_bilet_fiyatı = 120
young_bilet_fiyatı = 150
old_bilet_fiyatı = 100
ek_ücret3D = 50
menu_fiyatı = 90
haftaiçi_indirimi = 20
student_indirimOranı = 0.2

mid_week = ["pazartesi", "salı", "çarşamba", "perşembe"]

name = input("Name: ")
age = int(input("age: "))
isStudent1 = input("Öğrenci misin?").lower()

isStudent = True

if isStudent1 == "hayır":
    isStudent = False

day = input("Hangi gün izleyeceksiniz?").strip().lower()

movieType = input("Film türü? ").strip().upper()

isMenu1 = input("Menü ister misiniz?:").strip().lower()
isMenu = True
if isMenu1 == "hayır.":
    isMenu = False

biletPrice = 0
ilk_bilet_fiyati = 0
StudentPrice = 0
midWeekPrice = 0
price3D = 0
menuPrice = 0
isEnter = True

if age < 7:
    print("Sinemaya giremezsiniz.")
elif age <= 12:
    biletPrice = kids_bilet_fiyatı
elif age <= 17:
    biletPrice = young_bilet_fiyatı
elif age <= 64:
    biletPrice = normal_bilet_fiyatı
else:
    biletPrice = old_bilet_fiyatı

if isEnter:
    ilk_bilet_fiyati = biletPrice

if age > 12 and isStudent:
    StudentPrice = biletPrice * 0.2
    biletPrice -= StudentPrice

if day in mid_week:
    midWeekPrice = haftaiçi_indirimi
    biletPrice -= 20

if movieType == "3D":
    price3D = ek_ücret3D
    biletPrice += ek_ücret3D

if isMenu == True:
    menuPrice = 90

total = biletPrice + menuPrice
if total < 0:
    total = 0


print("Fiş:")
print(f"\nName:{name}")
print(f"\nAge: {age}")
print(f"\nÖğrenci Durumu: {isStudent}")
print(f"\nFilm Günü: {day}")
print(f"\nFilm Türü: {movieType}")
print(f"\nİlk Bilet Fiyatı:{ilk_bilet_fiyati} ")
print(f"\nÖğrenci indirimi: {StudentPrice}")
print(f"\nHafta içi İndirimi: {midWeekPrice}")
print(f"\n3D Film Ücreti: {price3D}")
print(f"\nMenü Ücreti: {menuPrice}")
print(f"\nTotal: {total}")

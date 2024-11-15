import pandas as pd 

veri = {
    "Tarih": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
    "Ürün": ["Ürün A", "Ürün B", "Ürün C", "Ürün D"],
    "Fiyat": [100, 150, 100, 200],
    "Miktar": [5, 2, 7, 3]
}

veri = pd.DataFrame(veri)

print(veri)

veri["Tarih"] = pd.to_datetime(veri["Tarih"])
veri["Toplam_Satis"] = veri["Fiyat"] * veri["Miktar"]

toplam_satis = veri.groupby("Ürün")["Toplam_Satis"].sum().reset_index(drop = True)
print(f"\nÜrün Bazında Toplam Satışlar:\n{toplam_satis}")
print(f"\nVeri İstatistikleri: {veri.describe()}")
gunluk_satis = veri.groupby("Tarih")["Toplam_Satis"].sum()
print(f"\nGünlük Satışlar: {gunluk_satis}")

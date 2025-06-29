
print("=" *41)
print("         Konversi Satuan Berat")  
print("=" *41)

# Pengambilan Data
Nilai = float(input("Masukan Nilai: "))

print("1. Ton")
print("2. Kwintal")
print("3. Puluhan Kg")
print("4. Kilogram")
print("5. Ons")
print("6. Gram")
print("7. Miligram")
Awal = input("Masukan Nomor Yang Mewakili Satuan Awal: ")
if Awal not in ('1','2','3','4','5','6','7'):
    print("Nomor Tidak Valid")
    exit()
else:
    print("Kamu Memilih Satuan", Awal)

print("1. Ton")
print("2. Kwintal")
print("3. Puluhan Kg")
print("4. Kilogram")
print("5. Ons")
print("6. Gram")
print("7. Miligram")
Tujuan = input("Masukan Nomor Yang Mewakili Satuan Tujuan: ")
if Tujuan not in ('1','2','3','4','5','6','7'):
    print("Nomor Tidak Valid")
    exit()
else:
    print("Kamu Memilih Satuan", Tujuan)

Konversi = {
    '1': 1000,
    '2': 100,
    '3': 10,
    '4': 1,
    '5': 0.1,
    '6': 0.001,
    '7': 0.000001
}

print("=" *41)
print("         Konversi Satuan Berat")  
print("=" *41)   

# Hasil 
Hasil = Nilai * Konversi[Awal] / Konversi[Tujuan]
print(f"Hasil Konversi: {Nilai} Dari Satuan {Awal} = {Hasil} Ke Satuan {Tujuan}")

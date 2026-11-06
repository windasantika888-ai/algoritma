# 1. Mulai Program
print("=================================")
print("  APLIKASI KASIR RESTORAN")
print("=================================")
total = 0
pesanan = []  # buat nyimpen pesanan

# Daftar menu pakai list, biar bisa di-loop pakai for
menu = [
    ("Nasi Goreng", 25000),
    ("Mie Ayam", 15000),
    ("Ayam Geprek", 20000),
    ("Sate Ayam", 30000),
    ("Bakso", 18000),
]

# 3. Proses Pemesanan - Perulangan WHILE
while True:
    # 2. Tampilkan Menu - Perulangan FOR
    print("\n--- MENU MAKANAN ---")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i][0]} - Rp{menu[i][1]}")
    print("0. Selesai Memilih")

    pilihan = int(input("Pilih menu (0-5): "))

    # 4. Apakah Pilihan 0?
    if pilihan == 0:
        break

    if pilihan < 1 or pilihan > 5:
        print("Pilihan tidak ada, coba lagi!")
        continue

    jumlah = int(input(f"Masukkan jumlah {menu[pilihan-1][0]}: "))
    subtotal = menu[pilihan-1][1] * jumlah
    total += subtotal

    # Simpan ke list pesanan
    pesanan.append((menu[pilihan-1][0], menu[pilihan-1][1], jumlah, subtotal))
    print(f"Subtotal: {menu[pilihan-1][0]} x {jumlah} = Rp{subtotal}")

# 5. Hitung Diskon
if total > 200000:
    persen_diskon = 20
    potongan = total * 0.20
else:
    persen_diskon = 0
    potongan = 0

total_bayar = total - potongan

# 6. Tampilkan Struk - Perulangan FOR lagi
print("\n===== STRUK PEMBAYARAN =====")
print("Rincian Pesanan:")
for nama, harga, jumlah, subtotal in pesanan:
    print(f"- {nama} x {jumlah} = Rp{subtotal}")

print("------------------------------")
print(f"Total Belanja : Rp {total}")
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : Rp {int(potongan)}")
print(f"Total Bayar   : Rp {int(total_bayar)}")
print("------------------------------")
print("Terima Kasih")
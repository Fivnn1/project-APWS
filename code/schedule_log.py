import datetime

data_jadwal = []

file_log = "logs/log_penyiraman.csv"

durasi_maksimum = 60
daftar_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
opsi_pemicu = ["OTOMATIS", "MANUAL", "TERJADWAL"]


# ===================== PENJADWALAN =====================

# Fungsi untuk memvalidasi input jadwal
def validasi_jadwal(hari, jam, durasi):
    if hari != "harian" and hari not in daftar_hari:
        return False, "Hari tidak valid Isi 'harian' atau satu nama hari (contoh: senin)"
    if len(jam) != 5 or jam[2] != ":" or not jam[:2].isdigit() or not jam[3:].isdigit():
        return False, "Format jam tidak valid Gunakan HH:MM (contoh: 06:00)"
    if int(jam[:2]) > 23 or int(jam[3:]) > 59:
        return False, "Jam tidak valid Jam 00-23 dan menit 00-59"
    if durasi < 1 or durasi > durasi_maksimum:
        return False, f"Durasi harus 1 - {durasi_maksimum} detik"
    return True, "Jadwal valid"

# Fungsi untuk menambah jadwal
def tambah_jadwal(hari, jam, durasi):
    valid, pesan = validasi_jadwal(hari, jam, durasi)
    if not valid:
        print(pesan)
        return
    data_jadwal.append({"hari": hari, "jam": jam, "durasi": durasi})
    print("Jadwal berhasil ditambahkan")

# Fungsi untuk menampilkan semua jadwal
def tampilkan_jadwal():
    print("===Daftar Jadwal===")
    if len(data_jadwal) == 0:
        print("Belum ada jadwal")
        return
    for i in range(len(data_jadwal)):
        jadwal = data_jadwal[i]
        print(f"{i + 1}. {jadwal['hari']} | {jadwal['jam']} | {jadwal['durasi']} detik")

# Fungsi untuk membaca semua riwayat dari file
def baca_log():
    daftar_log = []
    try:
        file = open(file_log, "r")
        for baris in file:
            baris = baris.strip()
            if baris != "":
                daftar_log.append(baris.split(","))
        file.close()
    except FileNotFoundError:
        pass  # file belum ada = belum ada riwayat
    return daftar_log
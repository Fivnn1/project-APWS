import random
import datetime

# Ambang batas pembacaan data sensor
rentang_kelembapan_tanah = (0, 100)
rentang_suhu = (10.0, 50.0)
rentang_kelembapan_udara = (0, 100)
opsi_level_air = ["CUKUP", "KURANG"]

def validasi_data_sensor(kelembapan_tanah, suhu, kelembapan_udara, level_air):
    if not rentang_kelembapan_tanah[0] <= kelembapan_tanah <= rentang_kelembapan_tanah[1]:
        return False, "Input data kelembapan tanah tidak valid!"
    if not rentang_suhu[0] <= suhu <= rentang_suhu[1]:
        return False, "Input suhu diluar batas kemampuan pembacaan!"
    if not rentang_kelembapan_udara[0] <= kelembapan_udara <= rentang_kelembapan_udara[1]:
        return False, "Input data kelembapan udara tidak valid!"
    if level_air.upper() not in opsi_level_air:
        return False, 'Status level air harus bernilai "CUKUP" atau "KURANG"!'
    return True, "Data sensor valid"

def baca_sensor_otomatis():
    """
    Menghasilkan simulasi data pembacaan sensor lingkungan secara berkala.
    Menggunakan modul bawaan random untuk memodelkan sensor IoT.
    """
    kelembapan_tanah = random.randint(20, 85)
    suhu = round(random.uniform(23.0, 34.0), 1)
    kelembapan_udara = random.randint(45, 90)
    # Probabilitas tandon CUKUP lebih tinggi daripada RENDAH
    level_air = random.choice(["CUKUP", "CUKUP", "CUKUP", "RENDAH"])

    return {
        "kelembapan_tanah": kelembapan_tanah,
        "suhu": suhu,
        "kelembapan_udara": kelembapan_udara,
        "level_air": level_air,
        "waktu_baca": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
def tampilkan_dashboard(data, status_pompa=False, ambang_min=40, ambang_maks=70):
    """
    Prosedur antarmuka CLI untuk menampilkan status pemantauan sensor
    sesuai kebutuhan SKPL-F-004.
    """
    if data is None:
        print("[PERINGATAN]: Tidak ada data sensor untuk ditampilkan.")
        return

    kondisi_tanah = format_status_tanah(data["kelembapan_tanah"], ambang_min, ambang_maks)
    kondisi_pompa = "MENYALA [ON]" if status_pompa else "MATI [OFF]"

    print("\n" + "=" * 55)
    print("        APWS MONITORING DASHBOARD (CLI VERSION)        ")
    print("=" * 55)
    print(f" Waktu Pembacaan  : {data['waktu_baca']}")
    print("-" * 55)
    print(f" Kelembapan Tanah : {data['kelembapan_tanah']}% -> {kondisi_tanah}")
    print(f" Suhu Lingkungan  : {data['suhu']} °C")
    print(f" Kelembapan Udara : {data['kelembapan_udara']}%")
    print(f" Level Air Tandon : {data['level_air']}")
    print(f" Status Pompa Air : {kondisi_pompa}")
    print("-" * 55)

    # Notifikasi langsung jika tandon air berada pada kondisi kritis
    if data["level_air"] == "RENDAH":
        print(" [PERINGATAN]: Level air tandon RENDAH! Isi ulang tandon air.")
    print("=" * 55)    
    
if __name__ == "__main__":
    print(">>> MULAI UJI COBA MODUL SENSOR MONITOR <<<\n")

    # TEST 1: Cek Simulasi Pembacaan Otomatis
    print("[TEST 1]: Membaca sensor otomatis & menampilkan dashboard")
    data_sensor = baca_sensor_otomatis()
    tampilkan_dashboard(data_sensor, status_pompa=False)

    print("\n" + "-" * 55 + "\n")

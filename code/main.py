import subprocess
import sys

import datetime

from sensor_monitor import simulasi_data, validasi_data_sensor


def tampilkanBanner():
    print("======================| Menu |======================\n")

    print("""Selamat Datang di Aplikasi Penyiram Tanaman Otomatis

    Pilih menu :
    1. Watering Control
    2. Sensor Monitor
    3. Schedule Log
    0. Keluar""")

    print("======================| APWS |======================\n")

def inputMenu():
    pilih = input("Masukkan Nomor Menu (1/2/3/0) : ")
    if(pilih == '1'):
        print("Watering Control Menu")
    elif(pilih == '2'):
        print("Sensor Monitor")
    elif(pilih == '3'):
        print("Schedule Log")
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Jalankan simulasi dari sensor.py
        t, s, u, a = simulasi_data()

        # 2. Masukkan hasil simulasi ke fungsi validasi dari sensor.py
        pesan = validasi_data_sensor(t, s, u, a)

        # 3. Tampilkan output ke terminal
        print(f"[{waktu}] Data Sensor -> Tanah: {t}%, Suhu: {s}°C, Udara: {u}%, Air: {a}")
        print(f"Status Validasi: {pesan}")
    elif pilih == "0":
        print("Keluar Aplikasi APWS")
        return False
    else:
        print("input tidak valid, silahkan masukkan 1, 2, 3 atau 0")
    
    return True

if __name__ == "__main__":
    while True:
        tampilkanBanner()
        lanjut = inputMenu()

        if not lanjut:
            break

        input("\nTekan Enter untuk kembali ke Menu Utama...")
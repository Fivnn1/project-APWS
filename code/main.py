import subprocess
import sys

from sensor_monitor import simulasi_data, validasi_data_sensor

print("======================| Menu |======================\n")

print("""Selamat Datang di Aplikasi Penyiram Tanaman Otomatis

Pilih menu :
1. Watering Control
2. Sensor Monitor
3. Schedule Log""")

print("======================| APWS |======================\n")

def inputMenu():
    pilih = input("Masukkan Nomor Menu (1/2/3) : ")
    if(pilih == '1'):
        print("Watering Control Menu")
        # subprocess.run([sys.executable, ""])
    elif(pilih == '2'):
        print("Sensor Monitor")
        subprocess.run([sys.executable, "code/sensor_monitor.py"])
    elif(pilih == '3'):
        print("Schedule Log")
        subprocess.run([sys.executable, "code/schedule_log.py"])
        
    else:
        print("input tidak valid")

inputMenu()
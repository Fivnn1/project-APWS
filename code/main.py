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
    elif(pilih == '2'):
        print("Sensor Monitor")
    elif(pilih == '3'):
        print("Schedule Log")
    else:
        print("input tidak valid")
        inputMenu()
        
inputMenu()
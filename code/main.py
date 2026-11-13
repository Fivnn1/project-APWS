import datetime
import auth_device

from sensor_monitor import simulasi_data, validasi_data_sensor


def tampilkanBanner():
    print("======================| Menu |======================\n")

    print("""Selamat Datang di Aplikasi Penyiram Tanaman Otomatis

    Pilih menu :
    1. Watering Control
    2. Sensor Monitor
    3. Schedule Log
    0. Keluar""")

    print("\n======================| APWS |======================\n")

def inputMenu():
    pilih = input("Masukkan Nomor Menu (1/2/3/0) : ")


    if(pilih == '1'):
        print("Watering Control Menu")



    elif(pilih == '2'):
        print("Schedule Log")


    
    elif(pilih == '3'):
        print("Sensor Monitor")
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Jalankan simulasi dari sensor.py
        t, s, u, a = simulasi_data()

        # 2. Masukkan hasil simulasi ke fungsi validasi dari sensor.py
        pesan = validasi_data_sensor(t, s, u, a)

        # 3. Tampilkan output ke terminal
        print(f"[{waktu}] \nData Sensor -> Tanah: {t}%, \nSuhu: {s}°C, \nUdara: {u}%, \nAir: {a}")
        print(f"Status Validasi: {pesan}")


    
    elif pilih == "0":
        print("Keluar Aplikasi APWS")

        auth_device.login()

        return False
       

    
    else:
        print("input tidak valid, silahkan masukkan 1, 2, 3 atau 0")
    
    return True



if __name__ == "__main__":
    while True:

        status_login = auth_device.login()

        if status_login:

            tampilkanBanner()
            lanjut = inputMenu()

            if not lanjut:
                break

            input("\nTekan Enter untuk kembali ke Menu Utama...")

        else:
            print("Aplikasi dimatikan. Sampai jumpa!")
            break
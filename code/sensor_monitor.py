import random
import datetime

# Ambang batas pembacaan data sensor
rentang_kelembapan_tanah = (0, 100)
rentang_suhu = (10.0, 50.0)
rentang_kelembapan_udara = (0, 100)
opsi_level_air = ["CUKUP", "KURANG"]

# Fungsi untuk memvalidasi data yang didapat dari sensor
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

# Fungsi untuk membuat simulasi data
def simulasi_data():
    # Untuk membuat nilai random
    tanah = random.randint(0, 100)
    # suhu = random.randuniform(10.0, 50.0)
    # " ini salah nulis fungsi? "

    suhu = random.uniform(10.0, 50.0)
    udara = random.randint(0, 100)
    # menambahkan [] karena banyak argumen
    air = random.choice(["CUKUP", "CUKUP", "CUKUP", "KURANG"])

    # menambahkan return agar bisa mengembalikan nilai
    return tanah, suhu, udara, air

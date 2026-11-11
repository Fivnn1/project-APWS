import hashlib

data_pengguna = {}
# tempat menyimpan data
def hash_password(kata_sandi):
  return hashlib.sha256(kata_sandi.encode()).hexdigest()
# fungsi untuk melakukan registrasi pengguna
def registrasi():
  while True:
    print("===Registrasi===")
    email = input("Masukkan Email : ")
    kata_sandi = input("Masukkan Kata Sandi : ")
    if email in data_pengguna:
      print("Email sudah terdaftar")
      return
    if "@gmail.com" not in email:
      print("Email tidak valid (harus menggunakan @gmail.com)")
      return
    if len(kata_sandi) <= 6:
      print("Kata sandi minimal 6 karakter")
      return
    password = hash_password(kata_sandi)
    data_pengguna[email] = password
    print("Registrasi berhasil silahkan login")
    print("Data pengguna:", data_pengguna)
    print("Kata sandi yang di-hash:", password)
    break
# fungsi untuk melakukan login pengguna
def login():
  while True:
    print("===Login===")
    email = input("Masukkan email : ")
    kata_sandi = input("Masukkan kata sandi : ")
    if email in data_pengguna:
      password = hash_password(kata_sandi)
      if data_pengguna[email] == password:
        print("Login berhasil ! ")
        break
      else:
        print("Kata sandi salah")
    if email not in data_pengguna or "@gmail.com" not in email:
        print("Email tidak terdaftar/tidak valid")
    if len(kata_sandi) < 6:
        print("Kata sandi minimal 6 karakter")
        

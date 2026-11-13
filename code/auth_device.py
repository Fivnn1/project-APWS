import hashlib

data_pengguna = {}
# tempat menyimpan data
def hash_password(kata_sandi):
  return hashlib.sha256(kata_sandi.encode()).hexdigest()
# fungsi untuk melakukan registrasi pengguna
def registrasi():
  print("===Registrasi===")
  email = input("Masukkan Email : ").strip()
  kata_sandi = input("Masukkan Kata Sandi : ")

  if "@" not in email or "." not in email: #menambahkan cek .
    print("Email tidak valid")
    return
  
  if email in data_pengguna:
    print("Email sudah terdaftar")
    return
  
  if len(kata_sandi) < 6:
    print("Kata sandi minimal 6 karakter")
    return
  
  password = hash_password(kata_sandi)
  data_pengguna[email] = password

  print("Registrasi berhasil silahkan login")
  print("Data pengguna:", data_pengguna)
  print("Kata sandi yang di-hash:", password)
  
# fungsi untuk melakukan login pengguna
def login():
  print("===Login===")
  email = input("Masukkan email : ").strip()
  kata_sandi = input("Masukkan kata sandi : ")
  # if email in data_pengguna:
  #   password = hash_password(kata_sandi)
  #   if data_pengguna[email] == password:
  #     print("Login berhasil ! ")
      
  #   else:
  #     print("Kata sandi salah")
  # if email not in data_pengguna or "@" not in email:
  #     print("Email tidak terdaftar/tidak valid")
  # if len(kata_sandi) < 6:
  #     print("Kata sandi minimal 6 karakter")

  if email not in data_pengguna:
    print("Gagal, email tidak terdaftar!")
    return False

  password_hash = hash_password(kata_sandi)
  if data_pengguna[email] == password_hash:
    print("Login berhasil!")
    return True
  else:
    print("Gagal, kata sandi salah!")
    return False

def auth_menu():
  while True:
    print("================| Autentikasi APWS |===============\n")
    
    print("""Pilih menu :
    1. Login
    2. Registrasi
    0. Keluar Aplikasi""")

    print("\n====================================================\n")

    pilih = input("Pilih menu (1/2/0) : ").strip()

    if pilih == "1":
      if login():
        return True
    elif pilih == "2":
      registrasi()
    elif pilih == "0":
      return False
    else:
        print("Pilihan tidak valid, silahkan masukkan 1, 2 atau 0")

  
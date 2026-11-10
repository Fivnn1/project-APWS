import hashlib

data_pengguna = {}
# tempat menyimpan data
def hash_password(kata_sandi):
  return hashlib.sha256(kata_sandi.encode()).hexdigest
  
def registrasi():
  print("===Registasi===")
  email = input("Masukkan Email :")
  kata_sandi = input("Masukkan Kata Sandi :")
  if email in data_pengguna:
    print("Email sudah terdaftar")
    return
  if "@" not in email:
    print("Email tidak valid")
    return
  if len(kata_sandi) < 6:
    print("Kata sandi minimal 6 karakter")
    return
  data_pengguna[email] = hash_password(kata_sandi)
  print("Registrasi berhasil silahkan login")
registrasi()

import hashlib

data_pengguna = {}
# tempat menyimpan data
def password(password):
  return hashlib.sha256(password.encode()).hexdigest
  
def registrasi():
  print("===Registasi===")
  email = input("Masukkan Email :")
  if email in data_pengguna:
    print("Email sudah terdaftar")
    return
  if "@" not in email:
    print("Email tidak valid")
    return
  if len(password) < 6:
    print("Kata sandi minimal 6 karakter")
    return
  data_penggguna[email] = hash_password(password)
  print("Registrasi berhasil silahkan login")

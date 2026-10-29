# 🌿 project-APWS (Automatic Plant Watering System) - CLI Simulation

Program simulasi berbasis baris perintah (**Command Line Interface / CLI**) untuk sistem penyiraman tanaman otomatis (_Automatic Plant Watering System_)[cite: 6, 12]. Sistem ini memantau parameter kelembapan tanah, suhu udara, serta level air tandon secara berkala, dan mengotomatisasi pengairan dengan logika proteksi pengaman (_failsafe_)[cite: 12, 19, 20, 23].

Proyek ini dikembangkan mengacu pada dokumen **Spesifikasi Kebutuhan Perangkat Lunak (SKPL) APWS Revisi 1.0.0**.

---

## 📌 Fitur Utama

- **Pemantauan Kondisi Sensor:** Membaca data kelembapan tanah, suhu dan kelembapan udara, serta status ketersediaan air pada tandon[cite: 19].
- **Penyiraman Otomatis Berbasis Ambang Batas:** Pompa menyala otomatis ketika kelembapan tanah berada di bawah nilai minimum dan berhenti saat mencapai batas maksimum yang ditentukan[cite: 19].
- **Sistem Pengaman (Failsafe Protection):**
  - Pembatasan durasi penyiraman maksimal (default 60 detik) untuk mencegah pengairan berlebih (_over-watering_)[cite: 19].
  - Pencegahan pompa menyala jika air pada tandon berstatus rendah guna mencegah pompa berjalan kering (_dry-run protection_)[cite: 20, 23].
- **Penyiraman Manual & Kendali Operasi:** Eksekusi penyiraman manual ("Siram Sekarang") dengan durasi kustom serta opsi penghentian kapan saja[cite: 20, 21].
- **Pencatatan Riwayat (Logging):** Mencatat setiap aktivitas penyiraman secara rinci (waktu, durasi, pemicu otomatis/manual, kondisi kelembapan sebelum dan sesudah)[cite: 20].

---

## 🛠️ Komponen & Parameter Sistem

| Parameter / Komponen            | Peran dalam Simulasi                                       | Acuan SKPL               |
| :------------------------------ | :--------------------------------------------------------- | :----------------------- |
| **Sensor Kelembapan Tanah**     | Mengukur persentase kadar air tanah (0–100%)               | SKPL-F-001[cite: 19]     |
| **Sensor Suhu & Udara (DHT22)** | Mengukur suhu (°C) dan kelembapan udara (%)                | SKPL-F-002[cite: 19]     |
| **Sensor Level Air**            | Mendeteksi ketersediaan volume air tandon (Cukup/Rendah)   | SKPL-F-003[cite: 19]     |
| **Relay & Pompa Air**           | Mengendalikan status aliran air (Aktif / Nonaktif)         | SKPL-F-007[cite: 14, 19] |
| **Ambang Batas (Threshold)**    | Nilai acuan aktivasi otomatis (Default: Min 40%, Maks 70%) | SKPL-F-006[cite: 19, 20] |

---

## 💻 Tech Stack

- **Bahasa Pemrograman:** Python 3.15.1
- **Antarmuka:** Command Line Interface (CLI / Terminal Interaktif)
- **Format Penyimpanan Log:** CSV
- **Simulasi Perangkat Keras:** Wokwi Simulator
- **Version Control:** Git & GitHub

---

## 📂 Struktur Repositori

```text
project-APWS/
├── src/                  # Kode sumber modul simulasi
│   ├── __init__.py
│   ├── sensor.py         # Logika simulasi & pembacaan sensor tanah/air/suhu
│   ├── controller.py     # Logika ambang batas, kontrol pompa, & proteksi failsafe
│   └── storage.py        # Pengelolaan pencatatan log riwayat penyiraman
├── docs/                 # Dokumentasi proyek
│   ├── diagram.json      # Konfigurasi skema sirkuit simulator Wokwi
│   └── SKPL-APWS.pdf     # Dokumen Spesifikasi Kebutuhan Perangkat Lunak
├── logs/                 # Direktori penyimpanan file log
│   └── .gitkeep
├── .gitignore            # Daftar file yang diabaikan oleh Git
├── requirements.txt      # Dependensi modul pendukung Python
├── main.py               # Program utama / entry-point menu interaktif CLI
└── README.md             # Dokumentasi utama repositori
```

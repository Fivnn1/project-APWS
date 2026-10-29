# 🌿 project-APWS (Automatic Plant Watering System)

Sistem penyiraman tanaman otomatis berbasis IoT (_Internet of Things_) yang memantau kelembaban tanah secara _real-time_ dan mengotomatisasi pengairan tanaman untuk menjaga kondisi tanah tetap optimal[cite: 1].

---

## 📌 Fitur Utama

- **Otomatisasi Penyiraman:** Pompa air menyala secara otomatis ketika kelembaban tanah berada di bawah batas ambang (_threshold_).
- **Monitoring Real-Time:** Pantau kondisi parameter kelembaban tanah dan status pompa dari jarak jauh melalui dashboard web / aplikasi IoT.
- **Mode Manual & Otomatis:** Kendali fleksibel untuk menyiram tanaman secara manual maupun terjadwal/otomatis.
- **Pencatatan Data (Logging):** Menyimpan riwayat pembacaan sensor dan aktivitas pengairan untuk evaluasi berkala.

---

## 🛠️ Komponen & Perangkat Keras

| Perangkat / Komponen                            | Fungsi                                                             |
| :---------------------------------------------- | :----------------------------------------------------------------- |
| **Microcontroller (ESP32)**                     | Otak pemrosesan data sensor, logika kendali, dan konektivitas WiFi |
| **Capacitive / Resistive Soil Moisture Sensor** | Mengukur tingkat kelembaban tanah                                  |
| **Relay Module (1/2 Channel)**                  | Saklar digital kendali daya pompa air                              |
| **Pompa Air DC (Mini Diaphragm Pump 12V / 5V)** | Mengalirkan air menuju pot/tanah                                   |
| **Catu Daya / Power Supply**                    | Sumber tegangan untuk mikrokontroler dan pompa                     |
| **Selang & Nozzle Dripper**                     | Jalur distribusi air ke titik tanaman                              |

---

## 💻 Tech Stack & Library

- **Firmware:** MicroPython
- **Dashboard / Visualisasi:** Blynk IoT
- **Bahasa Pemrograman:** Python
- **Version Control:** Git & GitHub

---

## 📂 Struktur Repositori

```text
project-APWS/
├── firmware/             # Kode program mikrokontroler (ESP32 / MicroPython)
│   ├── main.py           # Program utama
│   └── boot.py           # Inisialisasi koneksi WiFi
├── dashboard/            # Kode web dashboard / antarmuka visualisasi
│   └── app.py            # Aplikasi Streamlit / monitoring
├── docs/                 # Skema sirkuit, diagram pengkabelan, dan dokumentasi
├── .gitignore            # Daftar file yang diabaikan oleh Git
├── requirements.txt      # Dependensi pustaka Python
└── README.md             # Dokumentasi utama proyek
```


## 📄 CTF-Flag-Automation-On-The-AD-Platform

**CTF-Flag-Automation-On-The-AD-Platform** adalah sebuah proyek Python yang dirancang untuk **mengotomatiskan proses eksploitasi dan pengiriman flag pada platform AD CTF**. Dengan menggunakan sistem ini, peserta CTF tidak perlu lagi mengirimkan flag secara manual — cukup buat skrip eksploitasi, jalankan, dan sistem akan secara otomatis mengirimkan flag yang berhasil diperoleh ke server CTF.

Proyek ini cocok digunakan untuk mempercepat penyelesaian challenge dalam kompetisi CTF (Capture The Flag), terutama ketika berhadapan dengan banyak tantangan dalam waktu terbatas.

---

## ⚙️ Kebutuhan

Sebelum menggunakan proyek ini, pastikan Anda telah menginstal:

* Python 3 dengan pip
* Library Python berikut:

  * `requests`
  * `python-dotenv`
  * `flask`

Instalasi dapat dilakukan melalui:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Penggunaan

1. **Clone repositori ini**

   ```bash
   git clone https://github.com/Fauzan-Aldi/CTF-Flag-Automation-On-The-AD-Platform.git
   cd CTF-Flag-Automation-On-The-AD-Platform
   ```

2. **Instal seluruh dependensi**

   ```bash
   pip install -r requirements.txt
   ```

3. **Buat file konfigurasi `.env`**

   ```bash
   cp .env.example .env
   ```

   Lalu sesuaikan isi file `.env` dengan token dan URL dari platform AD CTF.

4. **Jalankan server lokal**

   ```bash
   python3 server.py
   ```

5. **Buat file eksploitasi dari template**

   ```bash
   cp template.py exploit-<chall_id>.py
   ```

6. **Edit file `exploit-<chall_id>.py` sesuai tantangan**

   * Isi `CHALL_ID` dengan ID challenge
   * Isi `CHALL_PORT` dengan port challenge
   * Tulis fungsi `exploit()` untuk mengeksekusi serangan
   * Pastikan memanggil `tick()` agar flag dikirim otomatis

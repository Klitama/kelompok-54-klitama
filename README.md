# Klitama 🩺

**Klitama** adalah aplikasi berbasis Django yang dikembangkan untuk mendukung layanan kesehatan digital.  

Aplikasi ini memungkinkan pengguna untuk:

- Melakukan **reservasi layanan klinik**
- Membaca **artikel kesehatan**
- Login sebagai **pasien**, **dokter**, atau **admin**

---

## 🚀 Cara Menjalankan Aplikasi

### ✅ 1. Jalankan Secara Manual (tanpa Docker)

#### 📦 Persyaratan
- Python 3.11+
- PostgreSQL (lokal atau remote)
- Virtual Environment (opsional, tapi disarankan)

#### ⚙️ Langkah

```bash
# Install dependencies
pip install -r requirements.txt

# Buat file .env (lihat bagian konfigurasi .env)
cp .env.example .env

# Jalankan migrasi database
python manage.py migrate

# Jalankan server
python manage.py runserver
```

### ✅ 2. Jalankan dengan Docker Compose (recommended)

#### 📦 Persyaratan
- Docker
- Docker Compose

#### ⚙️ Langkah

```bash
# Jalankan seluruh service (Django + PostgreSQL)
docker-compose up --build

# Untuk menghentikan 
docker-compose down
```

## 🔐 Konfigurasi .env
Berikut contoh isi file .env yang digunakan baik untuk mode manual maupun docker:

```bash
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=klitama
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

> ⚠️ Jika dijalankan tanpa Docker Compose (manual), ubah `DB_HOST=db` menjadi `DB_HOST=localhost`.
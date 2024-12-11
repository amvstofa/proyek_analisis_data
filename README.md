# Setup Environment - Shell/Terminal

mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell

# Run steamlit app

streamlit run dashboard.py

# RFM Analysis Dashboard

Aplikasi ini dirancang untuk menganalisis data produk menggunakan pendekatan **RFM Analysis** (Recency, Frequency, Monetary). Analisis ini memberikan wawasan penting untuk pengelompokan data berdasarkan pola frekuensi, nilai moneter, dan keterkinian data.

---

## Navigasi

Aplikasi ini terdiri dari tiga bagian utama:

1. **Dataset Overview**: Memberikan gambaran awal tentang dataset, termasuk jumlah data, kolom, missing values, dan duplikasi.
2. **RFM Analysis**: Menghitung dan menampilkan metrik RFM melalui tabel dan visualisasi interaktif.
3. **Kesimpulan**: Menyajikan poin-poin penting yang dapat diambil dari analisis data.

---

## 1. Dataset Overview

Bagian ini memberikan ringkasan data, meliputi:

- **Tabel Data**: 5 baris pertama dataset.
- **Informasi Kolom**: Tipe data, jumlah missing values, dan duplikasi.

### Output:

- **Informasi Dataset**:
  - Jumlah baris dan kolom.
  - Jumlah missing values per kolom.
  - Jumlah data duplikasi.

---

## 2. RFM Analysis

Bagian ini menghitung tiga metrik utama:

- **Recency**: Simulasi peringkat berdasarkan kategori yang paling sering muncul.
- **Frequency**: Jumlah produk pada setiap kategori.
- **Monetary**: Rata-rata berat produk per kategori.

### Visualisasi:

1. **Frequency Bar Chart**:
   Menampilkan jumlah produk pada setiap kategori dalam bentuk bar chart.
2. **Monetary Bar Chart**:
   Memvisualisasikan rata-rata berat produk untuk setiap kategori.
3. **Scatter Plot (RFM Metrics)**:
   Menggambarkan hubungan antara Frequency, Monetary, dan Recency.

---

## 3. Kesimpulan

### Poin Penting:

1. **Frequency**:
   - Kategori dengan jumlah produk tertinggi dapat menjadi prioritas dalam strategi pemasaran.
2. **Monetary**:
   - Rata-rata berat produk memberikan wawasan logistik, seperti kebutuhan pengemasan dan pengiriman.
3. **Recency**:
   - Mengidentifikasi kategori produk yang baru-baru ini memiliki frekuensi tinggi, untuk fokus pada ketersediaan.

---

**Aplikasi ini membantu dalam memahami pola data produk dan mendukung pengambilan keputusan yang lebih strategis.**

import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Konfigurasi halaman
st.set_page_config(page_title="RFM Analysis on Product Data", layout="wide")

# Header
st.title("Dashboard :bar_chart:")
st.markdown("""
Aplikasi ini melakukan analisis RFM menggunakan data produk.
""")

# Mendapatkan path absolut untuk folder root
BASE_DIR = Path(__file__).resolve().parent.parent

# Memuat dataset
@st.cache_data
def load_data():
    data_path = BASE_DIR / "data" / "products_dataset.csv"
    data = pd.read_csv(data_path)
    data.dropna(subset=['product_category_name'], inplace=True)
    return data

products_dt = load_data()

gambar_path = BASE_DIR / "gambar" / "data_science2.png"
# Menampilkan gambar di sidebar
st.sidebar.image(str(gambar_path), width=200)

# Sidebar untuk navigasi menu
st.sidebar.title("Menu Navigasi")
menu = st.sidebar.selectbox(
    "Pilih Analisis:",
    ["Dataset Overview", "RFM Analysis", "Kesimpulan"]
)

# Dataset Overview
if menu == "Dataset Overview":
    st.header("Dataset Overview :open_book:")
    st.write("5 Baris Pertama Dataset:")
    st.dataframe(products_dt.head())

    st.write("Informasi Dataset:")
    st.write(products_dt.info())

    st.write("Jumlah Missing Values:")
    st.write(products_dt.isna().sum())

    st.write("Jumlah Duplikasi:")
    st.write(products_dt.duplicated().sum())

# RFM Analysis
elif menu == "RFM Analysis":
    st.header("RFM Analysis :green_book:")
    st.write("Menghitung metrik RFM berdasarkan data produk")

    # Frequency: Jumlah produk per kategori
    category_frequency = products_dt['product_category_name'].value_counts().reset_index()
    category_frequency.columns = ['product_category_name', 'frequency']

    # Monetary: Rata-rata berat produk per kategori
    category_monetary = products_dt.groupby('product_category_name')['product_weight_g'].mean().reset_index()
    category_monetary.columns = ['product_category_name', 'monetary']

    # Gabungkan Frequency dan Monetary
    rfm_table = pd.merge(category_frequency, category_monetary, on='product_category_name')

    # Recency: Urutkan kategori berdasarkan frekuensi (simulasi urutan 'recency')
    rfm_table['recency'] = rfm_table['frequency'].rank(ascending=False)

    # Tampilkan tabel RFM
    st.write("Tabel RFM:")
    st.dataframe(rfm_table)

    # Visualisasi RFM
    # Frequency Bar Chart
    st.subheader("Frequency: Jumlah Produk per Kategori")
    fig_frequency = px.bar(
        rfm_table,
        x='product_category_name',
        y='frequency',
        title='Frequency: Jumlah Produk per Kategori',
        labels={'product_category_name': 'Kategori Produk', 'frequency': 'Jumlah Produk'},
        color='product_category_name',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_frequency.update_layout(xaxis_tickangle=-45, title_x=0.5)
    st.plotly_chart(fig_frequency)

    # Monetary Bar Chart
    st.subheader("Monetary: Rata-rata Berat per Kategori")
    fig_monetary = px.bar(
        rfm_table,
        x='product_category_name',
        y='monetary',
        title='Monetary: Rata-rata Berat Produk per Kategori',
        labels={'product_category_name': 'Kategori Produk', 'monetary': 'Rata-rata Berat (gram)'},
        color='product_category_name',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_monetary.update_layout(xaxis_tickangle=-45, title_x=0.5)
    st.plotly_chart(fig_monetary)

    # Scatter Plot untuk Recency, Frequency, Monetary
    st.subheader("Scatter Plot: RFM Metrics")
    fig_rfm = px.scatter(
        rfm_table,
        x='frequency',
        y='monetary',
        size='recency',
        color='product_category_name',
        title='RFM Scatter Plot',
        labels={
            'frequency': 'Frequency (Jumlah Produk)',
            'monetary': 'Monetary (Rata-rata Berat)',
            'recency': 'Recency Rank'
        },
        color_discrete_sequence=px.colors.qualitative.Dark2
    )
    fig_rfm.update_layout(title_x=0.5)
    st.plotly_chart(fig_rfm)

# Kesimpulan
elif menu == "Kesimpulan":
    st.header("Kesimpulan :bulb:")
    st.markdown("""
    1. **Frequency**: Fokus pada kategori dengan jumlah produk terbanyak untuk meningkatkan penjualan.
    2. **Monetary**: Analisis berat rata-rata untuk mengoptimalkan logistik.
    3. **Recency**: Kategori dengan frekuensi tinggi mencerminkan permintaan yang lebih tinggi.
    """)

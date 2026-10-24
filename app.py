import streamlit as st

st.set_page_config(page_title="İnşaat Mühendisliği Hesaplayıcı", page_icon="🏗️")
st.title("🏗️ Beton Eleman Taşıma Kapasitesi Hesaplayıcı")

st.sidebar.header("Girdi Parametreleri")

beton_sinifi = st.sidebar.selectbox("Beton Sınıfı Seçin", ["C20", "C25", "C30", "C35", "C40", "C50"])
genislik = st.sidebar.number_input("Kesit Genişliği (b) [mm]", min_value=100, max_value=2000, value=300, step=50)
yukseklik = st.sidebar.number_input("Kesit Yüksekliği (h) [mm]", min_value=100, max_value=2000, value=500, step=50)

fck_degerleri = {"C20": 20, "C25": 25, "C30": 30, "C35": 35, "C40": 40, "C50": 50}

fck = fck_degerleri[beton_sinifi]
alani_mm2 = genislik * yukseklik
alani_m2 = alani_mm2 / 1_000_000
tasima_kapasitesi_kn = (fck * alani_mm2) / 1000

st.subheader("📊 Hesaplama Sonuçları")
col1, col2 = st.columns(2)
col1.metric("Kesit Alanı", f"{alani_m2:.2f} m²")
col2.metric("Eksenel Basınç Kapasitesi", f"{tasima_kapasitesi_kn:,.1f} kN")

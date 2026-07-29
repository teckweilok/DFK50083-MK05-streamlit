import streamlit as st

# ------------------------------------------------------------
# Konfigurasi halaman
# ------------------------------------------------------------
st.set_page_config(page_title="Profil & Kalkulator BMI", page_icon="🧑‍💻", layout="wide")

# ------------------------------------------------------------
# 1. BAHAGIAN PROFIL (ASAS)
# ------------------------------------------------------------
st.title("🧑‍💻 Aplikasi Profil Peribadi & Kalkulator BMI")
st.header("Profil Diri")

# Layout dengan st.columns untuk elemen visual + info profil
col1, col2 = st.columns([1, 2])

with col1:
    # Elemen visual - gambar profil (placeholder online, boleh tukar ke gambar sendiri)
    st.image(
        "https://via.placeholder.com/300x300.png?text=Foto+Profil",
        caption="Gambar Profil",
        use_container_width=True,
    )

with col2:
    st.markdown(
        """
        **Nama:** _(isi nama anda)_  
        **Bidang Pengajian:** _(isi bidang pengajian anda)_  
        **Hobi:** _(isi hobi anda)_

        Selamat datang ke aplikasi web ringkas saya! Aplikasi ini dibangunkan
        menggunakan **Streamlit** sebagai sebahagian daripada Aktiviti MK05.
        """
    )

st.divider()

# ------------------------------------------------------------
# SIDEBAR (Susun Atur)
# ------------------------------------------------------------
st.sidebar.title("⚙️ Menu & Tetapan")
st.sidebar.write("Gunakan menu di bawah untuk mencuba kalkulator BMI.")
unit = st.sidebar.selectbox("Pilih unit ketinggian:", ["Meter (m)", "Sentimeter (cm)"])
st.sidebar.info("Kalkulator BMI ini mengira Indeks Jisim Badan (BMI) anda "
                 "berdasarkan berat dan ketinggian yang dimasukkan.")

# ------------------------------------------------------------
# 2. BAHAGIAN INTERAKTIF (Widgets & Logik) - Kalkulator BMI
# ------------------------------------------------------------
st.header("🧮 Kalkulator BMI Ringkas")

col3, col4 = st.columns(2)

with col3:
    berat = st.number_input("Masukkan berat badan anda (kg):", min_value=1.0, max_value=300.0, value=60.0, step=0.5)

with col4:
    if unit == "Meter (m)":
        tinggi = st.slider("Masukkan ketinggian anda (m):", min_value=1.0, max_value=2.5, value=1.65, step=0.01)
        tinggi_m = tinggi
    else:
        tinggi_cm = st.slider("Masukkan ketinggian anda (cm):", min_value=100, max_value=250, value=165, step=1)
        tinggi_m = tinggi_cm / 100

kira_button = st.button("Kira BMI Saya")

# Logik Ringkas - respon berdasarkan input pengguna
if kira_button:
    bmi = berat / (tinggi_m ** 2)
    st.subheader(f"BMI anda ialah: **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("Kategori: Kurang Berat Badan (Underweight)")
    elif 18.5 <= bmi < 25:
        st.success("Kategori: Berat Badan Normal (Normal)")
    elif 25 <= bmi < 30:
        st.warning("Kategori: Berlebihan Berat Badan (Overweight)")
    else:
        st.error("Kategori: Obes (Obese)")

    st.progress(min(int(bmi * 2), 100))
else:
    st.info("Masukkan berat & ketinggian anda, kemudian tekan butang **Kira BMI Saya**.")

st.divider()
st.caption("Dibangunkan untuk Aktiviti MK05 - Streamlit (DFK50083)")

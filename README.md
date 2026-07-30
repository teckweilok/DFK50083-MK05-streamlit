LOKTECKWEI<br>
18DIT24F1100<br>
DIT5E_18DIT24F1100_TECKWEI<br>


## Penerangan Aplikasi

Aplikasi web ringkas ini dibangunkan menggunakan **Streamlit** (Python). Ia memaparkan
profil peribadi ringkas (nama, bidang pengajian, hobi, gambar profil) serta sebuah
**Kalkulator BMI (Indeks Jisim Badan)** yang interaktif.

Ciri-ciri utama:
- Paparan tajuk, sub-tajuk, dan gambar profil.
- Input pengguna melalui `st.number_input`, `st.slider`, `st.selectbox`, dan `st.button`.
- Logik pengiraan BMI berdasarkan berat dan ketinggian yang dimasukkan, lengkap
  dengan kategori (Kurang Berat Badan / Normal / Berlebihan / Obes).
- Susun atur menggunakan `st.sidebar` (menu tetapan) dan `st.columns` (susunan
  ruang profil dan input).

## Cara Menjalankan Aplikasi

1. Klon repository ini:
   ```
   git clone https://github.com/<username>/dfk50083-mk05-streamlit.git
   cd dfk50083-mk05-streamlit
   ```
2. Pasang library yang diperlukan:
   ```
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi:
   ```
   streamlit run app.py
   ```
4. Aplikasi akan terbuka secara automatik di pelayar web anda (biasanya di
   `http://localhost:8501`).

import streamlit as st
import pandas as pd

st.title('Halo! Ini Aplikasi Pertamaku')

st.write("""
Selamat datang di aplikasi Streamlit. 
Di sini kita bisa menampilkan data dengan mudah.
""")

nama = st.text_input("Siapa nama Anda?", "Ketik nama di sini...")

if st.button('Sapa Saya'):
    st.success(f'Halo, {nama}! Senang bertemu Anda.')

# Contoh grafik sederhana
st.write("Contoh Grafik:")
data = pd.DataFrame({'Angka': [1, 2, 3, 4, 5], 'Nilai': [10, 20, 30, 40, 50]})
st.line_chart(data)

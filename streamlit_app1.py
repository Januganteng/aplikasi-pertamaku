import streamlit as st

st.title("📺 Pemutar YouTube Sederhana")

# 1. Kotak Input untuk memasukkan Link
url_video = st.text_input("Masukkan Link YouTube di sini:", "https://www.youtube.com/watch?v=yoI88jG3vqM")

# 2. Logika untuk memutar
if url_video:
    try:
        st.write("Sedang memutar video...")
        
        # Fungsi ajaib Streamlit untuk memutar video
        st.video(url_video)
        
    except Exception as e:
        st.error(f"Video tidak bisa diputar. Error: {e}")

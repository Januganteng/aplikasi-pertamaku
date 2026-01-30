import streamlit as st
from youtubesearchpython import VideosSearch
from pytube import YouTube
import os

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="YouTube Super App", page_icon="▶️")

st.title("▶️ Aplikasi YouTube All-in-One")
st.write("Dibuat dengan Python & Streamlit")

# --- Menu Sidebar (WAJIB ADA AGAR ELIF BEKERJA) ---
menu = ["Cari Video", "Putar Video", "Download Video"]
choice = st.sidebar.selectbox("Pilih Menu", menu)

# ==========================================
# FITUR 1: PENCARIAN VIDEO
# ==========================================
if choice == "Cari Video":
    st.header("🔍 Cari Video YouTube")
    query = st.text_input("Masukkan kata kunci pencarian:")
    
    if st.button("Cari"):
        if query:
            with st.spinner('Sedang mencari...'):
                try:
                    # Mencari 10 video
                    videosSearch = VideosSearch(query, limit=10)
                    results = videosSearch.result()
                    
                    st.success(f"Menemukan hasil untuk: {query}")
                    
                    for video in results['result']:
                        col1, col2 = st.columns([1, 2])
                        with col1:
                            st.image(video['thumbnails'][0]['url'], use_column_width=True)
                        with col2:
                            st.subheader(video['title'])
                            st.write(f"Channel: **{video['channel']['name']}**")
                            st.write(f"Views: {video['viewCount']['short']} | Durasi: {video['duration']}")
                            # Link agar bisa dicopy user
                            st.text_input("Link Video:", video['link'], key=video['id'])
                        st.divider()
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
        else:
            st.warning("Mohon masukkan kata kunci.")

# ==========================================
# FITUR 2: PUTAR VIDEO (VERSI ANTI-ERROR)
# ==========================================
elif choice == "Putar Video":
    st.header("📺 Putar Video")
    url = st.text_input("Masukkan Link YouTube:", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    if url:
        st.info("Jika player atas error, gunakan player bawah.")
        
        # 1. Player Standar
        try:
            st.video(url)
        except:
            pass
            
        # 2. Player Alternatif (Embed HTML)
        # Mencoba mengambil ID video dari berbagai format link
        video_id = ""
        if "youtu.be" in url:
            video_id = url.split("/")[-1]
        elif "v=" in url:
            try:
                video_id = url.split("v=")[1].split("&")[0]
            except:
                pass
        elif "shorts" in url:
            video_id = url.split("shorts/")[1].split("?")[0]
            
        if video_id:
            st.write("---")
            st.write("**Player Alternatif (Lebih Kuat):**")
            html_code = f"""
            <iframe width="100%" height="400" 
            src="https://www.youtube.com/embed/{video_id}" 
            frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
            """
            st.markdown(html_code, unsafe_allow_html=True)
        else:
            if len(url) > 10: 
                st.warning("Format link mungkin salah atau belum didukung.")

# ==========================================
# FITUR 3: DOWNLOADER
# ==========================================
elif choice == "Download Video":
    st.header("⬇️ Download Video")
    st.info("Catatan: Download mungkin lambat tergantung server Streamlit.")
    
    url_dl = st.text_input("Masukkan Link untuk didownload:")
    
    if url_dl:
        if st.button("Cek Video"):
            try:
                yt = YouTube(url_dl)
                st.image(yt.thumbnail_url, width=300)
                st.write(f"**Judul:** {yt.title}")
                
                # Mengambil stream
                stream = yt.streams.get_highest_resolution()
                st.success(f"Siap mendownload resolusi: {stream.resolution}")
                
                # Tombol Download
                # Kita harus mendownload dulu ke server, baru kirim ke user
                with st.spinner('Sedang mengunduh ke server...'):
                    path = stream.download(filename="video.mp4")
                    
                    with open(path, "rb") as file:
                        st.download_button(
                            label="📥 Klik SINI untuk Simpan ke HP/Laptop",
                            data=file,
                            file_name=f"{yt.title}.mp4",
                            mime="video/mp4"
                        )
            except Exception as e:
                st.error(f"Gagal. YouTube sering memblokir IP server cloud. Error: {e}")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Pastikan file requirements.txt berisi: streamlit, pytube, youtube-search-python, httpx==0.23.3")

import streamlit as st
from pytube import YouTube
from youtubesearchpython import VideosSearch
import os

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="YouTube Super App", page_icon="▶️")

st.title("▶️ Aplikasi YouTube All-in-One")
st.write("Dibuat dengan Python & Streamlit")

# --- Menu Sidebar ---
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
                            st.write(f"[Buka di YouTube]({video['link']})")
                        st.divider()
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
        else:
            st.warning("Mohon masukkan kata kunci.")

# ==========================================
# FITUR 2: PUTAR VIDEO
# ==========================================
elif choice == "Putar Video":
    st.header("📺 Putar Video")
    url = st.text_input("Masukkan Link YouTube:", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    if url:
        st.video(url)

# ==========================================
# FITUR 3: DOWNLOADER
# ==========================================
elif choice == "Download Video":
    st.header("⬇️ Download Video")
    st.info("Catatan: Hanya bisa download resolusi standard (720p/360p) yang memiliki suara.")
    
    url_dl = st.text_input("Masukkan Link untuk didownload:")
    
    if url_dl:
        try:
            yt = YouTube(url_dl)
            st.image(yt.thumbnail_url, width=300)
            st.write(f"**Judul:** {yt.title}")
            st.write(f"**Author:** {yt.author}")
            
            # Tombol Proses
            if st.button("Proses Video"):
                with st.spinner('Sedang memproses video... (Mohon tunggu)'):
                    # Mengambil stream progresif (video + audio gabung)
                    stream = yt.streams.get_highest_resolution()
                    
                    # Download ke memori server sementara
                    path = stream.download(filename="video_download.mp4")
                    
                    # Membaca file untuk tombol download
                    with open(path, "rb") as file:
                        btn = st.download_button(
                            label="📥 Klik di sini untuk Simpan Video",
                            data=file,
                            file_name=f"{yt.title}.mp4",
                            mime="video/mp4"
                        )
                    
                    # Hapus file sampah di server
                    # os.remove(path) 
        except Exception as e:
            st.error(f"Gagal memproses link. Pastikan link benar atau video tidak diprivate. Error: {e}")

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Tips: Jika terjadi error pada Downloader, itu wajar karena YouTube sering mengupdate sistem keamanannya.")

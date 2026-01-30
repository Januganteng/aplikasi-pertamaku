# ==========================================
# FITUR 2: PUTAR VIDEO (VERSI PERBAIKAN)
# ==========================================
elif choice == "Putar Video":
    st.header("📺 Putar Video")
    url = st.text_input("Masukkan Link YouTube:", "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    if url:
        try:
            # 1. Coba pakai Player Standar Streamlit
            st.write("Mode Player 1 (Standar):")
            st.video(url)
        except:
            st.warning("Player standar gagal, mencoba metode alternatif...")
    
    # 2. Metode Alternatif (Embed HTML Manual) - Lebih kuat untuk Shorts/Video tertentu
    # Logika untuk mengambil ID Video dari link
    video_id = ""
    if "youtu.be" in url:
        video_id = url.split("/")[-1]
    elif "v=" in url:
        video_id = url.split("v=")[1].split("&")[0]
    elif "shorts" in url:
        video_id = url.split("shorts/")[1].split("?")[0]
        
    if video_id:
        st.write("---")
        st.write("Mode Player 2 (Embed Paksa):")
        st.markdown(
            f'<iframe width="100%" height="400" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            unsafe_allow_html=True
        )
    elif url and not video_id:
        st.error("Link tidak dikenali. Pastikan link YouTube benar.")

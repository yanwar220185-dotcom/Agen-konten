import streamlit as st

st.title("🤖 Robot Penulis")
tugas = st.text_input("Apa yang ingin kamu tulis?")

if st.button("Robot, Tolong Tuliskan!"):
    if tugas:
        st.write("Robot sedang berpikir...")
        st.success(f"Ini tulisan keren tentang: {tugas}!")
    else:
        st.warning("Tulis dulu topiknya ya!")


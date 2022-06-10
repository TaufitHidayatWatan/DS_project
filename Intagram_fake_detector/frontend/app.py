import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Fake Instagram Detector",
    page_icon="‼️",
    menu_items={
        'Get Help': 'https://web.facebook.com/watanthw/',
        'Report a bug': "https://github.com/TaufitHidayatWatan/",
        'About': "# Hai, ini adalah Milestone_2 Phase_1 Taufit Hidayat Watan di FTDS Hacktiv8!"
           }
)


#st.title("Instagram Fake Account Detector")
st.markdown("<h1 style='text-align: center; color: black;'>Instagram Fake Account Detector</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image("fakes.jpg")

with col3:
    st.write(' ')

#with st.form(key = "form1"):
pp = st.selectbox("Apakah Akun Memiliki Foto Profil", ["Tidak", "Iya"])
name = st.selectbox("Apakah Nama Akun Sama Dengan Username Akun", ["Tidak", "Iya"])
desc = st.number_input("Berapa Banyak Deskripsi Pada Akun")
url = st.selectbox("Apakah Akun Memilki External URL", ["Tidak", "Iya"])
prv = st.selectbox("Apakah Akun Bersifat Private", ["Tidak", "Iya"])
posts = st.number_input("Berapa Jumlah Postingan Akun")
followers = st.number_input("Berapa Jumlah Followers Akun")
follows = st.number_input("Berapa Jumlah Following Akun")
    #submit = st.form_submit_button(label = 'Ayok Cek!!!')

# inference
data = {'profile pic':pp,
        'name==username':name,
        'description length': desc,
        'external URL':url,
        'private':prv,
        '#posts':posts,
        '#followers':followers,
        '#follows':follows
        }

URL = "https://h8-m2-backend.herokuapp.com//instagram"

# komunikasi
r = requests.post(URL, json=data)
print('r:',r)
res = r.json()

if st.button('Ayo Cek!!'):
    st.header(res['result']['classes'])






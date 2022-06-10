import streamlit as st
from PIL import Image, ImageOps
from img_classification import fmd_detector
st.set_page_config(
    page_title="FMD Detector",
    page_icon="🐄",
    menu_items={
        'Get Help': 'https://web.facebook.com/watanthw/',
        'Report a bug': "https://github.com/TaufitHidayatWatan/",
        'About': "# Hai, ini adalah Milestone_2 Phase_2 Taufit Hidayat Watan di FTDS Hacktiv8!"
           }
)

#st.title("Instagram Fake Account Detector")
st.markdown("<h1 style='text-align: center; color: black;'>Foot and Mouth Disease on Cattle Detector</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:
    st.image("cattle.jpg")

with col3:
    st.write(' ')

uploaded_file = st.file_uploader("Please Upload Your Cattle Images ...", type=['jpg', 'png', 'jpeg'])
if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Detecting...")
        classes = fmd_detector(image, 'FMD_Base.h5')
        print(classes) 
        if classes[0][0] == 1:
            st.write('Not - Infected')
        else:
            st.write('Infected')
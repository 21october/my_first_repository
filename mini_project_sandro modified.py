#https://fr.sandro-paris.com/fr/femme/manteaux/manteau-en-drap-de-laine/SFPOU00489.html?dwvar_SFPOU00489_color=G023#start=1
#python3 -m streamlit run /Users/youkyung/temp/my_first_repository/my_first_repository/strlit.py

import streamlit as st
from utils2.save_info import Sandro

st.write("""
산드로의 페이지 링크를 입력하면 이미지와 상품정보를 다운로드 할 수 있어요!
""")

form = st.form(key="my_form")
url = form.text_input(label="Url을 입력하세요. 이미지와 상품정보가 다운로드 됩니다.", placeholder="https://fr.sandro-paris.com/fr/femme/manteaux/manteau-en-drap-de-laine/SFPOU00489.html?dwvar_SFPOU00489_color=G023#start=1")
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    print(f"URL: {url}")
    sandro = Sandro()
    scrapped_info = sandro.get_info(url)
    sandro.save_info(scrapped_info)
    sandro.save_images(scrapped_info)

st.write("""
작업이 끝났습니다.
""")

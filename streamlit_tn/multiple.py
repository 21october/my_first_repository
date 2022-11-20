#https://fr.sandro-paris.com/fr/femme/manteaux/manteau-en-drap-de-laine/SFPOU00489.html?dwvar_SFPOU00489_color=G023#start=1
#python3 -m streamlit run /Users/youkyung/temp/my_first_repository/my_first_repository/strlit.py

import streamlit as st
from streamlit_tn.utils2.save_info import CELINE, DIOR
from utils2.save_info import Sandro

st.write("""
페이지 링크를 입력하면 이미지와 상품정보를 다운로드 할 수 있어요!
""")
#첫 번째 버튼 : 디올
form_dior = st.form(key="dior")
url_dior = form_dior.text_input(label="DIOR")
submit_button_dior = form_dior.form_submit_button(label='디올 이미지 다운로드')

if submit_button_dior:
    dior = DIOR()
    scrapped_dior = dior.get_info(url_dior)
    dior.save_images(scrapped_dior)
    st.success('다운로드를 완료했습니다.', icon="✅")


#두 번째 버튼: 셀린느
form_celine = st.form(key="celine")
url_celine = form_celine.text_input(label="CELINE")
submit_button_celine = form_celine.form_submit_button(label='셀린느 이미지 다운로드')

if submit_button_celine:
    celine = CELINE()
    scrapped_celine = celine.get_info(url_celine)
    celine.save_images(scrapped_celine)
    st.success('다운로드를 완료했습니다.', icon="✅")




#세 번째 버튼: 산드로
form_sandro = st.form(key="sandro")
url_sandro = form_sandro.text_input(label="SANDRO")
submit_button = form_sandro.form_submit_button(label='산드로 이미지 다운로드')

if submit_button:
    sandro = Sandro()
    scrapped_sandro = sandro.get_info(url_sandro)
    sandro.save_images(scrapped_sandro)
    st.success('다운로드를 완료했습니다.', icon="✅")








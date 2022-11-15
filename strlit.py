#python3 -m streamlit run /Users/youkyung/temp/my_first_repository/my_first_repository/strlit.py

import streamlit as st
import pandas as pd

form = st.form(key="my_form")
url = form.text_input(label="Url을 입력하세요. 이미지와 상품정보가 다운로드 됩니다.")
submit_button = form.form_submit_button(label='Submit')





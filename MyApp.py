import streamlit as st
# from utils.save_files import save_info, save_images, get_information

from utils.save_files import GoodClass
from utils.save_files import Cup


cup = Cup()
print("처음 컵의 상태는: ", cup.is_empty)
cup.refill()
print("리필 된 후의 상태는: ", cup.is_empty)
cup.drink()
print("마신 후의 상태는: ", cup.is_empty)


st.write("""
이미지가 있는 페이지의 URL 을 보내면, 이미지와 상품정보를 다운로드 할 수 있어요.
""")

form = st.form(key="my_form")
url = form.text_input(label="URL 을 입력하세요.")

submitted = form.form_submit_button(label="Submit")

if submitted:
    print(f"URL: {url}")

    good = GoodClass()

    scrapped_info = good.get_information(url)
    good.save_info(scrapped_info)
    good.save_images(scrapped_info)

    st.write("""
    모든 작업이 끝났어요.
    """)

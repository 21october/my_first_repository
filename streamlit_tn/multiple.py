#https://fr.sandro-paris.com/fr/femme/manteaux/manteau-en-drap-de-laine/SFPOU00489.html?dwvar_SFPOU00489_color=G023#start=1
#python3 -m streamlit run /Users/youkyung/temp/my_first_repository/my_first_repository/strlit.py
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import urllib.request
import os

current_path = os.getcwd()

class SANDRO:
    def get_info(self, page_url):
        response = requests.get(page_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.select_one("#title").text
        #price = soup.select_one("span.price-sales").text.strip()
        images = soup.select("img", attrs={"class": "productthumbnail lazyload loaded"})

        return {'name': name, 'images': images}

    def save_images(self, info):
        img_list =[]
        for img in info['images']:
            if "data-hires" in img.attrs:
                img_url = img["data-hires"]
                img_list.append(img_url)
            else:
                pass
        
        for index, url in enumerate(img_list):
            with urlopen(url) as f:
                with open(f"{current_path}/{info['name']}_{str(index)}.jpg", 'wb') as h:
                    img = f.read()
                    h.write(img)


class DIOR:
    def get_info(self, page_url):
        response = requests.get(page_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        name = soup.select_one('span.multiline-text.Titles_title__PAVsd').text
        images = soup.select('img')
        reference = soup.select_one('p.Titles_ref__7LPN1').text.split(':')[1].strip()

        return {'name': name, 'images': images, 'reference': reference}

    def save_images(self, info):
        img_list =[]
        for img in info['images']:
            if info['reference'] in img['src']:
                try:
                    img_list.append(img['src'])
                except:
                    pass
        
        for index, url in enumerate(img_list):
            with urlopen(url) as f:
                with open(f"{current_path}/{info['name']}_{str(index)}.jpg", 'wb') as h:
                    img = f.read()
                    h.write(img)

class CELINE:
    def get_info(self, page_url):
        response = requests.get(page_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        name = soup.select_one('span.o-product__title-truncate.f-body--em').text
        images = soup.find_all('button','m-thumb-carousel__img')
        reference = soup.select_one('span.product-id.d-none').text

        return {'name': name, 'images': images, 'reference': reference}

    def save_images(self, info):
        n = 1
        for img in info['images']:
            imgUrl = img.find('img')['data-src-zoom']
            urllib.request.urlretrieve(imgUrl, current_path+'/'+info['name'] + str(n)+'.jpg')
            n += 1
        


import streamlit as st

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
    sandro = SANDRO()
    scrapped_sandro = sandro.get_info(url_sandro)
    sandro.save_images(scrapped_sandro)
    st.success('다운로드를 완료했습니다.', icon="✅")








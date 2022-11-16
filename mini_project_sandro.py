from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import urllib.request
import openpyxl

#터미널 명령어
#python3 -m streamlit run /Users/youkyung/temp/my_first_repository/my_first_repository/strlit.py

# import streamlit as st
# import pandas as pd

# form = st.form(key="my_form")
# url = form.text_input(label="Url을 입력하세요. 이미지와 상품정보가 다운로드 됩니다.")
# submit_button = form.form_submit_button(label='Submit')

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["이름","가격"])

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#이름 엑셀에 기록
name = soup.select_one("#title").text
ws.cell(row=2, column=1).value = name
#가격 엑셀에 기록
price = soup.select_one("span.price-sales").text.strip()
ws.cell(row=2, column=2).value = price

images = soup.select("img",attrs={"class":"productthumbnail lazyload loaded"})

list = []
for img in images:
    if "data-hires" in img.attrs:
        imgUrl = img["data-hires"]
        list.append(imgUrl)
    else:
        pass
    
from urllib.request import urlopen
n = 1
for i in list:
    with urlopen(i) as f:
        with open("/Users/youkyung/miniproject/"+name+str(n)+'.jpg','wb') as h:
            img = f.read()
            h.write(img)
    n += 1

wb.save(f"/Users/youkyung/miniproject/{name}.xlsx")

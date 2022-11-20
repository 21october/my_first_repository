from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import urllib.request


class Sandro:
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
                with open(f"{info['name']}_{str(index)}.jpg", 'wb') as h:
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
                with open(f"{info['name']}_{str(index)}.jpg", 'wb') as h:
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
            urllib.request.urlretrieve(imgUrl, info['name'] + str(n)+'.jpg')
            n += 1
        
        # for index, url in enumerate(img_list):
        #     with urlopen(url) as f:
        #         with open(f"./results/{info['name']}_{str(index)}.jpg", 'wb') as h:
        #             img = f.read()
        #             h.write(img)
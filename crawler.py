final_data = []
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

df_total = pd.read_csv('Total List.csv')
df_urls = df_total['Product Link']
for item in df_urls:
    if item == 'NaN':
        item = np.nan
headers = {"Accept": "application/json, text/plain, */*",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "en-US,en;q=0.9", "Connection": "keep-alive",
           "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"}

attr = {
    'product_title': 'h1',
    'class_title': 'text-18 sm:text-32 md:text-32 font-bold text-dark-gray',
    'team': 'a',
    'class_team': 'text-14 sm:text-16 font-semibold text-light-gray py-3',
    'product_category': 'span',
    'class_category': 'text-12 font-semibold text-dark-gray text-dark-gray',
    'total_up_votes': 'div',
    'class_up_votes': 'text-14 font-semibold text-white uppercase',
    'class_comments': '#about > div.mb-10.flex.flex-row.justify-between > div:nth-child(3) > div.text-18.font-semibold.text-dark-gray',
    'class_day_rank': '#about > div.mb-10.flex.flex-row.justify-between > div:nth-child(5) > div.text-18.font-semibold.text-dark-gray',
    
    
}
df_first = pd.DataFrame(columns=['Name', 'Product_link', 'Post_link'])

for url in df_urls:
    if url is not np.nan:
        link = str(url).split('/')
        if len(link) > 4:
            if link[3] == 'products':
                df_first = df_first._append({'Name': link[4], 'Product_link': 'https://www.producthunt.com/' + 'products' + '/' + link[4], 'Post_link': 'https://www.producthunt.com/' + 'posts' + '/' + link[4]}, ignore_index=True)
            elif link[3] == 'posts':
                df_first = df_first._append({'Name': link[4], 'Product_link': 'https://www.producthunt.com/' + 'products' + '/' + link[4], 'Post_link': 'https://www.producthunt.com/' + 'posts' + '/' + link[4]}, ignore_index=True)
                
        else:
            df_first = df_first._append({'Product_link': np.nan, 'Post_link': np.nan}, ignore_index=True)
                

class Product:
    def __init__(self, url: str, attr: dict, headers: dict):
        self.url = url
        self.attr = attr
        self.web_obj = None
        self.web_page = None

    def webpage_setup(self):
        try:
            options = Options()
            # options.add_argument("--headless=new")
            options.add_argument(f"user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36")
            # options.add_argument("--no-sandbox")
            # options.add_argument("--disable-dev-shm-usage")
            # options.add_argument("disable-gpu")
            experimental_option = {"excludeSwitches": ["enable-automation",            
                                                    "ignore-certificate-errors",
                                                    "safebrowsing-disable-download-protection",
                                                    "safebrowsing-disable-auto-update",
                                                    "disable-client-side-phishing-detection"],
                                'useAutomationExtension': False}
            for key, value in experimental_option.items():
                options.add_experimental_option(key, value)
            self.selenium_driver = Chrome(options=options)
            self.selenium_driver.maximize_window()
            self.selenium_driver.set_page_load_timeout(60)
            self.selenium_driver.set_script_timeout(60)
            self.selenium_driver.get(self.url)   
            sleep(10)
            content = self.selenium_driver.page_source.encode('utf-8').strip()
            self.web_page = BeautifulSoup(content,"html.parser")
        except Exception as e:
            raise e

    def scrap_page(self):
        product_title = self.web_page.find(self.attr["product_title"], attrs={'class': self.attr['class_title']}).text
        team_member = self.web_page.find_all(self.attr['team'], attrs={'class': self.attr['class_team']})
        team_member = str(team_member)
        team_member = team_member.split(',')
        for i in range(0, len(team_member)):
            match = re.search(r'href="([^"]+)"', team_member[i])
            if match:
                href_content = match.group(1)
                team_member_link = "https://www.producthunt.com" + href_content
                team_member[i] = team_member_link
                
        return product_title, team_member

class Post:
    def __init__(self, url: str, attr: dict, headers: dict):
        self.url = url
        self.attr = attr
        self.web_obj = None
        self.web_page = None

    def webpage_setup(self):
        try:
            options = Options()
            # options.add_argument("--headless=new")
            options.add_argument(f"user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36")
            # options.add_argument("--no-sandbox")
            # options.add_argument("--disable-dev-shm-usage")
            # options.add_argument("disable-gpu")
            experimental_option = {"excludeSwitches": ["enable-automation",            
                                                    "ignore-certificate-errors",
                                                    "safebrowsing-disable-download-protection",
                                                    "safebrowsing-disable-auto-update",
                                                    "disable-client-side-phishing-detection"],
                                'useAutomationExtension': False}
            for key, value in experimental_option.items():
                options.add_experimental_option(key, value)
            self.selenium_driver = Chrome(options=options)
            self.selenium_driver.maximize_window()
            self.selenium_driver.set_page_load_timeout(60)
            self.selenium_driver.set_script_timeout(60)
            self.selenium_driver.get(self.url)   
            sleep(10)
            content = self.selenium_driver.page_source.encode('utf-8').strip()
            self.web_page = BeautifulSoup(content,"html.parser")
        except Exception as e:
            raise e

    def scrap_page(self):
        product_categories_elements = self.web_page.find_all(self.attr['product_category'], attrs={'class': self.attr['class_category']})
        product_categories = [element.text for element in product_categories_elements]
        total_up_votes = self.web_page.find(self.attr['total_up_votes'], attrs={'class': self.attr['class_up_votes']}).text
        total_comments = self.web_page.select_one(self.attr['class_comments']).text
        day_rank = self.web_page.select_one(self.attr['class_day_rank']).text
        # hunter_use = 
        # maker_comments
        
        return product_categories, total_up_votes, total_comments, day_rank
        
obj = Post(url="https://www.producthunt.com/posts/anode", attr= attr, headers=headers)    
obj.webpage_setup()
print(obj.scrap_page())








# post = 'https://www.producthunt.com/products/anode'
# post_obj = Post(url=post, attr=attr, headers=headers)
# final_data.append(post_obj.scrap_page())
# ''' product = 'https://www.producthunt.com/products/anode'
# product_obj = Product(url=product, attr=attr, headers=headers)
# final_data.append(product_obj.scrap_page())
# '''
# print(final_data)
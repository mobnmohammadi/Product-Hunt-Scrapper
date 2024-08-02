from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from browser import ChromeDriverManager
from config import show_all_makers_button_xpath

class Crawling():
    def __init__(self, product_id: str, 
                 driver_manager: ChromeDriverManager) -> None:
        self.product_id = product_id
        self.driver = driver_manager.get_driver()
        self._urls: dict = None

    def get_post_page(self):
        self.driver.get(url=self.urls['post'])
        if '404' in str(self.driver.get_log('browser')):
            return None
        
        try:
            WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="about"]')))
        except Exception as e:
            print(f"Error loading post page: {e}")
            return None

        sleep(10)
        return self.driver.page_source

    def get_all_makers_page(self):
        self.driver.get(url=self.urls['makers'])
        if '404' in str(self.driver.get_log('browser')):
            return None
        try:
            show_all_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, show_all_makers_button_xpath))
            )[0]

            if show_all_element.is_displayed():
                show_all_element.click()
        except Exception as e:
            print(f"Error loading makers page or clicking 'show all': {e}")
            return None

        return self.driver.page_source

    @property
    def urls(self):
        if self._urls is None:
            self._urls = {
                'makers': f"https://www.producthunt.com/products/{self.product_id}/makers",
                'post': f"https://www.producthunt.com/posts/{self.product_id}/"
            }
        return self._urls
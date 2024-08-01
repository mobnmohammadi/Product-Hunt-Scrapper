from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class ChromeDriverManager():
    def __init__(self, user_agent: str = None):
        self.user_agent = user_agent
        self.driver = self._create_driver()
        
    def _create_driver(self):
        chrome_options = Options()
        # options.add_argument("--headless=new")
        # chrome_options.add_argument(f"user-agent={self.user_agent}")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("disable-gpu")
        chrome_options.add_argument('--window-size=1920,1080')
        driver = Chrome(options=chrome_options)
        return driver

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        self.driver.quit()
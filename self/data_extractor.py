from bs4 import BeautifulSoup

class Extractor():
    def __init__(self, page_content, attrs) -> None:
        self.content = page_content
        self.attr = attrs
        self.extractor = BeautifulSoup(page_content, 'html.parser')
        self.result: dict = {}
        

    def perform_product_page(self):
        self.extract_product_title()
        self.extract_team_member_count()
    
    def perform_product_post(self):
        self.extract_product_categories()
        self.extract_status()
        self.has_hunter_badge()
    
    def extract_product_title(self):
        try:
            element = self.extractor.find(self.attr["product_title"], attrs={'class': self.attr['class_title']})
            self.result['product_title'] = element.text if element else None
        except Exception as e:
            print(f"Error extracting product title: {e}")
            self.result['product_title'] = None
    
    def extract_team_member_count(self):
        try:
            
            elements = self.extractor.find_all(self.attr['team'], attrs={'class': self.attr['class_team']})
            self.result['team_member_count'] = len(elements)
        except Exception as e:
            print(f"Error extracting team member count: {e}")
            self.result['team_member_count'] = None

    def extract_product_categories(self):
        try:
            elements = self.extractor.find_all(self.attr['product_category'], attrs={'class': self.attr['class_category']})
            self.result['categories'] = [element.text for element in elements] if elements else None
        except Exception as e:
            print(f"Error extracting product categories: {e}")
            self.result['categories'] = None
    
    def extract_status(self):
        try:
            elements = self.extractor.find_all(class_ = 'flex flex-col items-center gap-2')
            if elements:
                result = [element.find('div', attrs={'class': 'text-18 font-semibold text-dark-gray'}).text for element in elements]
                self.result['comments_count'] = result[1]
                self.result['up_votes'] = result[0]
                self.result['day_rank'] = result[2]
            else:
                self.result['comments_count'] = None
                self.result['up_votes'] = None
                self.result['day_rank'] = None
        except Exception as e:
            print(f"Error extracting status: {e}")
            self.result['comments_count'] = None
            self.result['up_votes'] = None
            self.result['day_rank'] = None

    def has_hunter_badge(self):
        try:
            element = self.extractor.find('path', attrs={'d': 'M4.55 10h1.18V7.625h2.54V10h1.18V4.363H8.27v2.29H5.73v-2.29H4.55z'})
            self.result['hunter_badge'] = True if element else False
        except Exception as e:
            print(f"Error checking hunter badge: {e}")
            self.result['hunter_badge'] = False

    def get_team_member_count(self):
        try:
            element = self.extractor.find_all('path', attrs={'d': 'M4.055 10h1.05V6.164h.079L6.629 10h.738l1.446-3.836h.078V10h1.05V4.363H8.59L7.035 8.488h-.07L5.406 4.363H4.055z'})
            self.result['team_member_count'] = len(element)
        except Exception as e:
            print(f"Error checking team_member_count badge: {e}")
            self.result['team_member_count'] = None

    def get_product_title(self):
        try:
            element = self.extractor.find('h1', attrs={'class': 'text-24 font-bold text-dark-gray styles_title__x5KUY'})
            self.result['product_title'] = len(element)
        except Exception as e:
            print(f"Error checking product_title badge: {e}")
            self.result['product_title'] = None
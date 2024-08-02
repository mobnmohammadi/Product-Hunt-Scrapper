from crawler import Crawling
from browser import ChromeDriverManager
from data_extractor import Extractor
from config import get_random_user_agent, attr
from data_gathering import output

def main():
    with open('self/first_500.csv', 'r') as names:
        product_names = names.readlines()
        for product_name in product_names:
            page = Crawling(product_id = product_name, driver_manager = ChromeDriverManager(user_agent=get_random_user_agent()))
            product_page = page.get_all_makers_page()
            result = {}
            if product_page is not None:
                extraction_object = Extractor(page_content = product_page ,attrs = attr)
                extraction_object.perform_product_page()
                result = extraction_object.result

            post_page = page.get_post_page()
            if post_page:
                extraction_object = Extractor(page_content = post_page ,attrs = attr)
                extraction_object.perform_product_post()
                for key, value in extraction_object.result.items():
                    result[key] = value
            if 'product_title'  not in result.keys() or result['product_title'] == None:
                result['product_name'] = extraction_object.get_product_title()
            if 'team_member_count'  not in result.keys() or result['team_member_count'] == None:
                result['team_member_count'] = extraction_object.get_team_member_count()

            output(result)

if __name__ == '__main__':
    main()
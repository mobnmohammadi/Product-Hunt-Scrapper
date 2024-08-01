from random import choice

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5910.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6055.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6117.95 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6176.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5910.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6055.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6117.95 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6176.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5910.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6055.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6117.95 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6176.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.63 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.91 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.98 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5910.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6055.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6117.95 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6176.97 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0"
]

show_all_makers_button_xpath = '//*[@id="__next"]/div[2]/div[3]/main/div[2]/div/div[2]/button'


attr = {
    'product_title': 'h1',
    'class_title': 'text-18 sm:text-32 md:text-32 font-bold text-dark-gray',
    'team': 'li',
    'class_team': 'styles_makerItem__cTHr3 mb-6 flex flex-row',
    'product_category': 'span',
    'class_category': 'text-12 font-semibold text-dark-gray text-dark-gray',
    'total_up_votes': 'div',
    'class_up_votes': 'text-14 font-semibold text-white uppercase',
    'class_comments': '#about > div.mb-10.flex.flex-row.justify-between > div:nth-child(3) > div.text-18.font-semibold.text-dark-gray',
    'class_day_rank': '#about > div.mb-10.flex.flex-row.justify-between > div:nth-child(5) > div.text-18.font-semibold.text-dark-gray',
    
    
}
# attr = {
#     "product_title": "h1",  # Example, adjust according to actual HTML structure
#     "class_title": "product-title-class",  # Example, adjust according to actual HTML structure
#     "team": "div",  # Example, adjust according to actual HTML structure
#     "class_team": "team-member-class",  # Example, adjust according to actual HTML structure
#     "product_category": "a",  # Example, adjust according to actual HTML structure
#     "class_category": "category-class",  # Example, adjust according to actual HTML structure
# }

def get_random_user_agent():
    return choice(user_agents)


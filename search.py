import requests 
from bs4 import BeautifulSoup 

class Search:
    NAME = ""
    SPLITTED_NAME = []
    FORMATTED_NAME = ""

    URL = []

    SITE_1 = {}
    SITE_2 = {}


    # PYTHON CONSTRUCTOR
    def __init__(self, name):
        self.NAME = name
        self.SPLITTED_NAME = name.split(" ")
        self.FORMATTED_NAME = "+".join(self.SPLITTED_NAME)

        self.URL.append(f"https://itti.com.np/catalogsearch/result/index/?cat=&product_list_limit=24&q={self.FORMATTED_NAME}")
        self.URL.append(f"https://bigbyte.com.np/page/1/?s={self.FORMATTED_NAME}&post_type=product&dgwt_wcas=1")


    # SEND GET REQUESTS TO WEBSITES
    def open_url(self):
        i = 0
        while i < len(self.URL):
            site = requests.get(self.URL[i])

            self.parse_html(site.text, i)
            i += 1
        
        return self.return_data()

    def parse_html(self, html, count):
        parsed_html = BeautifulSoup(html, "html.parser")

        search_query = self.NAME

        if count == 0:
            names = parsed_html.find_all(class_="product-item-link")
            prices = parsed_html.find_all(class_="price")

            for (name,price) in zip(names,prices):
                # if name.string is not None and name.string.__contains__(search_query):
                if name.string is not None:
                    self.SITE_1[name.string] = price.string
        else:
            names = parsed_html.find_all(class_="woocommerce-loop-product__title")
            prices = parsed_html.find_all("bdi")

            for (name,price) in zip(names,prices):
                # if name.string.__contains__(search_query):
                if name.string is not None:
                    self.SITE_2[name.string] = price.text

    
    def return_data(self):
        return self.SITE_1, self.SITE_2
        # print("SITE 1:\n")
        # for key,value in self.SITE_1.items():
        #     print(f"{key}:{value}")
        
        # print("\nSITE 2:\n")
        # for key,value in self.SITE_2.items():
        #     print(f"{key}:{value}")
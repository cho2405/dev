import requests
from bs4 import BeautifulSoup


class Crawler:
    STOCK_POPULAR_URL = "https://finance.naver.com/sise/lastsearch2.nhn"
    STOCK_GOLDCROSS_URL = "https://finance.naver.com/sise/item_gold.nhn"
    STOCK_GAP_URL = "https://finance.naver.com/sise/item_gap.nhn"
    STOCK_QUANT_URL = "https://finance.naver.com/sise/sise_quant.nhn"

    def get_bs_obj(self, page):
        stock_url = ""
        if page == "popular":
            stock_url = self.STOCK_POPULAR_URL
        elif page == "goldcross":
            stock_url = self.STOCK_GOLDCROSS_URL
        elif page == "gap":
            stock_url = self.STOCK_GAP_URL
        elif page == "quant":
            stock_url = self.STOCK_QUANT_URL

        url_get = requests.get(stock_url)
        bs_obj = BeautifulSoup(url_get.content, "html.parser")
        return bs_obj

    def get_titles(self, page="popular"):
        bs_obj = self.get_bs_obj(page)
        stock_titles = bs_obj.find_all("a", {"class": "tltle"})
        for title in stock_titles:
            print(title.text)

        return stock_titles


crawler = Crawler()
titles = crawler.get_titles("quant")



from bs4 import BeautifulSoup
import requests

class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"}
        self.response=requests.get(url=self.url, headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response,"lxml")

    def product_title(self):
        # title=self.soup.find("span",id_="productTitle")
        title=self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text
        else:
            return "title not found"

    def product_price(self):
        price=self.soup.find("span",{"class":"a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "price not found"


device_info=PriceTracer(url="https://www.amazon.com/Smartphone-Unlocked-Processor-ProScaler-Manufacturer/dp/B0DP3G51DN/ref=sr_1_1_sspa?crid=3CS30ODS1C5YG&dib=eyJ2IjoiMSJ9.BfBevw5ara_BXd6hiDpYAs2J-XjeUHiXV7cXul3943o1TOBNHC7rv-Go51WsSZMzI1dMRRn2_JNFXzD9zj9t8aj0QQHJ5yxpYHTmQeBg2_tkhl1m__gjlgKE67nj5VyZTjit91kZs6lkW4-WDssr62TYunh6JMfQokTbvBvmkeQdvkSS9CFcCB3_x-b7hOCqVpfqXSTjfpbAR45_Oq7o-ODT7RHpwGVeUyNhqJHg2_0.Xg6KQ0yei8sQkm7Z9avihJ2a41avw5lKATXHNV3nfG4&dib_tag=se&keywords=s24&qid=1770157836&sprefix=s24%2Caps%2C496&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
print(device_info.product_title())
print(device_info.product_price())
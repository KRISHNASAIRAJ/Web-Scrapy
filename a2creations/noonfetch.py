import scrapy
from selenium import webdriver

class NoonSpider(scrapy.Spider):
    name = 'noon'
    allowed_domains = ['noon.com']

    main_url = [
        'https://www.noon.com/egypt-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?limit=50&page={}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc']

    def __init__(self):
        self.ddata = webdriver.Chrome()

    def start_requests(self):
        for i in range(1, 3):#here even if i tried to change no of pages it only gets the data for one page
            url = self.main_url[0].format(i)
            yield scrapy.Request(url=url, meta={"playwright": True}, callback=self.parse)

    def parse(self, response):
        self.ddata.get(response.url)
        for i in range(1, 51):
            url = 'https://noon.com'+response.xpath(
                f'//*[@id="__next"]/div/section/div/div/div/div[2]/div[1]/span[{i}]/a').get().split(" ")[1][6:]
            yield scrapy.Request(url=url, callback=self.product)

    def product(self, response):
        product_names = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/h1')
        product_name = product_names.css("h1::text").get()
        product_prices = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/span/div')
        product_price = product_prices.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/span/div/text()[3]').get()
        sellers = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/span[1]/button/div[2]/div[1]/div/div')
        seller = sellers.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/span[1]/button/div[2]/div[1]/div/div/span/span/text()').get()
        ratings = response.xpath(
            '/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/a/div/div[1]/span')
        rating = ratings.xpath(
            '/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/a/div/div[1]/span/text()').get()
        model_numbers = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div')
        model_number = model_numbers.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/div/text()[3]').get()
        delivery_dates = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/span[2]/div/div/div/div/div/div[1]/div/div/div/span')
        delivery_date = delivery_dates.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/span[2]/div/div/div/div/div/div[1]/div/div/div/span/text()').get()
        categories = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[1]/div/div/div/div/div/div/div/a')
        category = categories.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[1]/div/div/div/div/div/div/div/a/text()').get()
        currencies = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/span/div')
        currency = currencies.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/span/div/text()[1]').get()
        brands = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/a/div/div')
        brand = brands.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/a/div/div/text()').get()
        partners_ratings = response.xpath(
            '//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/span[1]/button/div[2]/div[2]/div[1]/span')
        partner_rating = partners_ratings.xpath(
            '/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/span[1]/button/div[2]/div[2]/div[1]/span/text()[1]').get()
        ratings_counts = response.xpath(
            '/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/a/div/div[2]/div/span')
        rating_count = ratings_counts.xpath(
            '/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]/a/div/div[2]/div/span/text()').get()
        partners_rating_counts = response.xpath(
            '//*[@id="__next"]/div/section/div[1]/div[1]/div[2]/div[2]/div[3]/div')
        partner_rating_count = partners_rating_counts.xpath(
            '//*[@id="__next"]/div/section/div[1]/div[1]/div[2]/div[2]/div[3]/div/text()').get()
        sku_all=response.xpath("/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[1]")
        sku=sku_all.xpath('//*[@id="__next"]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/a/div/div').get()[24:34]
        fbn_all=response.xpath("/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/span[2]/div/div/div/div/div/div[2]/div/img")
        fbn=fbn_all.xpath("/html/body/div[1]/div/section/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/span[2]/div/div/div/div/div/div[2]/div/img").get().split(" ")[2].split("=")[1][6:-1]
        f_url=response.url
        yield{
            'brand': brand,
            "product_name": product_name,
            'currency': currency,
            "prices": product_price,
            'category': category,
            'model_number': model_number,
            "seller": seller,
            'rating': rating,
            'rating_count': rating_count,
            'delivery': delivery_date,
            'partner_ratings': partner_rating,
            'partner_rating_count': partner_rating_count,
            'SKU':sku,
            'FBN':fbn,
            'URL':f_url
        }

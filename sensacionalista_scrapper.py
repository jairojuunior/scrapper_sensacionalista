import scrapy

class SensacionalistaScrapper(scrapy.Spider):
    name = "sensacionalista_scrapper"
    start_urls = ['https://www.sensacionalista.com.br/pais/', 'https://www.sensacionalista.com.br/entretenimento/']

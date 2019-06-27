import scrapy

#td-module-thumb
#entry-title
#start_urls = ['https://www.sensacionalista.com.br/pais/', 'https://www.sensacionalista.com.br/entretenimento/']
#//div[contains(@class, "entry-title")]/a::text()

class SensacionalistaScrapper(scrapy.Spider):
  name = "sensacionalista_scrapper"
  start_urls = ['https://www.sensacionalista.com.br/pais/']

  def parse(self, response):
    SET_SELECTOR = '//div[contains(@class, "entry-title")]/a::text()'
    print(response)
    #for news in response.xpath(SET_SELECTOR):
      #news_title = news.extract()
      #print(news_title)

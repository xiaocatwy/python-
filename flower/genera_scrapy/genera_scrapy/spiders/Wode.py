from scrapy.spider import Spider,Request
# from genera_scrapy.items import GeneraScrapyItem

class CountrySpider(Spider):
    # name = 'country'
    # def start_requests(self):
    #     url_str = "http://example.webscraping.com/places/default/view/Canada-41"
    #     yield Request(url=url_str, callback=self.parse_item , dont_filter=True)
    #
    # def parse_item(self,response):
    #     item = GeneraScrapyItem()
    #     item['name'] = response.css('tr#places_country__row td.w2p_fw::text').extract_first()
    #     item['population'] = response.css("tr#places_population__row td.w2p_fw::text").extract_first()
    #     print(item)
    #     yield item
    name = 'huabai'

    def __init__(self):
        self.title = "人物画像"

    def start_requests(self):
        url_str = "http://huaban.com/search/?q={}".format(self.title)
        yield Request(url=url_str, callback=self.parse, meta={"page": "1"})

    def parse(self, response):
        item = {}
        imgurl = response.xpath("//div[@id='waterfall']/div[@class='pin wfc wft']/a/img/@src").extract()
        for i in range(len(imgurl)):
            item["name"] = self.title
            item["imgurl"] = imgurl[i]

            item["imgherf"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc wft']/a/@href").extract()[i]

            item["imgvisit"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc wft']/p/span[@class='repin']/text()").extract()[i]
            try:
                item["imglike"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc wft']/p/span[@class='like']/text()").extract()[i]
            except Exception as e:
                item["imglike"] = "0"
            try:
                item["imgdiscrit"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc wft']/p[@class='description']/text()").extract()[i]
            except Exception as e:
                item["imgdiscrit"] = ""
            yield item
        for i in range(4):
            yield Request(url=response.url, callback=self.next, meta={"page": "2"},dont_filter=True)
    def next(self,response):
        item = {}
        imgurl = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/a/img/@src").extract()
        for i in range(len(imgurl)):
            item["name"] = self.title
            item["imgurl"] = imgurl[i]

            item["imgherf"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/a/@href").extract()[i]

            item["imgvisit"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/p/span[@class='repin']/text()").extract()[i]
            try:
                item["imglike"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/p/span[@class='like']/text()").extract()[i]
            except Exception as e:
                item["imglike"] = "0"
            try:
                item["imgdiscrit"] = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/p[@class='description']/text()").extract()[i]
            except Exception as e:
                item["imgdiscrit"] = ""
            yield item

        # imgurl1 = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/a/img/@src").extract()
        # imgherf1 = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/a/@href").extract()
        # imgvisit1 = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/p/span[@class='repin']/text()").extract()
        # imglike1 = response.xpath("//div[@id='waterfall']/div[@class='pin wfc ']/p/span[@class='like']/text()").extract()
        # print(imgurl1)


import scrapy
import re
from markets.items import MarketsItem


class MakroSpider(scrapy.Spider):
    name = "makro"
    allowed_domains = ["makromarket.uz"]


    def start_requests(self):
        url="https://makromarket.uz/products"
        yield scrapy.Request(
        url=url,
        callback=self.parse,
        meta={"playwright": True}
        )
    def parse(self, response):
        for product in response.css("div.product > div.card"):
            item=MarketsItem()

            # item["market_name"]='makro'
            # item['old_price']=float(
            #     re.sub(
            #         r"[^\d]",
            #         "",
            #         (product.css("div.old-price::text").get() or "0"),
            #     )
            # )
            # item['current_price']=float(
            #     re.sub(
            #         r"[^\d]",
            #         "",
            #         (product.css("div.current-price::text").get() or "0"),
            #     )
            # )

            # yield item

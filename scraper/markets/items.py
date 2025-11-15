# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarketsItem(scrapy.Item):

    market_name = scrapy.Field()
    product_name = scrapy.Field()
    discount_period = scrapy.Field()
    promotion_info = scrapy.Field()
    old_price = scrapy.Field()
    current_price = scrapy.Field()
    price_unit = scrapy.Field()
    discount = scrapy.Field()
    weight = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()

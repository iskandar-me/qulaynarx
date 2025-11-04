import scrapy
import re
from markets.items import MarketsItem
from scrapy_playwright.page import PageMethod

class BarakaSpider(scrapy.Spider):
    name = "baraka"
    allowed_domains = ["barakamarket.uz"]

    def start_requests(self):
        url = "https://barakamarket.uz/discounts"

        yield scrapy.Request(
            url,
            callback=self.parse,
            meta={
                "playwright":True,
                "playwright_page_methods": [
                PageMethod("wait_for_selector", "div.flex.flex-col.justify-center.items-center.mx-2.bg-white.shadow-blockShadow.p-7.mb-10.mt-10.rounded-xl")
                ]
            ,}
        )

    def parse(self, response):
        for product in response.css("div.flex.flex-col.justify-center.items-center.mx-2.bg-white.shadow-blockShadow.p-7.mb-10.mt-10.rounded-xl"):
            item=MarketsItem()

            item["market_name"]='baraka'

            item["weight"]="SWORDBEK"

            item["price_unit"] = "SWORDBEK"

            item["image_url"]=product.css("div.w-full.\\!scale-95.transition-all.duration-200 > img.rounded-lg.mx-auto::attr(src)").get() or ""

            item["discount_period"]="mavjud"

            item["promotion_info"]=item["discount_period"]

            product_url=response.urljoin(product.css("a::attr(href)").get())
            item['url']= product_url or ""

            yield scrapy.Request(
                url=product_url,
                callback=self.parse_product,
                meta={"item":item}
            )

    def parse_product(self,response):
        item=response.meta['item']
        name=(response.css("div.flex.flex-col >h1.font-obold::text").get() or "").strip()
        item["product_name"]=name

        price_block = response.css("p.flex.gap-x-4.items-center.max-sm\\:flex-col")

        old_price_text = price_block.css("s::text").get()
        current_price_text = price_block.css("span::text").get()

    # Tozalaymiz (faqat raqamlarni olish uchun)
        def clean_price(text):
            if text:
                return float(text.replace("сум", "").replace(" ", "").strip())
            return 0.0

        old_price = clean_price(old_price_text)
        current_price = clean_price(current_price_text)

        discount_value = 0
        if old_price > 0:
            discount_value = (old_price - current_price) / old_price * 100

        item["old_price"] = old_price
        item["current_price"] = current_price
        item["discount"] = round(discount_value, 2)

        yield item

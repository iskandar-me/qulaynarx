import scrapy
import re
from markets.items import MarketsItem


class MakroSpider(scrapy.Spider):
    name = "makro"
    allowed_domains = ["makromarket.uz"]
    start_urls=["https://makromarket.uz/products"]


    def start_requests(self):
        url="https://makromarket.uz/products"
        yield scrapy.Request(
        url=url,
        callback=self.parse,
        meta={"playwright": True}
        )
    async def parse(self, response):
        page = response.meta["playwright_page"]

        # sahifani skroll qilish — lazy load uchun
        for _ in range(15):
            await page.mouse.wheel(0, 2000)
            await page.wait_for_timeout(1200)

        html = await page.content()
        await page.close()

        response = response.replace(body=html)

        for product in response.css("div.card"):
            item=MarketsItem()
            item["market_name"]='makro'

            item["product_name"]=(product.css("h3.title::text").get() or "N/A").strip()
            item["discount_period"]=(product.css("p.end-date::text").get() or "No discount").replace("\"","").strip()
            item["promotion_info"]=item['discount_period']
            item['old_price']=float(
                re.sub(
                    r"[^\d]",
                    "",
                    (product.css("span.old-price::text").get() or "0"),
                )
            )
            item['current_price']=float(
                re.sub(
                    r"[^\d]",
                    "",
                    (product.css("div.current-price::text").get() or "0"),
                )
            )
            item['price_unit']='SHOULD DEAL WITH THIS'
            item["discount"]=(product.css("div.smnthg > span.percent::text").get() or "N/A").replace("\"","").strip()
            item["weight"]="SHOULD DEAL WITH THIS"

            item["image_url"]=(product.css("div.imgCtr > img.card-img::attr(src)").get() or "N/A").strip()
            item["url"]=item["image_url"]
            yield item

import scrapy
import re
from markets.items import MarketsItem
from scrapy_playwright.page import PageMethod

scrolling_script = """
async ()=>{
    const delay= ms => new Promise(res=> setTimeout(res,ms));
    let previousHeight=0

    while(document.body.scrollHeight!==previousHeight){
        previousHeight=document.body.scrollHeight;
        window.scrollBy(0,4000);
        await delay(1000);
    }
}

"""


class MakroSpider(scrapy.Spider):
    name = "makro"
    allowed_domains = ["makromarket.uz"]
    start_urls = ["https://makromarket.uz/products?category=&region=3"]

    def start_requests(self):
        url = "https://makromarket.uz/products?category=&region=3"
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("evaluate", scrolling_script),
                    PageMethod("wait_for_selector", "div.card"),
                    PageMethod("screenshot",path="makro.png",full_page=True)
                ],
            },
            errback=self.errback
        )

    def parse(self, response):
        for product in response.css("div.card"):
            item = MarketsItem()
            item["market_name"] = "makro"

            item["product_name"] = (
                product.css("h3.title::text").get() or "N/A"
            ).strip()
            item["discount_period"] = (
                (product.css("p.end-date::text").get() or "No discount")
                .replace('"', "")
                .strip()
            )
            item["promotion_info"] = item["discount_period"]
            item["old_price"] = float(
                re.sub(
                    r"[^\d]",
                    "",
                    (product.css("span.old-price::text").get() or "0"),
                )
            )
            item["current_price"] = float(
                re.sub(
                    r"[^\d]",
                    "",
                    (product.css("div.current-price::text").get() or "0"),
                )
            )
            item["price_unit"] = "SHOULD DEAL WITH THIS"
            item["discount"] = (
                (product.css("div.smnthg > span.percent::text").get() or "N/A")
                .replace('"', "")
                .strip()
            )
            item["weight"] = "SHOULD DEAL WITH THIS"

            item["image_url"] = (
                product.css("div.imgCtr > img.card-img::attr(src)").get() or "N/A"
            ).strip()
            item["url"] = item["image_url"]
            yield item

    def errback(self, failure):
        self.logger.error(f"Playwright xatosi: {failure}")

import scrapy
import re
from markets.markets.items import MarketsItem

class KorzinkaSpider(scrapy.Spider):
    name = "korzinka"
    allowed_domains = ["korzinka.uz"]
    start_urls = ["https://korzinka.uz/uz/catalog"]
    def start_requests(self):
        url="https://korzinka.uz/uz/catalog"
        yield scrapy.Request(url,callback=self.parse, meta={'playwright': True})

    def parse(self, response):
        for product in response.css("div.product"):
            item=MarketsItem()
            item["market_name"] = "korzinka"

            item["discount_period"] = (
                (
                    product.css(
                        "div.product_tags >div.product__tag-primary_2::text"
                    ).get()
                    or "N/A"
                )
                .strip()
                .replace("<!---->", "")
            )

            item["promotion_info"] = (
                (
                    product.css(
                        "div.product_tags> div.product__tag-primary_5::text"
                    ).get()
                    or "No promotion"
                )
                .strip()
                .replace("<!---->", "")
            )

            item["old_price"] = float(
                re.sub(
                    r"[^\d]",
                    "",
                    (product.css("span.product__price-old > span::text").get() or "0"),
                )
            )
            item["current_price"] = float(
                re.sub(
                    r"[^\d]",
                    "",
                    (product.css("span.product__price-current::text").get() or "0"),
                )
            )
            item["price_unit"] = (
                product.css("span.product__price-type::text").get() or "N/A"
            ).strip()
            item["discount"] = (
                product.css("span.product__price-salestext::text").get()
                or "No discount"
            ).strip()
            item["product"] = (
                product.css("p.product__descr::text").get() or "N/A"
            ).strip()
            item["weight"] = (
                product.css("span.product__weight::text").get() or "Sold by weight"
            ).strip()
            item["url"] = (
                product.css("a.item__info--button.product__link::attr(href)").get()
                or "N/A"
            ).strip()

            img_url = (
                product.css("div.product__image > img::attr(src)").get() or "N/A"
            ).strip()
            if img_url != "N/A" and "https://" in img_url:
                img_url = img_url[img_url.index("https://") :]
            item["image_url"] = img_url

            yield item

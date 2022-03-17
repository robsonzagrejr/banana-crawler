import scrapy
import json


class JapaneseAlphabetSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.nhk.or.jp/lesson/pt/',
    ]

    def parse(self, response):
        alphabets_urls = response.xpath('//a[contains(@href,"alphabet")]')
        alphabets_urls += response.xpath('//a[contains(@href,"hiragana")]')
        alphabets_urls += response.xpath('//a[contains(@href,"katakana")]')
        yield from response.follow_all(alphabets_urls, callback=self.parse_alphabet)

        
    def parse_alphabet(self, response):
        divs = response.xpath('//div[contains(@class,"letters")]')
        uls = divs.xpath("descendant::node()/ul[contains(@class, 'letters')]")
        rows = uls.xpath("./li")
        alphabet_dict = {}
        i = 0
        for row in rows:
            alphabet_dict[i] = {
                "text": row.xpath("./img[@alt]/@alt").getall(),
                "image": row.xpath("./img[@src]/@src").getall(),
                "sound": [],
            }
            i += 1

        with open('banana_crawler/out/japanese_alphabet.json', 'w') as f:
            json.dump(alphabet_dict, f, indent=4)


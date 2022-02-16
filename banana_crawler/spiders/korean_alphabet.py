import scrapy
import json


class KoreanAlphabetSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.90daykorean.com/learn-korean/'
    ]

    def parse(self, response):
        alphabets_urls = response.xpath('//a[contains(.,"alphabet")]')
        yield from response.follow_all(alphabets_urls, callback=self.parse_alphabet)

        
    def parse_alphabet(self, response):
        #tables_consonant = response.xpath('//table[contains(.,"Consonant")]')
        #tables_vowel = response.xpath('//table[contains(.,"Vowel")]')
        tables = response.xpath('//table')
        rows = tables.xpath("./tbody/tr")
        alphabet_dict = {}
        i = 0
        for row in rows:
            alphabet_dict[i] = {
                "text": row.xpath("./td[not(a)]/text()").getall(),
                "image": row.xpath("descendant::node()/a/text()").getall(),
                "sound": row.xpath("descendant::node()/a/@data-audio-url").getall(),
            }
            i += 1

        with open('banana_crawler/out/korean_alphabet.json', 'w') as f:
            json.dump(alphabet_dict, f, indent=4)


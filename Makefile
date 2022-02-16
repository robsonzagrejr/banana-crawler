shell_url?=https://www.russianforeveryone.com/

install_local:
	pip3 install -r requirements.txt

install:
	pip3 install poetry
	poetry install

run_russian_alphabet:
	poetry run scrapy runspider banana_crawler/spiders/russian_alphabet.py

run_japanese_alphabet:
	poetry run scrapy runspider banana_crawler/spiders/japanese_alphabet.py

run_korean_alphabet:
	poetry run scrapy runspider banana_crawler/spiders/korean_alphabet.py

run_ref:
	poetry run scrapy runspider ref/quotes_spider.py -o ref/quotes.jl
	cat ref/quotes.jl

scrapy_shell:
	poetry run scrapy shell $(shell_url)


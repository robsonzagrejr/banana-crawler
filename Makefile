install_local:
	pip3 install -r requirements.txt

install:
	pip3 install poetry
	poetry install

run_ref:
	poetry run scrapy runspider ref/quotes_spider.py -o ref/quotes.jl
	cat ref/quotes.jl

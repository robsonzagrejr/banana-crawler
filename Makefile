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

clean_korean_alphabet:
	poetry run python src/postprocess_korean_alphabet.py \
		-f banana_crawler/out/korean_alphabet.json \
		-d assets/korean_alphabet/ \
		-o data/korean_alphabet.json

clean_japanese_alphabet:
	poetry run python src/postprocess_japanese_alphabet.py \
		-f banana_crawler/out/japanese_alphabet.json \
		-d assets/japanese_alphabet/ \
		-o data/japanese_alphabet.json

clean_russian_alphabet:
	poetry run python src/postprocess_russian_alphabet.py \
		-f banana_crawler/out/russian_alphabet.json \
		-d assets/russian_alphabet/ \
		-o data/russian_alphabet.json

gen_korean_alphabet:
	poetry run python src/anki_creator.py \
		-f data/korean_alphabet.json \
		-n korean_alphabet \
		-m assets/korean_alphabet/ \
		-o assets/ankidecks/korean_alphabet
	
gen_japanese_alphabet:
	poetry run python src/anki_creator.py \
		-f data/japanese_alphabet.json \
		-n japanese_alphabet \
		-m assets/japanese_alphabet/ \
		-o assets/ankidecks/japanese_alphabet
	
gen_russian_alphabet:
	poetry run python src/anki_creator.py \
		-f data/russian_alphabet.json \
		-n russian_alphabet \
		-m assets/russian_alphabet/ \
		-o assets/ankidecks/russian_alphabet
	
scrapy_shell:
	poetry run scrapy shell $(shell_url)


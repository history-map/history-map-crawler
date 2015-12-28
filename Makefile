all:    clean crawl

crawl:
	scrapy crawl building -o building.json

clean:
	rm -f *.json

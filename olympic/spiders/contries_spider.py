import scrapy


class ScrapeTableSpider(scrapy.Spider):
    name = 'contries'

    def start_requests(self):
        urls = [
            'https://www.whereig.com/olympics/medals/tokyo-2020-21-olympics-medal-table.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('/html/body/div/div[2]/main/section/div[2]/table[2]/tbody[1]/tr'):
            yield {
                'place': row.xpath('td[1]//text()').extract_first(),
                'country': row.xpath('td[1]//text()').extract_first(),
                'gold': row.xpath('td[2]//text()').extract_first(),
                'silver': row.xpath('td[3]//text()').extract_first(),
                'bronze': row.xpath('td[4]//text()').extract_first(),
                'total': row.xpath('td[5]//text()').extract_first(),
            }

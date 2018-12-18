# coding = 'utf-8'


import scrapy
from scrapy.spider import CrawlSpider
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # 项目的唯一名字
    # 可以爬取的域名，如果不是则会被过滤掉
    allowed_domains = ["quotes.toscrape.com"]
    # 包含Spider在启动时爬取的url列表
    start_urls = ['http://quotes.toscrape.com/']

    # 被调用时start_urls里面的链接构成的请求完成下载后，返回的response就会作
    # 为唯一的参数传递给这个函数，该方法负责解析返回的response，
    # 提取数据或者进一步生成要处理的请求。
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            # 使用Item，先impor，然后把item当做字典进行存储解析出来的数据
            item = QuoteItem()
            # text和author都是取第一个所以用extract_first，css('.class名::数据的类型')
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            # tags是要class内所有tag所以用extract()就可以了
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        # next是网页中下一个爬取的链接 attr()使得获取的事属性的值，而不是text这部分内容
        next = response.css('.pager .next a::attr(href)').extract_first()
        # urljoin将从网页获取的相对链接地址变为绝对的url
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)


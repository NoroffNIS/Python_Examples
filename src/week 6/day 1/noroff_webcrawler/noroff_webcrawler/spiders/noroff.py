# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from noroff_webcrawler.items import NoroffWebcrawlerItem
from scrapy.http import Request
import re


class NoroffSpider(scrapy.Spider):
    name = "noroff"
    allowed_domains = ["noroff.no"]
    start_urls = ['http://noroff.no/']

    def parse(self, response):
        hxs = Selector(response)

        # CODE for scraping book titles
        # book_titles = hxs.xpath('//div[@class="book-block-title"]/text()').extract()
        # for title in book_titles:
        #	book = NinjaCrawlerItem()
        #	book["title"] = title
        #	book["location_url"] = response.url
        #	yield book

        # CODE for scraping emails
        emails = hxs.xpath("//*[contains(text(),'@')]").extract()
        for email in emails:
            com = NoroffWebcrawlerItem()
            com["email"] = email
            com["location_url"] = response.url
            yield com


        visited_links = []
        links = hxs.xpath('//a/@href').extract()
        link_validator = re.compile(
            "^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

        for link in links:
            if link_validator.match(link) and not link in visited_links:
                visited_links.append(link)
                yield Request(link, self.parse)
            else:
                full_url = response.urljoin(link)
                visited_links.append(full_url)
                yield Request(full_url, self.parse)

# -*- coding: utf-8 -*-

# Scrapy settings for history-map project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'history-map'

SPIDER_MODULES = ['history-map.spiders']
NEWSPIDER_MODULE = 'history-map.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'history-map (+http://www.yourdomain.com)'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'

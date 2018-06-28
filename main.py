import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings



if __name__ == '__main__':
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='scraper.log',
        format='%(created) - f%(levelname)s: %(message)s',
        level=logging.INFO
    )
    process = CrawlerProcess(get_project_settings())
    process.crawl('Tomcat_7')
    process.crawl('Tomcat_8')
    process.crawl('Tomcat_9')
    process.crawl('TomcatNative')
    process.crawl('OpenSSL')
    process.crawl('Httpd')
    process.crawl('Curl')
    process.crawl('Connectors')

    process.start()

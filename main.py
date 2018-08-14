import logging

from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from utils.args import get_args


if __name__ == '__main__':
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='scraper.log',
        format='%(created) - f%(levelname)s: %(message)s',
        level=logging.INFO
    )
    process = CrawlerProcess(get_project_settings())
    process.crawl('Connectors',cmd_arguments=get_args())

    process.start()

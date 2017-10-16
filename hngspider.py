from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class HngSpider:

    # Class Variables (Shared among all instanes)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        HngSpider.project_name = project_name
        HngSpider.domain_name = domain_name
        HngSpider.base_url = base_url
        HngSpider.queue_file = HngSpider.project_name + '/queue.txt'
        HngSpider.crawled_file = HngSpider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', HngSpider.base_url)

    @staticmethod  # Since boot is a static method
    def boot():
        create_project_dir(HngSpider.project_name)
        create_data_files(HngSpider.project_name, HngSpider.base_url)
        HngSpider.queue = file_to_set(HngSpider.queue_file)
        HngSpider.crawled = file_to_set(HngSpider.crawled_file)

    @staticmethod  # Since crawl_page is also a static method
    def crawl_page(thread_name, page_url):
        if page_url not in HngSpider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(HngSpider.queue)) + '| crawled' + str(len(HngSpider.crawled)))
            HngSpider.add_links_to_queue(HngSpider.gather_links(page_url))
            HngSpider.queue.remove(page_url)
            HngSpider.crawled.add(page_url)
            HngSpider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(HngSpider.base_url, page_url)
            finder.feed(html_string)
        except:
            print ('Error: Unable to crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in HngSpider.queue:
                continue
            if url in HngSpider.crawled:
                continue
            if HngSpider.domain_name not in url:
                continue
            HngSpider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(HngSpider.queue, HngSpider.queue_file)
        set_to_file(HngSpider.crawled, HngSpider.crawled_file)






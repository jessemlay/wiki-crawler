import urllib2
from BeautifulSoup import BeautifulSoup
from urlparse import urljoin

class Crawler(object):
    user_agent = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.7) Gecko/2007091417 Firefox/2.0.0.7"

    crawled_urls = {}

    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    headers = {'User-Agent': self.user_agent}
                    req = urllib2.Request(page, headers=headers)
                    c=urllib2.urlopen(req)
                except urllib2.HTTPError, e:
                    print "Could not open %s" % page
                    print e
                    continue
                soup = BeautifulSoup(c.read())
                #self.addtoindex(page, soup)
            
                links=soup('a')
                for link in links:
                    if('href' in dict(link.attrs)):
                        url=urljoin(page, link['href'])
                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]
                        if url[0:4] == 'http':
                            newpages.add(url)
            pages = newpages
            self.crawled_urls[i] = newpages
        

crawler = Crawler()
crawler.crawl(['http://en.wikipedia.org/wiki/Main_Page/'], 2)
print crawler.crawled_urls
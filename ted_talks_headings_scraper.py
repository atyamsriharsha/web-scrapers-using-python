import urllib2

from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.ted.com/talks")

soup = BeautifulSoup(page)

link = soup.findAll(lambda tag: tag.name == 'a' and tag.findParent('dt', 'thumbnail'))

#for anchor in link.findAll('a', title = True):
#    print anchor['title']
for anchor in link:
    print anchor['title']

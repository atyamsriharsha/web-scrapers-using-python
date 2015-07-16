import random
import requests
from bs4 import BeautifulSoup
import urllib2
import re

def Clean(Href):
	Href = str(Href)
	temp = re.search('\?q=(.+?)\&', Href)
	Ans = temp.group(1)
	return Ans

def results(word1):
	start = 0
	while(start < 500): # Extracts data from only first page. If you want to get data from first n pages, change 10 to n*10.
		url = 'https://www.google.com/search?q='+word1+'&start='+str(start)
		Request = urllib2.Request(url)
		Request.add_header('User-agent', 'Mozilla 5.10')
		html = urllib2.urlopen(Request).read()
		soup = BeautifulSoup(html)
		try:
			H3 = soup.findAll('h3', {'class' : 'r'})
		except Exception:
			break
		if(len(H3) == 0): # No results.
			break
		for i in H3:
			temp = i
			A = temp.findAll('a')
			Href = A[0]['href']
			try:
				Href = Clean(Href)
				Contents = A[0].contents
				print ""
				print "Url :", Href
				print "Heading :",
				for j in Contents:
					try:
						temp = str(j)
						print temp.replace('<b>', '').replace('</b>', '').replace('\n', '').replace(' ', ''),
					except Exception:
						pass
				print "\n"
			except Exception:
				pass
		start += 10

word1 = raw_input("Please enter the word you want to search:\n")
results(word1)

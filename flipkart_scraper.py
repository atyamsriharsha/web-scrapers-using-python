import random
import requests
from bs4 import BeautifulSoup
import os
import webbrowser

def get_needed_tshirts(href,title,min_price,max_price):
	offer = 'No offer'
	flag = 0
	flag1 = 0
	if title!=None:
		flag1 = 1
		print (title   )
	url = href
	source_code1 = requests.get(url)
	plain_text1 = source_code1.text
	soup1 = BeautifulSoup(plain_text1)
	link1 = soup1.findAll('span',{'class':'selling-price omniture-field'})
	for x in link1:
		naa1 = 0
		ref1 = x.string
		ref2 = ref1[4:]
		ref3 = ref2.replace(',','')
		#print ref2
		if min_price<=ref3 and max_price>=ref3:
            #print("This is the selling Price")
		    print(x.string)
		    naa1 = 1
		    print ('\n')
		    break

	link2 = soup1.findAll('span',{'class':'price'})
	for x in link2:
		if naa1 is 1:
		    print ("This is the original Price ")
		    print x.string
		    print ('\n')
		    break

	link3 = soup1.findAll('span',{'class':'discount fk-green'})
	for x in link3:
		flag = 1
		if naa1 is 1:
		    print ("The Discount is ")
		    print x.string
		    print ('\n')
		    break

	if flag==0:
		if flag1==1:
		    print offer
		    print ('\n')

	link4 = soup1.findAll('img',{'class':'imgWrapper'})
	

def get_niketshirts(min_price,max_price):
	url = 'http://www.flipkart.com/mens-clothing/t-shirts/pr?p%5B%5D=facets.brand%255B%255D%3D'+'Nike'+'&sid=2oq%2Cs9b%2Cj9y&filterNone=true'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a',{'class':'fk-display-block'}):
		if link.get('href')!='javascript:void(0);':
		  href = 'http://www.flipkart.com'+link.get('href')
		  title = link.get('title')
		  if title!=None:
		    get_needed_tshirts(href,title,min_price,max_price)


def get_pepe_jeans_tshirts(min_price,max_price):
	url = 'http://www.flipkart.com/mens-clothing/t-shirts/pr?p%5B%5D=facets.brand%255B%255D%3D'+'Pepe'+'&sid=2oq%2Cs9b%2Cj9y&filterNone=true'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a',{'class':'fk-display-block'}):
		if link.get('href')!='javascript:void(0);':
		  href = 'http://www.flipkart.com'+link.get('href')
		  title = link.get('title')
		  if title!=None:
		    get_needed_tshirts(href,title,min_price,max_price)


def get_lee_tshirts(min_price,max_price):
	url = 'http://www.flipkart.com/mens-clothing/t-shirts/pr?p%5B%5D=facets.brand%255B%255D%3D'+'Lee'+'&sid=2oq%2Cs9b%2Cj9y&filterNone=true'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('a',{'class':'fk-display-block'}):
		if link.get('href')!='javascript:void(0);':
		  href = 'http://www.flipkart.com'+link.get('href')
		  title = link.get('title')
		  if title!=None:
		    get_needed_tshirts(href,title,min_price,max_price)
		

print ('-------------Available Brands-----------')
print ('---LEE\n---PEPEJEANS\n---NIKE\n---FLYINGMACHINE\n---REEBOK\n')
print ('Choose Your Brand:\n')
brand = raw_input()
print ('------------Available Sizes------------')
print ('--M\n--L\n--XL\n--XXL\n')
size = raw_input()
print ('------------Enter the Minimum Price------')
min_price = raw_input()
print('\n')
print ('------------Enter the Maximum Price------')
max_price = raw_input()
print ('\n')

if brand.upper()=='NIKE':
  get_niketshirts(min_price,max_price)

elif brand.upper()=='PEPE':
  get_pepe_jeans_tshirts(min_price,max_price)

elif brand.upper()=='LEE':
   get_lee_tshirts(min_price,max_price) 

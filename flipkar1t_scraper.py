import random
import requests
from bs4 import BeautifulSoup


def get_tshirts(brand,size_of_goodie_needed,min_price,max_price,colour):
	tshirts_url = 'http://www.flipkart.com/mens-clothing/'+brand+'~brand/~shirts/pr?p%5B%5D=facets.price_range%255B%255D%3DRs.%2B'+min_price+'%2B-%2BRs.%2B'+max_price+'&p%5B%5D=facets.color%255B%255D%3D'+colour+'&sid=2oq%2Cs9b&filterNone=true'
	source_code_tshirts = requests.get(tshirts_url)
	plain_text_tshirts = source_code_tshirts.text
	soup_tshirts = BeautifulSoup(plain_text_tshirts)
	for x in soup_tshirts.findAll('a',{'class':'fk-display-block'}):
		href = 'http://www.flipkart.com'+link.get('href')
		if link.get('href')!='javascript:void(0);':
		  title = link.get('title')
		  offer = 'No offer'
		  flag = 0
		  flag1 = 0
		  print offer
		  if title!=None:
		    flag1 = 1
		    print (title)
		    source_code_tshirts_1 = requests.get(href)
	        soup_tshirts1 = source_code_tshirts_1.text
	        tshirts_link = soup_tshirts1.findAll('span',{'class':'selling-price omniture-field'})
	        for x in tshirts_link:
		      print x.string
		      print '\n'
		      tshirts_link2 = soup_tshirts1.findAll('span',{'class':'price'})
		      print(tshirts_link2)
		      for x in tshirts_link2:
		        print x.string
		        tshirts_link3 = soup_tshirts1.findAll('span',{'class':'discount fk-green'})
		        for x in tshirts_link3:
		        	flag = 1
		        	print x.string
		        	print ('\n')


def get_shirts(brand,size_of_goodie_needed,min_price,max_price,colour):
	'''
	offer = 'No offer'
	flag = 0
	flag1 = 0
	if title!=None:
		flag1 = 1
		print (title   )
	'''
	shirts_url = 'http://www.flipkart.com/mens-clothing/'+brand+'~brand/~shirts/pr?p%5B%5D=facets.price_range%255B%255D%3DRs.%2B'+min_price+'%2B-%2BRs.%2B'+max_price+'&p%5B%5D=facets.color%255B%255D%3D'+colour+'&sid=2oq%2Cs9b&filterNone=true'
	source_code_shirts = requests.get(shirts_url)
	plain_text_shirts = source_code_shirts.text 
	soup_shirts = BeautifulSoup(plain_text_shirts)
	shirts_link = soup_shirts.findAll('span',{'class':'selling-price omniture-field'})
	for x in shirts_link:
	 	print x.string
	 	print '\n' 
	shirts_link2 = soup_shirts.findAll('span',{'class':'price'})
	for x in shirts_link2:
		print x.string
	print(shirts_link2)
	shirts_link3 = soup_shirts.findAll('span',{'class':'discount fk-green'})
	for x in shirts_link3:
		flag = 1
		print x.string
		print ('\n')
	'''if flag==0:
		if flag1==1:
		 print offer
		 print ('\n')
    '''
	print(shirts_link3)
	
'''def get_jeans(brand,size_of_goodie_needed,min_price,max_price,colour):
    offer = 'No offer'
	flag = 0
	flag1 = 0
	print offer
	if title!=None:
		flag1 = 1
		print (title   )
    get_fit = raw_input("Please enter the fit you like:\nWe have Regular Slim Skinny\n")
	jeans_url =  'http://www.flipkart.com/mens-clothing/jeans/'+brand+'~brand/pr?p%5B%5D'+'=facets.fit%255B%255D%3D'+get_fit+'%2BFit&p%5B%5D=facets.price_range%255B%255D%3DRs.%2B'+min_price+'%2B-%2BRs.%2B'+max_price+'&p%5B%5D=facets.color%255B%255D%3D'+colour+'&sid=2oq%2Cs9b%2C94h&filterNone=true'
    source_code_jeans = requests.get(jeans_url)
    plain_text_jeans = source_code_jeans.text
    soup_jeans = BeautifulSoup(plain_text_jeans)
    jeans_link = soup_jeans.findAll('span',{'class':'selling-price omniture-field'})
    for x in jeans_link:
    	print x.string
    	print '\n'
    jeans_link2 = soup_jeans.findAll('span',{'class':'price'})
	for x in jeans_link2:
		print x.string
	print(jeans_link2)
	jeans_link3 = soup_jeans.findAll('span',{'class':'discount fk-green'})
	for x in jeans_link3:
		flag = 1
		print x.string
		print ('\n')
	if flag==0:
		if flag1==1:
		 print offer
		 print ('\n')
	print(jeans_link3)
'''



def results(type_of_goodie,brand,size_of_goodie_needed,min_price,max_price,colour):
	if type_of_goodie.upper() == 'SHIRTS':
		get_shirts(brand,size_of_goodie_needed,min_price,max_price,colour)
	elif type_of_goodie.upper() =='T-SHIRTS':
		get_tshirts(brand,size_of_goodie_needed,min_price,max_price,colour)
	elif type_of_goodie.upper() == 'JEANS':
		get_jeans(brand,size_of_goodie_needed,min_price,max_price,colour)



type_of_goodie = raw_input("Please enter what you want:\nwe have:\n T-shirts  shirts  Jeans\n ")
brand = raw_input("Please enter the brand you want to search:\n")
size_of_goodie_needed = raw_input("Please enter the size of the product:\n we have S M L XL XXL \n")
min_price = raw_input("Please enter the minimum price:\n")
max_price = raw_input("Please enter the maximum price:\n")
colour = raw_input("Please enter the colour you want:\nWe have Black Blue Red Green Yellow Orange Violet Pink")
results(type_of_goodie,brand,size_of_goodie_needed,min_price,max_price,colour)

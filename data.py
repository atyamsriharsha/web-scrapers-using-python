import random
import requests

url1 = "https://www.facebook.com/atyam.sriharsha/friends_all"

def download_stock_data(csv_url):
	response  = urllib.request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r'goog1.csv'
	fx = open(dest_url,"w")
	for line in lines:
		fx.write(line+"\n")
	fx.close()

download_stock_data(url1)  

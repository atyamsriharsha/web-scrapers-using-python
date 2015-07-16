import random
import urllib.request


def download_pics(url):
	name = random.randrange(1,1000)
	fullname = str(name) + ".jpg"
	urllib.request.urlretrieve(url,fullname)

download_pics('https://www.facebook.com/photo.php?fbid=712450538841880&set=pb.100002308212973.-2207520000.1434732726.&type=3&theater')

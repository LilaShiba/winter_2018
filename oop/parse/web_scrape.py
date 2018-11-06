import bs4, requests
# beauitful soup for parse
class Parsey(object):

	def __init__(self, url, find_me):
		# object as url and css selector
		self.url = url
		self.find_me = find_me

	def get_url(self):
		# Go to website
		res = requests.get(self.url)
		# Display to user
		print('going to %s'%(self.url))
		# Find requested data
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		# use css selector to locate
		elems = soup.select(self.find_me)
		print(elems[0].text)
		print('')

	# Example of mass loop
	  #	for link in soup.find_all('a'):
		#	print(link.get('href'))

		

# Create objects
jobs = Parsey('https://www.dwight.edu/about/employment-opportunities', '#fsEl_5489 > div > ul')
nytimes = Parsey('https://www.nytimes.com/', '#topnews-100000005850994 > h2 > a')
#wpost = Parsey('https://www.washingtonpost.com', '#f0MlwiA4gKaLOq > div > div > div.headline.small.normal-style.text-align-inherit > a')

# Call
Parsey.get_url(jobs)
Parsey.get_url(nytimes)
#Parsey.get_url(wpost)




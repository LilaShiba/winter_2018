import bs4, requests

class Movies(object):

	def __init__(self,url,css):
		self.url = url
		self.css = css
		self.name = url[8:15]

	def get_times(self):
		# download site
		res = requests.get(self.url)
		# print confirmation
		print('headed to %s which I will call %s'%(self.url, self.name))
		# parse data
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
		self.elems = soup.select(self.css)
		print(self.elems[0].text)
		print('')

	def compare(self, other):
		pass 



alamo = Movies('https://drafthouse.com/nyc/calendar/downtown-brooklyn', 'h1')
Movies.get_times(alamo)

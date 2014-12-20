import bs4
import requests

response = requests.get("http://www.uniqlo.com/us/men/featured/weekly-promotions.html")
soup = bs4.BeautifulSoup(response.text)
items = soup.select('div.product-detail-container')

def collectItems(items):
	lst = []

	for item in items:

		originalPrice = item.findAll('span')[0].text.strip().strip("$")
		salesPrice = item.findAll('span')[1].text.strip().strip("$")

		originalPrice = float(originalPrice)
		try: 
			salesPrice = float(salesPrice)
		except:
			salesPrice = 1000000

		name = item.findAll('a')[0].text.strip()
		newItem = {"name": name, "originalPrice": originalPrice, "salesPrice": salesPrice, 
					"discount": str(salesPrice/originalPrice) + "%"}

		lst += [newItem]

	return lst

"""
// item1('span', limit=2)[0]
// item1('span')[0]

// for node in item1.findAll('span'):
//     print("separate node: " + node.text)
"""
# strip removes white space and new lines
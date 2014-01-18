import lxml.html as parser
import requests

def fetch_page(url):
	"""
	Fetch the page from the given URL, and return the HTML as a string.
	"""
	try:
		page = requests.request('GET', url, timeout=2000, allow_redirects=True)
	except:
		return None

	if page.status_code is 200:
		return page.content

def extract_meta(page):
	"""
	Parse the HTML and extract the meta information.
	"""

	DESCRIPTORS_NAME = ('name', 'property', 'itemprop')
	DESCRIPTORS_VALUE = ('content')

	meta_list = []

	if page:
		tree = parser.fromstring(page)
		meta = tree.findall('head')[0].findall('meta')

		if meta:
			for tag in meta:
				for attribute in tag.attrib.keys():
					if attribute in DESCRIPTORS_NAME:
						meta_list.append({'name' : tag.attrib[attribute], 'value' : tag.attrib['content']})
					elif attribute == 'charset':
						meta_list.append({'name' : 'charset', 'value' : tag.attrib['charset']})
                        return meta_list, "OK"
		else:
			return [], "NO METADATA FOUND"

	else:
		return [], "INVALID HOST"

def extract_meta_prop(page, prop):
	meta_list, status = extract_meta(page)

	for field in meta_list:
		if prop == field['name']:
			return field, "OK"

	return [], "NO METADATA FOUND"


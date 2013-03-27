import httplib
import urllib
import json
from xml.dom.minidom import Document

params = urllib.urlencode({"q": "{query}"})
conn = httplib.HTTPConnection("movie.douban.com", 80)
conn.request("GET", "/j/subject_suggest?"+params)
response = conn.getresponse()
data = response.read()
conn.close()

dataobj = json.loads(data)
doc = Document()
items = doc.createElement("items")
for item in dataobj:
	title = item["title"]
	if "year" in item:
		title = title + " (" + item["year"] + ")"
	xmlitem = doc.createElement("item")
	xmlitem.setAttribute("uid", item["url"])
	xmlitem.setAttribute("arg", item["url"])
	xmlitem.setAttribute("autocomplete", item["title"])
	xmlitem.setAttribute("valid", "YES")
	attr = doc.createElement("title")
	attr.appendChild(doc.createTextNode(title))
	xmlitem.appendChild(attr)
	attr = doc.createElement("subtitle")
	attr.appendChild(doc.createTextNode(item["sub_title"]))
	xmlitem.appendChild(attr)
	attr = doc.createElement("icon")
	attr.appendChild(doc.createTextNode("icon.png"))
	xmlitem.appendChild(attr)
	items.appendChild(xmlitem)

doc.appendChild(items)
print unicode(doc.toxml()).encode("utf-8")

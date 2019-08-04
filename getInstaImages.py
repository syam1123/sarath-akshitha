import urllib
import re
import json
link = "https://www.instagram.com/explore/tags/alappuzha"
f_name = "dist/_nuxt/instaimages.json"
json.dump(re.findall(r'https?://\S+?.jpg[^"]+',str(urllib.request.urlopen(link).read())),open(f_name,"w"))




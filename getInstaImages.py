import urllib.request
import re
import json
link = "https://www.instagram.com/explore/tags/saraakshi"
f_name = "dist/_nuxt/instaimages.json"
resultHTML  = str(urllib.request.urlopen(link).read())
images = sorted(re.findall(r'https?://[^x\s]+?.jpg[^"]+',str(resultHTML)))[::2]
json.dump(images,open(f_name,"w"))

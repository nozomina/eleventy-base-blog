import json

with open("names.json") as f:
  d = json.loads(f.read())

#print(d.keys())

for unit in d.keys():
  url = "https://redive.estertion.win/icon/unit/%s.webp" % unit
  print("wget %s" % url)

import requests
import pprint

base_url = "http://datapoint.metoffice.gov.uk/public/data/{stuff}?key={api_key}"
api_key = "b7d01371-4991-43ba-acad-d7c6047a9247"
stuff = "val/wxfcs/all/json/sitelist"

data = requests.get(base_url.format(stuff=stuff, api_key=api_key))
print(data.status_code)
pprint.pprint(data.json())

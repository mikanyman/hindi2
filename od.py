# -*- coding: utf-8 -*-

# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import urllib  # This I have added

app_id = '5af53e25'
app_key = '2ab150726abb7eb5a6ac96e4d2e71056'

language = 'hi'
query = 'नमस्ते'
word_id = urllib.quote(query)  # %E0%A4%A8%E0%A4%AE%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%87

url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))


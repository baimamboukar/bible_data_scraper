# import json
# data = {
#     "Alkawal Kessal":{
#         "MATTA":{
#             "1": "Nda indee kaakirabr Yeesu Almasihu"
#         }
#     }
# }
# datax = {}
# datax['Alkawal Kessal'] = {}
# datax['Alkawal Kessal']['MARKUS'] = {}
# datax['Alkawal Kessal']['MARKUS']['1'] = "Linjila bana no Markus windi doum"
# print(datax['Alkawal Kessal'])

import requests
from bs4 import BeautifulSoup
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'referer': 'https://www.google.com/'
}

res = requests.get(
    "http://webcache.googleusercontent.com/search?q=cache:my.bible.com/fr/bible/906/GEN.12.FB", headers=header)
soup = BeautifulSoup(res.text, "html.parser")
pretty_soup = soup.prettify()
verse_tags = soup.findAll("span", {"class": "content"})
total_verses = len(verse_tags)
print(f"TOTAL VERSES : {total_verses}")

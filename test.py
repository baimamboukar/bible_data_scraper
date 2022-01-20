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

res = requests.get("https://my.bible.com/fr/bible/906/GEN.1.FB")
print(res)

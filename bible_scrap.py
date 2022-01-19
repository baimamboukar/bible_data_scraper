#coding: utf-8
import json
import os
import requests
import codecs
from bs4 import BeautifulSoup

books = ["MAT-28-Matta", "MRK-16-Markus", "LUK-24-Luka",
         "JHN-21-Yuhanna", "ACT-28-Kuude Neelabe"]
BASE_LINK = "https://my.bible.com/fr/bible/906/"

bible_json = {
    "Alkawal Kessal": {},
    "Alkawal Kidngal": {}
}

for book in books:
    splited = book.split("-")
    book_code = splited[0]
    number_of_chapters = int(splited[1])
    book_name = splited[2]
    bible_json["Alkawal Kessal"][book_name] = {}
    for chapter in range(number_of_chapters):
        chapter_name = book_name + " " + str(chapter + 1)
        bible_json["Alkawal Kessal"][book_name][chapter_name] = {}
        chapter_link = BASE_LINK + book_code + "." + str(chapter + 1) + ".FB"
        response = requests.get(chapter_link)
        soup = BeautifulSoup(response.text, "html.parser")
        pretty_soup = soup.prettify()

        verse_tags = soup.findAll("span", {"class": "content"})
        total_verses = len(verse_tags)
        print("TOTAL VERSES", total_verses)
        # for verse_index in range(total_verses):
        #     print(verse_tags[verse_index].text)
        # if verse_tags[verse_index].text == " " or ". " or ".”" or "." or ": ":
        #     verse_tags.pop(verse_in dex)

        for index in range(total_verses):
            print(index + 1)
            print(": " + verse_tags[index].text)
            # if(verse_tags[index].text not in [" ", ". ", ".", ", ", "!", ".”", ": "]):
            bible_json["Alkawal Kessal"][book_name][chapter_name][str(
                index)] = verse_tags[index].text


with codecs.open("bible.json", "w", "utf-8") as bible:
    pretty_json = json.dumps(bible_json, sort_keys=False,
                             indent=4, ensure_ascii=False)
    data_written = json.loads(pretty_json)
    bible.write(pretty_json)
    print(pretty_json)

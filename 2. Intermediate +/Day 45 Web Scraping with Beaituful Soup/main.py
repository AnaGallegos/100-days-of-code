from bs4 import BeautifulSoup
import requests

#  Website to be scraped
WEBSITE = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(WEBSITE)
movies_site = response.text

soup = BeautifulSoup(movies_site, 'html.parser')

# Get all titles (nested in a h3 tag)
song_titles_tags = soup.find_all(name='h3', class_='c-title')

#  Iterate through tags and put it in a list
song_list = [tag.getText() for tag in song_titles_tags]


print(song_list)

















# with open("website.html",  encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')



# # all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     print(tag.get("href")) # Links
# #     print(tag.getText()) # Anchored text

# # heading = soup.find(name="h1", id="name")
# # print(heading)


# # Select by id
# # name = soup.select_one(selector="#name")
# # print(name)

# # Select by class
# headings = soup.select(".heading")
# print(headings)
import json
import codecs
from brinfluence.lib import data_utils
import re

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)



string = "rnothing 4x4 🏼 ️ offroading cllinrollin luxury 🏼 enjoylife bekind "
print(string)
#string = emoji_pattern.sub(r'',string)
string = data_utils.remove_emojis(string)
string = data_utils.remove_special_char(string)
string = data_utils.remove_multiple_whitespace(string)
print(string)


'''
root_dir = "C:\\Users\hp\Desktop\Scraper"

path_to_user = root_dir + "\@nike\profile.json"

with open(path_to_user, mode="r", encoding="utf-8") as f:
    data = json.load(f)

print(data['graphql']['user']['business_category_name'])

data = json.load(codecs.open(root_dir + "\cocacola\cocacola.json", 'r', 'utf-8-sig'))

for obj in data:
    for media in obj['edge_media_to_caption']['edges']:
        print(media['node']['text'])

print("\nCOMMENTS")
for obj in data:
    for comment in obj['comments']['data']:
        print(comment['owner']['username'])
        print(comment['text'])
'''
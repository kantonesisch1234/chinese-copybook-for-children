import requests
from bs4 import BeautifulSoup
import json
import os
import sys
        
def download_image_from_word(word,attempts=10):
    url = "https://hk.images.search.yahoo.com/search/images?p=" + word

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    div_list = soup.find("div", class_="sres-cntr").find_all("li")
    img_links_length = min(attempts, len(div_list))
    img_links = [json.loads(div_list[i]['data'])['iurl'] for i in range(img_links_length)][:img_links_length]

    if not os.path.exists('pics'):
        os.makedirs('pics')

    if not os.path.exists('pics/'+word):
        os.makedirs('pics/'+word)

    directory = 'pics/'+word

    for idx,img_link in enumerate(img_links):
        try:
            response = requests.get(img_link)
            # img_file_type = '.'+img_link.split('.')[-1].split('?')[0].split('/')[0]
            img_file_type = '.jpg'
            file = open(directory + "/" + word+"_0" + str(idx+1) + img_file_type , "wb")
            file.write(response.content)
            file.close()
            print("Image downloading for " + word + " successful at " + str(idx+1) +". attempt.")
        except Exception as e:
            print(e)
            print("Error downloading image for " + word +" at " + str(idx+1) + "attempt.")
            
def download_image_from_wordlist(attempts):
    with open("wordlist.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        download_image_from_word(line.strip('\n'),attempts)
    
if __name__ == '__main__':
    download_image_from_wordlist(int(sys.argv[1]))
  
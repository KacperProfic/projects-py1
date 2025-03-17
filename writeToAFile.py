import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features='lxml')
 
filename = input("Podaj nazwe pliku: ") + ".txt"

with open(filename, 'a', encoding='utf-8') as open_file:
    for story_heading in soup.find_all(class_="story-heading"): 
        if story_heading.a: 
        
            open_file.write(story_heading.a.text.replace("\n", " ").strip())
        else: 
        
            open_file.write(story_heading.contents[0].strip())
print(f"Plik został zapisany jako: {filename}")
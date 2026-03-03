from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import time

def scraper(url):

    if not url.startswith("http"):
        url="https://"+url

    opt=Options()
    opt.add_argument("--headless")
    opt.add_argument("--log-level=3") 

    driver = webdriver.Chrome(options=opt)
    driver.get(url)

    time.sleep(2)

    html=driver.page_source
    driver.quit()

    soup=BeautifulSoup(html,"html.parser")

    t=soup.find("title")
    if t:
        print(t.text.strip())
    else:
        print()

    b = soup.find("body")
    if b:
        print(b.text.strip())
    else:
        print()

    links=soup.find_all("a")
    for link in links:
        href=link.get("href")
        if href:
            print(href)

if __name__=="__main__":

    if len(sys.argv)!=2:
        print("Please provide a URL")
        sys.exit()

    url=sys.argv[1]
    scraper(url)
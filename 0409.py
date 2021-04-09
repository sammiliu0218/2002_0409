import requests
import time 
for bs4 import beautifulsoup

URL="https://www.majortests.com/word-lists/word-list-01.html"
def generate_urls(ur1, start_page, end_page):
    urls = []
    for page in rang (start_page, end_page):
        urls.append(url.format(page))
    retuen urls
def get_resource(url):
    headers = {
        "user-agent":"Mozilla/5.0 (windows NT 10.0; Win64; x64) ApplWebkit/537.36(KHTML,like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    return requests.get(url, headers=headers)

def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")

    if __name__=="__main__":
        urlx=generate_urls(URL,1,2)
        for url in urlx:
            file=url.splite("/")[-1]
            print("catching:",file,"web data...")
            r=get_resource(url)
            if r.status_code==requests.codes.ok:
                soup=parse_html(r.text)
                words=[]
                count=0
                for wordlist_table in soup.find_all(class_="wordlist"):
                    count+=1
                    for word_entry in wordlist_table.find_all("tr"):
                        new_word=[]
                        new_word.append(file)
                        new_word.append(str(count))
                        new_word.append(word_entry.th.text)
                        new_word.append(word_entry.td.text)
                        words.append(new_word)
                    print(words)
                    print("____________\n\n")
                else:
                    print("HTTP request error!!")
                print("sleep 5 second")
                time.sleep(5)

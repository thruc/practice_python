import requests



url = "https://www.oxfordlearnersdictionaries.com/spellcheck/english/"
# url = "https://www.google.com/"
word = "daffiest"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

q = {'q':  word}
r = requests.get(url,params=q ,headers=headers)
print(r.text)
print(r.url)
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# rp.set_url("https://www.oxfordlearnersdictionaries.com/robots.txt")
# rp.read()
# rrate = rp.request_rate("*")
# print(rrate.requests)
# print(rrate.seconds)
# print(rp.crawl_delay("*"))
# print(rp.can_fetch("*", "https://www.oxfordlearnersdictionaries.com/"))
with open("t.html", mode="a",encoding="utf-8_sig") as f:
        f.write(r.text)
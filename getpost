import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import configs
import re
allposts= configs['allposts']
URL = allposts 
def login(login):
    session = requests.Session()


    resp = session.get(URL)
    soup = BeautifulSoup(resp.content, "html5lib")

    form = soup.find('form') 

    fields = form.findAll("input")

    data = dict(( field.get("name"), field.get("value")) for field in fields)

    data["log"] = login[0] 
    data["pwd"] = login[1] 
    postURL = urljoin(URL, form["action"])
    r = session.post(postURL, data=data)
    if r == "<Response [401]>":
        print("got error 401")

    return r





def post(user):
    r = login(user)

    html = BeautifulSoup(r.text, "html.parser")

    posts = html.findAll("a", {"class": "nolink"})
    post_list = []
    for i,post in enumerate(posts):
        if i != 0:
            post_link = post['href']
            #lets see if it will work
            h2 = post.find("h2")
            texts  = str(h2)[str(h2).find(">")+1:]
            texts  = texts[str(texts).find(">")+1:]
            author = texts[0:str(texts).find("<")]
            texts = texts[str(texts).find(">")+1:]
            title = texts[0:str(texts).find("<")]
            title = title.replace(" - ", "")
            post_list.append([author,title,post_link])       
    return post_list




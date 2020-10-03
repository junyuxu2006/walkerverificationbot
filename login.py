#discord supports instagram emb
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import configs
searchlink = configs['searchlink']
def login(login, URL):
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
    print(r)
    print(type(r))
    if str(r) == "<Response [401]>":
        print("Error 401")
        captcha(soup)
    return r

def captcha(html):
    print("got in the captcha function")
    question = html.find("span", {"style": "vertical-align:super;"})
    print("got the question")
    print(question)
    nospace = str(question).replace(" ","")
    print(nospace)

def comments(user, URL):
    r = login(user, URL)

    html = BeautifulSoup(r.text, "html.parser")

    comments = html.findAll("li", {"class": "comment"})
    tokens_list = []
    for comment in comments:
        found_token = comment.find("p").text
        found_id = comment.find("span", {"class": "wid"}).text
        tokens_list.append([found_id,found_token])

    return tokens_list

def post(user,URL):
    r = login(user,URL)

    html = BeautifulSoup(r.text, "html.parser")

    posts = html.findAll("a", {"class": "nolink"})
    post_list = []
    for i,post in enumerate(posts):
        if i != 0:
            post_link = post['href']
            h2 = post.find("h2")
            texts  = str(h2)[str(h2).find(">")+1:]
            texts  = texts[str(texts).find(">")+1:]
            author = texts[0:str(texts).find("<")]
            texts = texts[str(texts).find(">")+1:]
            title = texts[0:str(texts).find("<")]
            title = title.replace(" - ", "")
            post_list.append([author,title,post_link])       
    return post_list

def post_contents(user, URL):
    r = login(user,URL)

    html = BeautifulSoup(r.text, "html.parser")

    nameIT = html.find("article", {"id": "forum-single"}).text
    description = nameIT.replace("Report", "")
    return description

def searchPost(user, toSearch, max=10):
    r = login(user,f"{searchlink}{toSearch}")#run
    html = BeautifulSoup(r.text, "html.parser")
    posts = html.findAll("a", {"class": "nolink"})
    post_list = []
    
    for i,post in enumerate(posts):
        if i != 0:
            post_link = post['href']
            h2 = post.find("h2")
            texts  = str(h2)[str(h2).find(">")+1:]
            texts  = texts[str(texts).find(">")+1:]#run
            author = texts[0:str(texts).find("<")]
            texts = texts[str(texts).find(">")+1:]
            title = texts[0:str(texts).find("<")]
            title = title.replace(" - ", "")
            post_list.append([author,title,post_link])
            if i == max:
                return post_list    
    return post_list
            

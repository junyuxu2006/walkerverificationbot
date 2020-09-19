import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import configs
URL = configs['commenturl']
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
    return r

def comments(user):
    r = login(user)

    html = BeautifulSoup(r.text, "html.parser")

    comments = html.findAll("li", {"class": "comment"})
    tokens_list = []
    for comment in comments:
        found_token = comment.find("p").text
        found_id = comment.find("span", {"class": "wid"}).text
        tokens_list.append([found_id,found_token])

    return tokens_list

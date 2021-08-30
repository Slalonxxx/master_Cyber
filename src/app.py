from flask import Flask
import requests
from bs4 import BeautifulSoup as b
url='https://finance.yahoo.com/quote/DIS?p=DIS&.tsrc=fin-srch'
html= requests.get(url)
content=html.content
soup= b(content,"lxml")
precio=soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
rango=soup.find("span",{"class":"Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})

app = Flask(__name__)

@app.route("/")
def index():
    return "Valor Disney:"+ str(precio.txt)


if __name__ == "__main__":
    app.run()

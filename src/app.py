from flask import Flask
import requests
from bs4 import BeautifulSoup as b


app = Flask(__name__)

@app.route("/")
def index():
    url='https://finance.yahoo.com/quote/DIS?p=DIS&.tsrc=fin-srch'
    html= requests.get(url)
    content=html.content
    soup= b(content,"lxml")
    precio=soup.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    rango=soup.find("span",{"class":"Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})
    return "Valor Disney:"+ str(precio.text)


if __name__ == "__main__":
    app.run()

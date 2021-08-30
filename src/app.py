from flask import Flask, render_template

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
def home():
	data={
		'curso' : 'CyberFisicos',
		'nombre':'Edison',
		'precio': str(precio.text),
		'rango': str(rango.text) 
	}
	
	return render_template('reto1.html', data=data)
   
if __name__ == '__main__':
	app.run()
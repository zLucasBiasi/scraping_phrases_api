from bs4 import BeautifulSoup
import requests
from flask import Flask,jsonify

app = Flask(__name__)

@app.route(f"/frases/<int:id>",methods=['GET'])
def phrases(id):
    url = f'https://www.pensador.com/frases_filosofos/{id}'

    res = requests.get(url)

    html_page = res.text

    soup = BeautifulSoup(html_page,'html.parser')

    phrase_list = soup.find_all('p')
  
    list = []
    for phrase in phrase_list:
        new_list = phrase.text
        list.append(new_list.replace("\n",""))
    
    return jsonify(list)
        

app.run(port=5000, host='localhost', debug=True)

import json
from unicodedata import name
import requests 
import time
import psycopg2 

conection = psycopg2.connect(database="postgres", user="postgres", password="registro12", host="127.0.0.1", port="5432")
def get_service(): 
    response = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1154') 
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
        if results:
            for pokemon in results:
                name = pokemon['name']
                print (name)
                write_db(name)
    pass


def write_db(name):
   cursor = conection.cursor()
   sql="INSERT INTO pokemones(nombre) VALUES (%s)"
   map= name
   cursor.execute(sql,(json.dumps(map),))
   conection.commit()
pass


if __name__=="__main__":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)
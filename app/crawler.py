from bs4 import BeautifulSoup
import requests

def get_count():

    url = "https://swimpool.nctu.edu.tw/NCTUGym/index.php/anchor/fitness"
    r = requests.get(url)

    

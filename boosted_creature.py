import schedule
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def criatura_dia():
  #Aqui ele esta indo no site do Jogo e verificando qual é a criatura
  URL = "https://san.taleon.online/index.php"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  
  #armazenamos o nome da criatura na variavel result
  result = soup.find('div', {'id':'boosted-creature'})  
  #aqui aproveitamos para pegar o link de outro site onde está hospedado seu gif
  img_url = soup.find('div', {'id':'boosted-creature'}).find('a')['href']
  bixo = result.text


  #Como o proximo site ele tem uma proteção da CLoudfire, por isso usaremos o SELENIUM
  #Assim conseguimos acessa-lo e pegarmos essas informações
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  #Aqui pegamos a informção do link e 
  dr = webdriver.Chrome(options=chrome_options)
  dr.get(img_url)
  foto = dr.find_element_by_xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td[1]/table/tbody/tr[1]/td[1]/a/img').get_attribute('src') 
  
  return bixo, foto
cont = 0



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import configparser

#import urllib.request
#import ssl
#from dotenv import load_dotenv
#import os
#import json

from selenium.webdriver.common.by import By

from sys import exit
from urllib.parse import urlparse, parse_qs
#import numpy as np
from selenium.webdriver.chrome.service import Service


#driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome()
driver.maximize_window()
#options = webdriver.ChromeOptions()
#options.add_argument('--headless=new')
#driver = webdriver.Chrome(options=options)
#driver.get('https://practicesoftwaretesting.com/')
config = configparser.ConfigParser()
#Llamado de credenciales
config.read('credentials.conf')

valor_parametro1 = config.get('DEFAULT','usernamekey')
valor_parametro2 = config.get('DEFAULT','passwordkey')

# login
time.sleep(3)
target_url = 'https://www.facebook.com/login/'
driver.get(target_url) 
time.sleep(3)
username = driver.find_element("css selector", "input[name='email']")
password = driver.find_element("css selector", "input[name='pass']")
username.send_keys(valor_parametro1)
password.send_keys(valor_parametro2)
login = driver.find_element("css selector", "button[type='submit']").click()
resp = driver.page_source 
time.sleep(2)

driver.get('https://www.facebook.com/groups/2901591359932748')

def obtener_hijos():
    
    feed_div = driver.find_element("css selector", "div[role='feed']")
    
    return feed_div.find_elements(By.CSS_SELECTOR, "div")

def scroll_hasta_el_final(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
clase_objetivo = "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"
contador = 0
max_intentos = 3
intentos = 0
i=0
event=True
while event:
    try:
        scroll_hasta_el_final(driver)
        
        divs = obtener_hijos()
        # Procesar los nuevos divs
        for div in divs:
            scroll_hasta_el_final(driver)
            try:
                class_attr = div.get_attribute("class")

                
                contador += 1
                print(f"Div encontrado con la clase objetivo. Contador: {contador}")
                try:
                        div_global_info_post =driver.find_element(By.CSS_SELECTOR, "div.x1n2onr6.x1ja2u2z > div:not([class]) > div:not([class]) > div > div > div > div > div > div > div:not([class]) > div > div")
                        
                        div_cabecera_post = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1iyjqo2 > div")

                        #div_cabecera_post= div_global_info_post.find_element(By.XPATH, ".//div[@class='html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd']/div/div[@class='html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1iyjqo2']/div")
                        #div_post_person_name= div_cabecera_post.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']/span/h2")
                        div_post_person_name = div_cabecera_post.find_element(By.CSS_SELECTOR, "div.xu06os2.x1ok221b > span > h2")

                        #href_value = div_cabecera_post.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']/span/div/span/span/span/a").get_attribute("href")

                        print("username: ",  div_post_person_name.text)
                        #print("enlace: ",  href_value)

                except Exception as e:
                        print(f"Error al buscar en el árbol del div: {e}")
                i+=1
                print("termina en", 50-i)
                if i > 100: 
                    # Salir si el contador alcanza 50
                    event=False 
                    break
            
            except Exception as e:
                print(f"Error al procesar div: {e}")
       
    except Exception as e:
        print(f"Error durante el scroll o la obtención de divs: {e}")
        intentos += 1
        
print(f"Valor final de i después del bucle: {i}")
driver.quit()



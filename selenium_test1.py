from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from bs4 import BeautifulSoup
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
chrome_options.add_argument("--disable-notifications")
#chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome( options= chrome_options)
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


driver.get('https://www.facebook.com/groups/2901591359932748')

def obtener_hijos():
    try:
    
        feed_div = driver.find_element("css selector", "div[role='feed']")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "div[class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
            )                                 
        )
        return feed_div.find_elements(By.CSS_SELECTOR, "div[class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
    except Exception as e:                                         
        print(f"Error al obtener hijos: {e}")
        return []

def scroll_hasta_el_final(driver):
    # Obtener la altura total de la página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5) 


def extraer_datos():
    elementos_vistos = set()
    event =True  
    while event:  # Bucle infinito hasta que se detenga manualmente
          # Realiza scroll para cargar más contenido
        scroll_hasta_el_final(driver)
        divs = obtener_hijos()  # Obtiene los elementos actuales
        i =0
        for div in divs:
            texto = div.text
            i+=1
            print('cantidad total de divs: ',len(divs))
            if texto not in elementos_vistos:  # Verifica si el texto ya fue procesado
                elementos_vistos.add(texto) 
                #WebDriverWait(driver, 20).until(
                #EC.presence_of_element_located((By.XPATH, f"(//div[@class='xu06os2 x1ok221b']//span/h2/span)[{i}]"))
                #)
                try:
                    div_global_info_post =div.find_element(By.CSS_SELECTOR, "div.x1n2onr6.x1ja2u2z > div:not([class]) > div:not([class]) > div > div > div > div > div > div > div:not([class]) > div > div")
                    div_cabecera_post = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1iyjqo2 > div")
                    div_post_person_name = div_cabecera_post.find_element(By.CSS_SELECTOR, ".xu06os2.x1ok221b span > h2 > span")
                    div_post_id = div_global_info_post.find_element(By.CSS_SELECTOR, ".xu06os2.x1ok221b span > h2").get_attribute('id')
                    #div.html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 >div.html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6
                    #/div/a/div.x6s0dn4.x1jx94hy.x78zum5.xdt5ytf.x6ikm8r.x10wlt62.x1n2onr6.xh8yej3/div/div/div/img
                    #div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6
                    #html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6>a>div>div>div>div
                    #div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6 > a > div > div > div > div
                    try:
                        div_post_img = div_global_info_post.find_element(By.CSS_SELECTOR,"div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6 > a > div > div > div > div>img").get_attribute('src')
                        print('url: ', div_post_img)
                    except NoSuchElementException:
                        print('url: sin imagen')

                    try:
                        div_post_description = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x1l90r2v.x1pi30zi.x1swvt13.x1iorvi4")
                        print('Descripción del post: ', div_post_description.text)  # Imprimir la descripción si existe
                    except NoSuchElementException:
                        print('Descripción del post: No tiene ')
                        
                    print('estamons en el iterador', i)
                    print('div: ',div_post_person_name.text)
                    print('id_post', div_post_id)
                    yield  texto
                except Exception as e:
                     print(f"Error al procesar el elemento: {e}")
                
            if i== 100 | i==len(divs):
                print('al final i : ' ,i)
                event=False
                break;
        
        

for dato in extraer_datos():
    print('next :')

        


#nombres = []  # Lista para almacenar los datos
#data_generator = extraer_datos()


    

'''div_global_info_post =driver.find_element(By.CSS_SELECTOR, "div.x1n2onr6.x1ja2u2z > div:not([class]) > div:not([class]) > div > div > div > div > div > div > div:not([class]) > div > div")
                        
                        div_cabecera_post = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1iyjqo2 > div")
                        #div_cabecera_post= div_global_info_post.find_element(By.XPATH, ".//div[@class='html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd']/div/div[@class='html-div xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1iyjqo2']/div")
                        #div_post_person_name= div_cabecera_post.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']/span/h2")
                        div_post_person_name = div_cabecera_post.find_element(By.CSS_SELECTOR, "div.xu06os2.x1ok221b > span > h2 > span > span > a ")

                        #href_value = div_cabecera_post.find_element(By.XPATH, ".//div[@class='xu06os2 x1ok221b']/span/div/span/span/span/a").get_attribute("href")

                        print("username: ",  div_post_person_name.text)
                        #print("enlace: ",  href_value)

               )'''
#driver.quit()



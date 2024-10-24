from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,WebDriverException
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import configparser
import random
from selenium.webdriver.common.by import By
import psycopg2
import logging
from sys import exit
#from urllib.parse import urlparse, parse_qs
#import numpy as np
#from selenium.webdriver.chrome.service import Service
from pipeline_pages_fb_ import DatabaseConnection
class Scraper_Perfil_FB:
    def __init__(self):
        #driver = webdriver.Chrome()
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-notifications")
        #chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome( options= chrome_options)
        self.driver.maximize_window()
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless=new')
        #driver = webdriver.Chrome(options=options)
        #driver.get('https://practicesoftwaretesting.com/')
        self.config = configparser.ConfigParser()
        #Llamado de credenciales
        self.config.read('credentials.conf')
        self.credentials = self._get_credentials()
        #self.driver.execute_script("document.body.style.zoom='0.6';")
        #self.username = self.config.get('DEFAULT','usernamekey')
        #self.password = self.config.get('DEFAULT','passwordkey')
        self.perfil_links = [
            #'https://www.facebook.com/groups/chamba.dev',
            #'https://www.facebook.com/profile.php?id=61553491007165',
            #'https://www.facebook.com/santiagoolmedopolicia'
            #'https://www.facebook.com/profile.php?id=61552964263412'
            'https://www.facebook.com/santiagoolmedopolicia',
            'https://www.facebook.com/profile.php?id=100086973733765',
            'https://www.facebook.com/tenenciapolitica.goaltal.33',
            'https://www.facebook.com/surissayanna.bonescastro',
        ]
        self.selector_imagen = [
            "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6 > a > div > div > div > div>img",
            "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xat24cr.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1jx94hy.x8cjs6t.x1ch86jh.x80vd3b.xckqwgs.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xy80clv.xfh8nwu.xoqspk4.x12v9rci.x138vmkv.x6ikm8r.x10wlt62.x16n37ib.xq8finb > div > div > div.html-div.xdj266r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1mh8g0r.x11i5rnm.xod5an3 > div > a > div > div > div > div > img"
        ]

        self.selectors_modal = [
            "div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1",
            "div.__fb-dark-mode.xnkg4db.xwsalez.x13ywhbb.x178cd7z.x1n2onr6.xzkaem6 div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1"
        ]

        self.selectors_descripcion_perfil=[
            "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x1l90r2v.x1iorvi4.x1ye3gou.xn6708d",
            "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x1swvt13.x1pi30zi.x18d9i69 > span >div"
        ]
        self.conexion = DatabaseConnection()
        self.conexion.crear_conexion()
    def _get_credentials(self):
        credentials = []
        # Filtrar las claves que contienen pares coincidentes de username y password
        for key in self.config['DEFAULT']:
            if key.startswith('usernamekey'):
                num = key.replace('usernamekey', '')
                username = self.config.get('DEFAULT', f'usernamekey{num}')
                password = self.config.get('DEFAULT', f'passwordkey{num}')
                credentials.append((username, password))
        return credentials
    def login(self):
            attempt = 0
            max_attempts = len(self.credentials)
            # Limitar el número de intentos para evitar bucles infinitos
            while attempt < max_attempts and self.credentials:
                username, password = random.choice(self.credentials)
                print(f"Iniciando sesión con el usuario: {username} (Intento {attempt + 1})")
                try:
                    # Abrir la página de inicio de sesión de Facebook
                    time.sleep(3)
                    target_url = 'https://www.facebook.com/login/'
                    self.driver.get(target_url)
                    time.sleep(3)
                    self.driver.execute_script("document.body.style.zoom='50%'")

                    # Ingresar las credenciales
                    username_input = self.driver.find_element("css selector", "input[name='email']")
                    password_input = self.driver.find_element("css selector", "input[name='pass']")
                    username_input.send_keys(username)
                    password_input.send_keys(password)

                    # Hacer clic en el botón de inicio de sesión
                    login_button = self.driver.find_element("css selector", "button[type='submit']").click()
                    time.sleep(5)

                    # Verificar si la sesión fue exitosa
                    if "login_attempt" in self.driver.current_url or "checkpoint" in self.driver.current_url:
                        raise ValueError("Inicio de sesión fallido, el perfil puede estar bloqueado o las credenciales son incorrectas.")

                    print(f"Sesión iniciada con éxito con el usuario: {username}")
                    return self.driver.page_source  # Devuelve la fuente de la página si inicia sesión correctamente

                except (NoSuchElementException, WebDriverException, ValueError) as e:
                    print(f"Error al iniciar sesión con {username}: {str(e)}")
                    print("Intentando con otras credenciales...")
                    
                    # Eliminar las credenciales fallidas de la lista
                    self.credentials.remove((username, password))
                    attempt += 1

            print("Error: No se pudo iniciar sesión después de múltiples intentos.")
            return None
    def scroll_hasta_el_final(self, driver):
        # Obtener la altura total de la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(7) 
    def configurar_logger(self):
        # Configuración básica del logger
        logging.basicConfig(filename='errores_perfiles_fb.log',  # Archivo donde se guardarán los logs
                            level=logging.INFO,     # Nivel de registro, en este caso errores
                            format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
                            datefmt='%Y-%m-%d %H:%M:%S')  # Formato de la fecha y hora
    
    def perfil_generador(self,perfil_links):
        for perfil_link in perfil_links:
            yield perfil_link
    def obtener_comentario(self,elemento_base,publicacion_id,perfil_link):
          try:
            div_coment_content = elemento_base.find_element(By.CSS_SELECTOR,"div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6 div.x1r8uery.x1iyjqo2.x6ikm8r.x10wlt62.x1pi30zi div.xwib8y2.xn6708d.x1ye3gou.x1y1aw1k")
            div_open_comments = elemento_base.find_element(By.CSS_SELECTOR,"div.x1i10hfl.x1qjc9v5.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.xjbqb8w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1heor9g.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1ja2u2z")
            div_text_open_comments = div_open_comments.text.lower()
            if "1 comentario" in div_text_open_comments:
                try:
                    div_user_name_comment = div_coment_content.find_element(By.CSS_SELECTOR, " span > span.xt0psk2")
                    usuario_comentador=div_user_name_comment.text
                    print(f"Usuario solito: {div_user_name_comment.text}")
                    
                except Exception as e:
                    logging.error(f"Comentario solitario con id {publicacion_id} del grupo {perfil_link} sin usuario comentador ")
                try:
                    div_user_comment = div_coment_content.find_element(By.CSS_SELECTOR, " div.x1lliihq.xjkvuk6.x1iorvi4 > span")
                    comentario=div_user_comment.text
                    print(f"Usuario solito: {div_user_comment.text}")
                except Exception as e:
                    logging.error(f"Comentario solitario con id {publicacion_id} del grupo {perfil_link} sin descripcion ")

                try:
                    with self.conexion.connection.cursor() as cursor:
                        consulta = "INSERT INTO comentario (publicacion_id,usuario, descripcion_comentario) VALUES (%s,%s, %s) RETURNING Id"
                        cursor.execute(consulta, (publicacion_id,usuario_comentador, comentario))
                        self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                        comentario_id = cursor.fetchone()[0]
                        self.conexion.connection.commit()
                        print("Comentario insertado con éxitos")
                except psycopg2.Error as e:
                                logging.error(f"Error en la base de datos con unico comentario: {e}")
                except Exception as e:
                                logging.error(f"Algo está pasando con comentarios descripción unico: {e}")
                try:
                    div_user_image_comment = div_coment_content.find_element(By.CSS_SELECTOR,"div.x1ey2m1c.x9f619.xds687c.x17qophe.x10l6tqk.x13vifvy > a > img")
                    image_url=div_user_image_comment.get_attribute('src')
                    print(f"Imagen del comentario: {div_user_image_comment.get_attribute('src')}")
                    try:
                        with self.conexion.connection.cursor() as cursor:
                            consulta = "INSERT INTO imagen (publicacion_id,comentario_id,url) VALUES (%s,%s, %s)"
                            cursor.execute(consulta, (publicacion_id,comentario_id,image_url))
                            self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                            print("Imagen de comentario insertada con éxitos")
                    except psycopg2.Error as e:
                                        logging.error(f"Error en la base de datos con imagen en comentarios: {e}")
                    except Exception as e:
                                        logging.error(f"Algo está pasando con comentairos de image: {e}")
                except Exception as e:
                    logging.error(f"Comentario solitario con id {publicacion_id} del grupo {perfil_link} sin imagen ")
                
          except NoSuchElementException:
                logging.error(f"Publicacion con id {publicacion_id} del grupo {perfil_link} sin comentarios")     
    def obtener_hijos(self,driver):
        try:
            feed_div = driver.find_element("css selector", "div.x9f619.x1n2onr6.x1ja2u2z.xeuugli.xs83m0k.xjl7jj.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.x19h7ccj.xu9j1y6.x7ep2pv")
            WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, "div[class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
                )                                 
            )
            return feed_div.find_elements(By.CSS_SELECTOR, "div[class='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z']")
        except Exception as e:                                         
            print(f"Error al obtener hijos: {e}")
            return []
    def buscar_imagen(self,selector_imagen, elemento_base): 
        for selector in selector_imagen:
            try:
                test= elemento_base.find_element(By.CSS_SELECTOR, selector).get_attribute('src')
                return test
            except NoSuchElementException:
                continue
        return "sin imagen"
    def obtener_imagenes(self,div_global_info_post):
        try :
            try:
                post_imagenes = div_global_info_post.find_element(By.CSS_SELECTOR,
                    "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div > div > div.x1n2onr6 > div.x1n2onr6")
                # Si se encuentra post_imagenes, buscamos sus divs hijos
                child_divs = post_imagenes.find_elements(By.CSS_SELECTOR, "div.x6ikm8r.x10wlt62.x10l6tqk")
            except NoSuchElementException:
                # Si no se encuentra post_imagenes, buscamos en post_imagenes_inside
                post_imagenes_inside = div_global_info_post.find_element(By.CSS_SELECTOR,
                    "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd  > div.html-div.xdj266r.xat24cr.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1jx94hy.x8cjs6t.x1ch86jh.x80vd3b.xckqwgs.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xso031l.xy80clv.xfh8nwu.xoqspk4.x12v9rci.x138vmkv.x6ikm8r.x10wlt62.x16n37ib.xq8finb > div > div > div.html-div.xdj266r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1mh8g0r.x11i5rnm.xod5an3 > div > div > div.x1n2onr6 > div.x1n2onr6")          
                
                child_divs = post_imagenes_inside.find_elements(By.CSS_SELECTOR, "div.x6ikm8r.x10wlt62.x10l6tqk")
            
            for div_1 in child_divs:
                enlace1 = div_1.find_element(By.CSS_SELECTOR, "a > div > div > div > img").get_attribute('src')
                yield enlace1
        except NoSuchElementException:
                    yield 'aqui no hay imagenes'
    def procesar_comentarios(self, div_global_info_post,publicacion_id,perfil_link):
        try:
            # Localiza el botón para abrir los comentarios
            div_open_comments = div_global_info_post.find_element(By.CSS_SELECTOR,"div.x1i10hfl.x1qjc9v5.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.xjbqb8w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1heor9g.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1ja2u2z")
            div_text_open_comments = div_open_comments.text.lower()
            # Verificamos si el botón es para abrir comentarios
            if "comentarios" in div_text_open_comments:
                # Realiza la acción de abrir el modal de comentarios
                actions = ActionChains(self.driver)
                actions.move_to_element(div_open_comments).click().perform()
                time.sleep(2)
                # Procesamos el modal de comentarios
                try: 
                    wait = WebDriverWait(self.driver, 10)
                    #cerrarl_modal = driver.find_element(By.CSS_SELECTOR,"div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1")
                    cerrarl_modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1")))
                
                    modal_contenido = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1n2onr6.x1ja2u2z.x1afcbsf.xdt5ytf.x1a2a7pz.x71s49j.x1qjc9v5.xrjkcco.x58fqnu.x1mh14rs.xfkwgsy.x78zum5.x1plvlek.xryxfnj.xcatxm7.xrgej4m.xh8yej3')))
                    opem_all_coment = modal_contenido.find_element(By.CSS_SELECTOR,"div.x6ikm8r.x10wlt62 > div.xwya9rg.x11i5rnm.x1e56ztr.x1mh8g0r.xh8yej3 div > div >div > div.x6s0dn4.x78zum5.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xe0p6wg >div")
                    opem_all_coment.click()
                    
                    # Abrimos la sección de "ver todos los comentarios"
                    show_all_coments = self.driver.find_element(By.CSS_SELECTOR,"div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.xe8uvvx.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.x9f619.x1ypdohk.x78zum5.x1q0g3np.x2lah0s.x1i6fsjq.xfvfia3.xnqzcj9.x1gh759c.x10wwi4t.x1x7e7qh.x1344otq.x1de53dj.x1n2onr6.x16tdsg8.x1ja2u2z.x6s0dn4:nth-of-type(3)")
                    show_all_coments.click()
                    
                    div_with_comments = self.driver.find_element(By.CSS_SELECTOR,"div.html-div.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1gslohp")
                    # Bucle para scroll y cargar más comentarios
                    total_comentarios = 0
                    while True:
                        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_with_comments)
                        time.sleep(2)

                        # Obtenemos los comentarios
                        div_comment = div_with_comments.find_elements(By.CSS_SELECTOR, "div.x169t7cy.x19f6ikt")
                        for comment in div_comment:
                            try:
                                # Extraemos nombre de usuario y texto del comentario
                                div_user_name_comment = comment.find_element(By.CSS_SELECTOR, "div.xwib8y2.xn6708d.x1ye3gou.x1y1aw1k span.xt0psk2") # se le quito un span del original de paginas
                                div_user_description_comment = comment.find_element(By.CSS_SELECTOR, "div.xwib8y2.xn6708d.x1ye3gou.x1y1aw1k > div.x1lliihq.xjkvuk6.x1iorvi4 > span")
                                usuario_comentador=div_user_name_comment.text
                                comentario=div_user_description_comment.text
                                print(f"Usuario: {div_user_name_comment.text}")
                                print(f"Comentario: {div_user_description_comment.text}")
                                try:
                                        with self.conexion.connection.cursor() as cursor:
                                            consulta = "INSERT INTO comentario (publicacion_id,usuario, descripcion_comentario) VALUES (%s,%s, %s) RETURNING Id"
                                            cursor.execute(consulta, (publicacion_id,usuario_comentador, comentario))
                                            self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                                            comentario_id = cursor.fetchone()[0]
                                            self.conexion.connection.commit()
                                            print("Comentario insertado con éxitos")
                                except psycopg2.Error as e:
                                                logging.error(f"Error en la base de datos con comentarios: {e}")
                                except Exception as e:
                                                logging.error(f"Algo está pasando con comentairos: {e}")
                                # Extraemos la imagen del comentario
                                try:
                                    div_user_image_comment = comment.find_element(By.CSS_SELECTOR,"div.x1ey2m1c.x9f619.xds687c.x17qophe.x10l6tqk.x13vifvy > a > img")
                                    image_url=div_user_image_comment.get_attribute('src')
                                    print(f"Imagen del comentario: {div_user_image_comment.get_attribute('src')}")
                                    try:
                                        with self.conexion.connection.cursor() as cursor:
                                            consulta = "INSERT INTO imagen (publicacion_id,comentario_id,url) VALUES (%s,%s, %s)"
                                            cursor.execute(consulta, (publicacion_id,comentario_id,image_url))
                                            self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                                            print("Imagen de comentario insertada con éxitos")
                                    except psycopg2.Error as e:
                                                    logging.error(f"Error en la base de datos con imagen en comentarios: {e}")
                                    except Exception as e:
                                                    logging.error(f"No se encontro una imagen dentro de comentario:")
                                except:
                                    continue
                            except Exception as e:
                                print(f"Error al obtener el comentario: {e}")
                        
                        nuevos_comentarios = len(div_comment)
                        if nuevos_comentarios == total_comentarios:
                            break
                        total_comentarios = nuevos_comentarios

                    print(f"Total de comentarios procesados: {total_comentarios}")
                except Exception as e:
                    logging.error(f"Ausencia de elemento dentro del modal comentarios con id {publicacion_id} del grupo {perfil_link} ")
                    pass
            if cerrarl_modal:
                    cerrarl_modal.click()
                    print('Se cerró el modal de comentarios')
            else:
                print("El div es de compartido")
        
        except NoSuchElementException:
           logging.info("Sin comentarios y sin comparticiones , si este mensaje se repite mas de 20 veces seguidas en diferentes grupos, posiblemente cambia la estructura.")   
    def descripcion_perfil(self,selectors_descripcion_perfil, elemento_base): 
        wait = WebDriverWait(elemento_base, 7) 
        for selector in selectors_descripcion_perfil:
            try:
                descripcion_post = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text
                return descripcion_post
            except Exception as e:
                #print(f"Error en el {selector} : {e}")
                continue
        return "sin descripcion"
           
    def extraer_datos(self,driver,group_name,perfil_link):
        self.configurar_logger()
        elementos_vistos = set()
        event =True 
        contador_repeticiones = 0  # Contador para verificar repeticiones
        longitud_anterior = -1  # Inicializamos en -1 para que sea diferente de la primera longitud
    
        while event:  # Bucle infinito hasta que se detenga manualmente
            # Realiza scroll para cargar más contenido
            self.scroll_hasta_el_final(driver)
            divs = self.obtener_hijos(driver)  # Obtiene los elementos actuales
            i =0
            time.sleep(2)
            longitud_actual = len(divs)
            print('Cantidad total de divs: ', longitud_actual)
            if longitud_actual == longitud_anterior:
                contador_repeticiones += 1  # Incrementa el contador si es igual
            else:
                contador_repeticiones = 0  # Reinicia el contador si no es igual
            # Actualiza la longitud anterior con la longitud actual
            longitud_anterior = longitud_actual
            # Si la longitud se ha repetido 20 veces, cambia event a False
            if contador_repeticiones >= 12:
                print("La longitud de divs se ha repetido 20 veces. Terminando la extracción.")
                event = False  # Termina el bucle
        
            for div in divs:
                texto = div.text
                i+=1
                if texto not in elementos_vistos:  # Verifica si el texto ya fue procesado
                    elementos_vistos.add(texto) 
                    try:
                        div_global_info_post = WebDriverWait(div, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6.x1ja2u2z > div:not([class]) > div:not([class]) > div > div > div > div > div > div > div:not([class]) > div > div")))
                        div_cabecera_post = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1iyjqo2 > div")
                        try:
                            div_post_person_name = div_cabecera_post.find_element(By.CSS_SELECTOR, "div.xu06os2.x1ok221b >span  h2 > span")         
                            #div_post_img realiaar insert en tabla imagen                     
                        except:
                            div_post_person_name=div_cabecera_post.find_element(By.CSS_SELECTOR,"span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xo1l8bm.xi81zsa.x1yc453h >h2 >div")
                        try:
                            div_post_description = self.descripcion_perfil(self.selectors_descripcion_perfil, div_global_info_post)
                            print('Descripción del post: ', div_post_description)  # Imprimir la descripción si existe
                            #div_post_person_name.text realiaar insert en tabla publicacion columna descripcion
                        except NoSuchElementException:
                            div_post_description=""
                            logging.error('Esta publicacion del grupo no contiene una descripcion', e)
                        #print('identificador fecha:',div_post_date_id ,"::")    
                        logging.info(f'estamons en el iterador {i}  del grupo  {perfil_link}')
                        post_usuario=div_post_person_name.text
                        print('username: ',div_post_person_name.text)
                        try:
                            with self.conexion.connection.cursor() as cursor:
                                    consulta = "INSERT INTO publicacion (descripcion, usuario,group_name) VALUES (%s, %s,%s) RETURNING id"
                                    cursor.execute(consulta, (div_post_description, post_usuario,group_name))
                                    self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                                    publicacion_id = cursor.fetchone()[0]
                                    self.conexion.connection.commit()  # Asegúrate de confirmar la transacción
                                    print(f"Publicación insertada con éxito. ID de la publicación: {publicacion_id}")         
                        except psycopg2.Error as e:
                                    logging.error(f"Error en la base de datos con la publicación  con id : {publicacion_id} en el grupo :  { perfil_link}  : {e}")
                        except Exception as e:
                                    logging.error(f"algo esta mal con la insercion de la publicacion con id : {publicacion_id} en el grupo :  { perfil_link}  : {e}")
                        enlaceimagenes = self.obtener_imagenes(div_global_info_post)                   
                        for enlace in enlaceimagenes:
                            print('url:', enlace)
                            try:
                                with self.conexion.connection.cursor() as cursor:
                                        consulta = "INSERT INTO imagen (url,publicacion_id) VALUES (%s, %s)"
                                        cursor.execute(consulta, (enlace,publicacion_id ))
                                        self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                                        print(f"Imagen insertada con éxito")
                        
                            except psycopg2.Error as e:
                                        logging.error(f"Error en la base de datos Imagenes con la publicación  con id : {publicacion_id} en el grupo :    : {e}")
                            except Exception as e:
                                        logging.error(f"Algo está pasando con esto Imagenes: {e}")
                        
                        #div_post_person_name.text realiaar insert en tabla publicacion columna usuario
                        div_post_img = self.buscar_imagen(self.selector_imagen, div_global_info_post)
                        print('url: ', div_post_img)
                        try:
                            with self.conexion.connection.cursor() as cursor:
                                    consulta = "INSERT INTO imagen (url,publicacion_id) VALUES (%s, %s)"
                                    cursor.execute(consulta, (div_post_img,publicacion_id ))
                                    self.conexion.connection.commit() # Asegúrate de confirmar la transacción
                                    print(f"Imagen insertada con éxito")
                        
                        except psycopg2.Error as e:
                                    logging.error(f"Error en la base de datos Imagen: {e}")
                        except Exception as e:
                                    logging.error(f"Algo está pasando con esto Imagen: {e}")
                        self.obtener_comentario(div_global_info_post,publicacion_id,perfil_link)
                        self.procesar_comentarios(div_global_info_post,publicacion_id,perfil_link)                         
                        yield  texto
                    except Exception as e:
                        logging.error(f"Error al procesar el elemento: {e}")
    def procesar_perfiles(self):
        try:
            self.login()
            generador_perfil = self.perfil_generador(self.perfil_links)
            total_paginas = len(self.perfil_links)  # Total de paginas a procesar
            print("hay perfil:  " ,total_paginas)
            paginas_procesados = 0
            for perfil_link in generador_perfil:
                self.driver.get(perfil_link)  # Cargar el siguiente grupo
                print(f"Extrayendo información de {perfil_link}...")
                action = ActionChains(self.driver)
                action.key_down(Keys.CONTROL)
                # Simular Ctrl + Scroll hacia atrás (Zoom Out)
                pyautogui.keyDown('ctrl')  # Mantén presionada la tecla Ctrl
                for _ in range(3):  # Ajusta la cantidad de zoom out según sea necesario
                    pyautogui.scroll(-150)  # Desplazar hacia atrás para hacer zoom out
                    time.sleep(1)  # Pausa breve para que el navegador procese el zoom
                pyautogui.keyUp('ctrl') 
                div_perfil_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1.html-h1.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1vvkbs.x1heor9g.x1qlqyl8.x1pd3egz.x1a2a7pz"))
                )
                group_name=div_perfil_name.text
                for dato in self.extraer_datos(self.driver,group_name,perfil_link):
                    print('next :')
                paginas_procesados += 1  # Incrementar el contador de paginas procesados
                print(f"Perfiles procesados: {paginas_procesados}/{total_paginas}")    
        except Exception as e:
            print(f"Error al procesar perfiles: {e}")

        finally:
            # Asegurarse de que el navegador se cierra al terminar el procesamiento de todos los grupos
            if self.driver:
                self.driver.quit()   
    def cerrar_conexion(self):
        self.driver.quit()    
        self.conexion.cerrar_conexion()
def main():    
      scraper_group = Scraper_Perfil_FB()        
      scraper_group.procesar_perfiles()  # Llamar al método de scraping
      scraper_group.cerrar_conexion()  # Cerrar el navegador    
        
if __name__ == "__main__":
    main() 
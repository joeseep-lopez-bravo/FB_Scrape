from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import time
import configparser

from selenium.webdriver.common.by import By
import psycopg2
from sys import exit
#from urllib.parse import urlparse, parse_qs
#import numpy as np
#from selenium.webdriver.chrome.service import Service
from pipeline_pages_fb_ import DatabaseConnection

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

driver.get('https://www.facebook.com/groups/chamba.dev')
selector_imagen = [
    "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6 > a > div > div > div > div>img",
    "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xat24cr.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1jx94hy.x8cjs6t.x1ch86jh.x80vd3b.xckqwgs.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x178xt8z.xm81vs4.xy80clv.xfh8nwu.xoqspk4.x12v9rci.x138vmkv.x6ikm8r.x10wlt62.x16n37ib.xq8finb > div > div > div.html-div.xdj266r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1mh8g0r.x11i5rnm.xod5an3 > div > a > div > div > div > div > img"
]
selectors_modal = [
    "div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1",
    "div.__fb-dark-mode.xnkg4db.xwsalez.x13ywhbb.x178cd7z.x1n2onr6.xzkaem6 div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1"
]


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
    time.sleep(7) 
def buscar_imagen(selector_imagen, elemento_base): 
    for selector in selector_imagen:
        try:
            test= elemento_base.find_element(By.CSS_SELECTOR, selector).get_attribute('src')
            return test
        except NoSuchElementException:
            continue
    return "sin imagen"
def obtener_imagenes(div_global_info_post):
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
def procesar_comentarios(driver, div_global_info_post,publicacion_id):
    try:
        # Localiza el botón para abrir los comentarios
        div_open_comments = div_global_info_post.find_element(By.CSS_SELECTOR,"div.x1i10hfl.x1qjc9v5.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.xjbqb8w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1heor9g.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1ja2u2z")
        div_text_open_comments = div_open_comments.text.lower()
        # Verificamos si el botón es para abrir comentarios
        if "comentarios" in div_text_open_comments:
            # Realiza la acción de abrir el modal de comentarios
            actions = ActionChains(driver)
            actions.move_to_element(div_open_comments).click().perform()
            time.sleep(2)
            # Procesamos el modal de comentarios
            try: 
                wait = WebDriverWait(driver, 10)
                #elemento_encontrado = driver.find_element(By.CSS_SELECTOR,"div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1")
                elemento_encontrado = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1")))
            
                modal_contenido = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.__fb-light-mode.x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k.xshlqvt div.x1n2onr6.x1ja2u2z.x1afcbsf.xdt5ytf.x1a2a7pz.x71s49j.x1qjc9v5.xrjkcco.x58fqnu.x1mh14rs.xfkwgsy.x78zum5.x1plvlek.xryxfnj.xcatxm7.xrgej4m.xh8yej3')))
                opem_all_coment = modal_contenido.find_element(By.CSS_SELECTOR,"div.x6ikm8r.x10wlt62 > div.xwya9rg.x11i5rnm.x1e56ztr.x1mh8g0r.xh8yej3 div > div >div > div.x6s0dn4.x78zum5.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xe0p6wg >div")
                opem_all_coment.click()
                
                # Abrimos la sección de "ver todos los comentarios"
                show_all_coments = driver.find_element(By.CSS_SELECTOR,"div.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.xe8uvvx.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.xjyslct.x9f619.x1ypdohk.x78zum5.x1q0g3np.x2lah0s.x1i6fsjq.xfvfia3.xnqzcj9.x1gh759c.x10wwi4t.x1x7e7qh.x1344otq.x1de53dj.x1n2onr6.x16tdsg8.x1ja2u2z.x6s0dn4:nth-of-type(3)")
                show_all_coments.click()
                
                div_with_comments = driver.find_element(By.CSS_SELECTOR,"div.html-div.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1gslohp")
                # Bucle para scroll y cargar más comentarios
                total_comentarios = 0
                while True:
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_with_comments)
                    time.sleep(2)

                    # Obtenemos los comentarios
                    div_comment = div_with_comments.find_elements(By.CSS_SELECTOR, "div.x169t7cy.x19f6ikt")
                    for comment in div_comment:
                        try:
                            # Extraemos nombre de usuario y texto del comentario
                            div_user_name_comment = comment.find_element(By.CSS_SELECTOR, "div.xwib8y2.xn6708d.x1ye3gou.x1y1aw1k > span > span.xt0psk2")
                            div_user_description_comment = comment.find_element(By.CSS_SELECTOR, "div.xwib8y2.xn6708d.x1ye3gou.x1y1aw1k > div.x1lliihq.xjkvuk6.x1iorvi4 > span")
                            usuario_comentador=div_user_name_comment.text
                            comentario=div_user_description_comment.text
                            print(f"Usuario: {div_user_name_comment.text}")
                            print(f"Comentario: {div_user_description_comment.text}")
                            try:
                                    with conexion.connection.cursor() as cursor:
                                        consulta = "INSERT INTO comentario (publicacion_id,usuario, descripcion_comentario) VALUES (%s,%s, %s) RETURNING Id"
                                        cursor.execute(consulta, (publicacion_id,usuario_comentador, comentario))
                                        conexion.connection.commit() # Asegúrate de confirmar la transacción
                                        comentario_id = cursor.fetchone()[0]
                                        conexion.connection.commit()
                                        print("Comentario insertado con éxitos")
                            except psycopg2.Error as e:
                                            print(f"Error en la base de datos con comentarios: {e}")
                            except Exception as e:
                                            print(f"Algo está pasando con comentairos: {e}")

                            # Extraemos la imagen del comentario
                            try:
                                div_user_image_comment = comment.find_element(By.CSS_SELECTOR,"div.x1ey2m1c.x9f619.xds687c.x17qophe.x10l6tqk.x13vifvy > a > img")
                                image_url=div_user_image_comment.get_attribute('src')
                                print(f"Imagen del comentario: {div_user_image_comment.get_attribute('src')}")
                                try:
                                    with conexion.connection.cursor() as cursor:
                                        consulta = "INSERT INTO imagen (publicacion_id,comentario_id,url) VALUES (%s,%s, %s)"
                                        cursor.execute(consulta, (publicacion_id,comentario_id,image_url))
                                        conexion.connection.commit() # Asegúrate de confirmar la transacción
                                        print("Imagen de comentario insertada con éxitos")
                                except psycopg2.Error as e:
                                                print(f"Error en la base de datos con imagen en comentarios: {e}")
                                except Exception as e:
                                                print(f"Algo está pasando con comentairos de imagen: {e}")
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
                print(f"Error procesando el modal de comentarios:")
                pass
        if elemento_encontrado:
                elemento_encontrado.click()
                print('Se cerró el modal de comentarios')
        else:
            print("El div es de compartido")
    
    except NoSuchElementException:
        print("Sin comentarios y sin comparticiones")

conexion = DatabaseConnection()
conexion.crear_conexion()
def extraer_datos():
    elementos_vistos = set()
    event =True  
    while event:  # Bucle infinito hasta que se detenga manualmente
          # Realiza scroll para cargar más contenido
        scroll_hasta_el_final(driver)
        divs = obtener_hijos()  # Obtiene los elementos actuales
        i =0
        time.sleep(2)
        for div in divs:
            texto = div.text
            i+=1
            print('cantidad total de divs: ',len(divs))
            if texto not in elementos_vistos:  # Verifica si el texto ya fue procesado
                elementos_vistos.add(texto) 
                try:
                    div_global_info_post = WebDriverWait(div, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6.x1ja2u2z > div:not([class]) > div:not([class]) > div > div > div > div > div > div > div:not([class]) > div > div")))
                    div_cabecera_post = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1iyjqo2 > div")
                    div_post_person_name = div_cabecera_post.find_element(By.CSS_SELECTOR, ".xu06os2.x1ok221b span > h2 > span")         
                    #div_post_img realiaar insert en tabla imagen
                    
                                                  
                    try:
                        div_post_description = div_global_info_post.find_element(By.CSS_SELECTOR, "div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.html-div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x1l90r2v.x1pi30zi.x1swvt13.x1iorvi4")
                        descripcion_post= div_post_description.text
                        print('Descripción del post: ', div_post_description.text)  # Imprimir la descripción si existe
                        #div_post_person_name.text realiaar insert en tabla publicacion columna descripcion
                    except NoSuchElementException:
                        descripcion_post=""
                        print('Descripción del post: No tiene ')
                    #print('identificador fecha:',div_post_date_id ,"::")    
                    print('estamons en el iterador', i)
                    post_usuario=div_post_person_name.text
                    print('username: ',div_post_person_name.text)
                    try:
                        with conexion.connection.cursor() as cursor:
                                consulta = "INSERT INTO publicacion (descripcion, usuario) VALUES (%s, %s) RETURNING id"
                                cursor.execute(consulta, (descripcion_post, post_usuario))
                                conexion.connection.commit() # Asegúrate de confirmar la transacción
                                publicacion_id = cursor.fetchone()[0]
                                conexion.connection.commit()  # Asegúrate de confirmar la transacción
                                print(f"Publicación insertada con éxito. ID de la publicación: {publicacion_id}")         
                    except psycopg2.Error as e:
                                print(f"Error en la base de datos publicacion: {e}")
                    except Exception as e:
                                print(f"Algo está pasando con esto publicacion: {e}")
                    enlaceimagenes = obtener_imagenes(div_global_info_post)                   
                    for enlace in enlaceimagenes:
                        print('url:', enlace)
                        try:
                            with conexion.connection.cursor() as cursor:
                                    consulta = "INSERT INTO imagen (url,publicacion_id) VALUES (%s, %s)"
                                    cursor.execute(consulta, (enlace,publicacion_id ))
                                    conexion.connection.commit() # Asegúrate de confirmar la transacción
                                    print(f"Imagen insertada con éxito")
                    
                        except psycopg2.Error as e:
                                    print(f"Error en la base de datos Imagenes: {e}")
                        except Exception as e:
                                    print(f"Algo está pasando con esto Imagenes: {e}")
                    
                    #div_post_person_name.text realiaar insert en tabla publicacion columna usuario
                    div_post_img = buscar_imagen(selector_imagen, div_global_info_post)
                    print('url: ', div_post_img)
                    try:
                        with conexion.connection.cursor() as cursor:
                                consulta = "INSERT INTO imagen (url,publicacion_id) VALUES (%s, %s)"
                                cursor.execute(consulta, (div_post_img,publicacion_id ))
                                conexion.connection.commit() # Asegúrate de confirmar la transacción
                                print(f"Imagen insertada con éxito")
                    
                    except psycopg2.Error as e:
                                print(f"Error en la base de datos Imagen: {e}")
                    except Exception as e:
                                print(f"Algo está pasando con esto Imagen: {e}")
                    procesar_comentarios(driver, div_global_info_post,publicacion_id)                         
                    yield  texto
                except Exception as e:
                     print(f"Error al procesar el elemento: {e}")
                
            if i== 100 | i==len(divs):
                print('al final i : ' ,i)
                event=False
                break;
        
for dato in extraer_datos():
   print('next :')
conexion.cerrar_conexion()

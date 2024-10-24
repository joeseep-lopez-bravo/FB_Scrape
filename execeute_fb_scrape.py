import subprocess

# Variables para almacenar los subprocesos en ejecución
processes = []

# Funciones para ejecutar cada script
def ejecutar_script1():
    print("Ejecutando script páginas...")
    process = subprocess.Popen(["python", "pagina_fb.py"])
    processes.append(process)

def ejecutar_script2():
    print("Ejecutando script grupos...")
    process = subprocess.Popen(["python", "groups_fb.py"])
    processes.append(process)

def ejecutar_script3():
    print("Ejecutando script perfiles...")
    process = subprocess.Popen(["python", "perfil_fb.py"])
    processes
def ejecutar_script3():
    print("Ejecutando script perfiles...")
    process = subprocess.Popen(["python", "perfil_fb.py"])
    processes.append(process)

def ejecutar_script4():
    print("Ejecutando script obtener imágenes...")
    process = subprocess.Popen(["python", "image_process.py"])
    processes.append(process)

# Función para ejecutar todos los scripts de una vez
def ejecutar_todos_los_scripts():
    ejecutar_script1()
    ejecutar_script2()
    ejecutar_script3()
    

# Función para cancelar todos los scripts en ejecución
def cancelar_todos_los_scripts():
    for process in processes:
        if process.poll() is None:  # Verifica si el proceso sigue en ejecución
            print("Cancelando script...")
            process.terminate()
    processes.clear()  # Limpia la lista de procesos

# Ejecutar todos los scripts de una vez
if __name__ == "__main__":
    try:
        ejecutar_todos_los_scripts()
        ejecutar_script4()
        print("Todos los scripts se están ejecutando.")
    except KeyboardInterrupt:
        print("Cancelando todos los scripts...")
        cancelar_todos_los_scripts()

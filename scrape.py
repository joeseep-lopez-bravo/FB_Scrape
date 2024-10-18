import tkinter as tk
import subprocess

# Variables para almacenar los subprocesos en ejecución
script_process = None

# Funciones que se llaman cuando presionas los botones
def ejecutar_script1():
    global script_process
    cancelar_script()  # Cancela cualquier script anterior
    print("Ejecutando script páginas...")
    # Ejecuta el script real como subproceso
    script_process = subprocess.Popen(["python", "pagina_fb.py"])

def ejecutar_script2():
    global script_process
    cancelar_script()  # Cancela cualquier script anterior
    print("Ejecutando script grupos...")
    # Ejecuta el script real groups_fb.main() como subproceso
    
    script_process = subprocess.Popen(["python", "groups_fb.py"]) 
def ejecutar_script3():
    global script_process
    cancelar_script()  # Cancela cualquier script anterior
    print("Ejecutando script perfiles...")
    # Ejecuta el script real como subproceso
    script_process = subprocess.Popen(["python", "perfil_fb.py"])

def ejecutar_script4():
    global script_process
    cancelar_script()  # Cancela cualquier script anterior
    print("Ejecutando script obtener imágenes...")
    # Ejecuta el script real como subproceso
    script_process = subprocess.Popen(["python", "image_process.py"])

# Función para cancelar la ejecución del script
def cancelar_script():
    global script_process
    if script_process and script_process.poll() is None:  # Si hay un proceso en ejecución
        print("Cancelando script en ejecución...")
        script_process.terminate()  # Terminar el proceso
        script_process = None  # Limpiar la variable del proceso
    else:
        print("No hay script en ejecución.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejecutor de Scripts")
root.geometry("400x300")  # Tamaño de la ventana

# Crear y colocar los botones
btn1 = tk.Button(root, text="Ejecutar Script 1", command=ejecutar_script1)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Ejecutar Script 2", command=ejecutar_script2)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Ejecutar Script 3", command=ejecutar_script3)
btn3.pack(pady=10)

btn4 = tk.Button(root, text="Ejecutar Script 4", command=ejecutar_script4)
btn4.pack(pady=10)

# Botón para cancelar el script en ejecución
btn_cancel = tk.Button(root, text="Cancelar Script", command=cancelar_script)
btn_cancel.pack(pady=10)

# Botón para cerrar la aplicación
btn_exit = tk.Button(root, text="Salir", command=root.quit)
btn_exit.pack(pady=20)

# Ejecutar la ventana principal
root.mainloop()

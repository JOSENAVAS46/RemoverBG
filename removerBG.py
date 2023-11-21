import os
import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

def remove_background(input_path, output_folder, api_key, is_url=False):
    if is_url:
        data = {'image_url': input_path, 'size': 'auto'}
    else:
        files = {'image_file': open(input_path, 'rb')}
        data = {'size': 'auto'}

    headers = {'X-Api-Key': api_key}

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files=files if not is_url else None,
        data=data,
        headers=headers,
    )

    if response.status_code == requests.codes.ok:
        # Obtener la lista de archivos en el directorio de salida
        existing_files = [f for f in os.listdir(output_folder) if f.startswith("rmbg-") and f.endswith(".png")]

        # Obtener el nombre del archivo base
        base_filename = "rmbg.png"

        # Verificar si el nombre base ya existe
        counter = 1
        while f"rmbg-{counter}.png" in existing_files:
            counter += 1

        output_filename = f"rmbg-{counter}.png"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, 'wb') as out:
            out.write(response.content)

        return output_path
    else:
        print("Error:", response.status_code, response.text)
        return None

def postview_image(output_path, window_title):
    image = Image.open(output_path)
    image.thumbnail((400, 400))
    photo = ImageTk.PhotoImage(image)

    postview_window = tk.Toplevel()
    postview_window.title(window_title)

    label = tk.Label(postview_window, image=photo)
    label.image = photo
    label.pack(padx=10, pady=10)

    # Botón para guardar
    save_button = tk.Button(postview_window, text="Guardar", command=postview_window.destroy)
    save_button.pack(pady=10)

    postview_window.mainloop()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)
    entry_url.delete(0, tk.END)

def process_image():
    api_key = entry_api_key.get()

    if not api_key:
        messagebox.showerror("Error", "Por favor, ingrese una clave de API.")
        return

    input_path = entry_path.get()
    url = entry_url.get()

    if not input_path and not url:
        messagebox.showerror("Error", "Por favor, elija un archivo de imagen o ingrese una URL.")
        return

    if input_path and url:
        messagebox.showerror("Error", "Por favor, elija solo un modo: archivo o URL.")
        return

    if input_path:
        success = remove_background(input_path, "output_images", api_key)
        if success:
            postview_image(success, "Vista Previa - Después de Quitar el Fondo")
            messagebox.showinfo("Proceso completado", f"La imagen se guardó en output_images")
    elif url:
        success = remove_background(url, "output_images", api_key, is_url=True)
        if success:
            postview_image(success, "Vista Previa - Después de Quitar el Fondo")

# Crear la ventana principal
window = tk.Tk()
window.title("Remove Background GUI")

# Crear widgets
label_api_key = tk.Label(window, text="Clave de API:")
entry_api_key = tk.Entry(window, width=50)
label_path = tk.Label(window, text="Ruta de la imagen:")
entry_path = tk.Entry(window, width=50)
button_browse = tk.Button(window, text="Examinar", command=browse_file)
label_url = tk.Label(window, text="URL de la imagen:")
entry_url = tk.Entry(window, width=50)
button_process = tk.Button(window, text="Procesar", command=process_image)

# Posicionar widgets
label_path.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_path.grid(row=0, column=1, padx=10, pady=10)
button_browse.grid(row=0, column=2, padx=10, pady=10)
label_url.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_url.grid(row=1, column=1, padx=10, pady=10)
label_api_key.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_api_key.grid(row=2, column=1, padx=10, pady=10)
button_process.grid(row=3, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
window.mainloop()

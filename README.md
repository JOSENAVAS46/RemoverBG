# Remove Background GUI

Esta aplicación te permite eliminar el fondo de las imágenes utilizando la API de [Remove.bg](https://www.remove.bg/).

## Requisitos previos

Asegúrate de tener Python y pip instalados en tu computadora.

1. **Registro en Remove.bg:**
   - Ingresa a [Remove.bg](https://www.remove.bg/)
   - Crea una cuenta

2. **Obtén una API Key:**
   - Visita [Remove.bg API](https://www.remove.bg/api)
   - Haz clic en "Get API Key"
   - Haz clic en "New API Key"
   - Asigna un nombre a la API Key
   - Copia la API Key generada

3. **Instalación de dependencias:**
   - Ejecuta el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```

4. **Ejecutar la aplicación:**
   - Ejecuta la aplicación directamente usando Python:

     ```bash
     python removerBG.py
     ```

## Instrucciones de Uso

1. Ingresa la clave de API obtenida en el campo correspondiente.
2. Selecciona una imagen haciendo clic en "Examinar" o ingresa una URL en el campo respectivo.
3. Haz clic en "Procesar" para quitar el fondo de la imagen.
4. La imagen resultante se guardará en la carpeta `output_images`.

## Aviso Importante

Esta aplicación funciona con la API de Remove.bg. Asegúrate de obtener tu propia API Key siguiendo las instrucciones mencionadas anteriormente.

---
# Remove Background GUI

Esta aplicación te permite eliminar el fondo de las imágenes utilizando la API de [Remove.bg](https://www.remove.bg/).

## Requisitos previos

Asegúrate de tener Python y pip instalados en tu computadora.

### Instalación de Python

#### Para usuarios de Windows:

1. **Descarga Python:**
   - Visita [python.org](https://www.python.org/downloads/).
   - Haz clic en "Downloads" y selecciona la versión más reciente de Python.
   - Desplázate hacia abajo y elige el instalador adecuado para tu sistema operativo (por ejemplo, Windows).

2. **Inicia el instalador:**
   - Ejecuta el archivo descargado.
   - Asegúrate de marcar la casilla que dice "Add Python X.X to PATH" antes de hacer clic en "Install Now".

3. **Completa la instalación:**
   - Sigue las instrucciones del instalador y espera a que termine.

4. **Verifica la instalación:**
   - Abre la línea de comandos (Command Prompt) o PowerShell.
   - Ingresa el siguiente comando y presiona Enter:
     ```bash
     python --version
     ```
   - Deberías ver la versión de Python que acabas de instalar.

#### Para usuarios de macOS:

1. **Instalación con Homebrew (opcional pero recomendado):**
   - Abre la Terminal.
   - Ejecuta el siguiente comando para instalar Homebrew (si aún no lo tienes):
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **Instalación de Python:**
   - Ejecuta el siguiente comando para instalar Python con Homebrew:
     ```bash
     brew install python
     ```

3. **Verifica la instalación:**
   - En la Terminal, ingresa el siguiente comando y presiona Enter:
     ```bash
     python3 --version
     ```
   - Deberías ver la versión de Python que acabas de instalar.

#### Para usuarios de Linux (Ubuntu/Debian):

1. **Actualiza los paquetes:**
   - Abre la Terminal.
   - Ejecuta los siguientes comandos:
     ```bash
     sudo apt update
     sudo apt upgrade
     ```

2. **Instalación de Python:**
   - Ejecuta el siguiente comando para instalar Python:
     ```bash
     sudo apt install python3
     ```

3. **Verifica la instalación:**
   - En la Terminal, ingresa el siguiente comando y presiona Enter:
     ```bash
     python3 --version
     ```
   - Deberías ver la versión de Python que acabas de instalar.

### Instalación de pip

#### Para usuarios de Windows, macOS y Linux:

1. **Descarga `get-pip.py`:**
   - Visita [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py).
   - Haz clic derecho en la página y selecciona "Guardar como" para descargar el archivo `get-pip.py`.

2. **Instala pip:**
   - Abre la línea de comandos (Command Prompt o Terminal).
   - Navega al directorio donde guardaste `get-pip.py`.
   - Ejecuta el siguiente comando:
     ```bash
     python get-pip.py
     ```
     o
     ```bash
     python3 get-pip.py
     ```

3. **Verifica la instalación:**
   - En la Terminal o línea de comandos, ingresa los siguientes comandos y presiona Enter:
     ```bash
     pip --version
     ```
     o
     ```bash
     pip3 --version
     ```
   - Deberías ver la versión de pip que acabas de instalar.

### Obtén una API Key de Remove.bg

4. **Registro en Remove.bg:**
   - Ingresa a [Remove.bg](https://www.remove.bg/)
   - Crea una cuenta

5. **Obtén una API Key:**
   - Visita [Remove.bg API](https://www.remove.bg/api)
   - Haz clic en "Get API Key"
   - Haz clic en "New API Key"
   - Asigna un nombre a la API Key
   - Copia la API Key generada y guardala bien

### Instalación de dependencias

6. **Ejecuta el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:**

```bash
pip install -r requirements.txt
```

7. **Ejecutar la aplicación:**
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

## Cómo descargar el proyecto

Puedes descargar este proyecto directamente desde GitHub. Haz clic en el botón "Code" en la parte superior de la página y selecciona "Download ZIP". Descomprime el archivo ZIP en tu computadora y sigue las instrucciones anteriores para ejecutar la aplicación.

---

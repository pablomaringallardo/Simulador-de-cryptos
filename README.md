# Simulador-de-cryptos
Proyecto final BC14: Pablo Marín Gallardo

## Pasos para poder usar el programa.

1. Crear un entorno virtual

   ```shell
   # Windows
   python -m venv env

   # Mac / Linux
   python3 -m venv env
   ```

2. Activar el entorno virtual

   ```shell
    # Windows
    env\Scripts\activate

    # Mac / Linux
    source ./env/bin/activate

3. Instalar las dependencias

   ```shell
   pip install -r requirements.txt
   ```

4. Hacer una copia del archivo `.env_template` como `.env`

   ```shell
   # Windows
   copy .env-template .env

   # Mac / Linux
   cp .env-template .env
   ```

5. Editar el archivo `.env` y cambiar los valores de
   entorno necesarios. Por motivos de seguridad, dejar
   la variable `DEBUG` con el valor `False`.

6. Haz una copia del archivo config.sample.py como
   config.py e introduce tu SECRET KEY.

7. Con el entorno virtual activo, lanzar la aplicación

   ```shell
   flask run
   ```
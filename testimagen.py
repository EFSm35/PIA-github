# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:46:03 2023

@author: edo-s

Modulo encargado de interpretar los metadatos y guarda los resultados en un txt
"""

import argparse
import logging
from PIL import Image
from PIL.ExifTags import TAGS

# Configurar el logger
logging.basicConfig(filename='error.log', level=logging.ERROR)

def interpret_metadata(image_path):
    """
    Interpreta los metadatos de una imagen y los guarda en un archivo de texto.

    :param image_path: Ruta de la imagen.
    """
    try:
        # Abrir la imagen utilizando Pillow
        image = Image.open(image_path)

        # Extraer los metadatos
        metadata = image._getexif()

        # Verificar si existen metadatos
        if metadata is None:
            logging.error("La imagen %s no contiene metadatos.", image_path)
            return

        # Interpretar los metadatos
        interpreted_metadata = []
        for tag, value in metadata.items():
            # Interpretar el tag utilizando la tabla TAGS de PIL
            tag_name = TAGS.get(tag, tag)
            interpreted_metadata.append(f"{tag_name}: {value}")

        # Guardar los metadatos en un archivo de texto
        with open("metadatos.txt", "w") as file:
            file.write("\n".join(interpreted_metadata))

        #print("Los metadatos han sido guardados en el archivo 'metadatos.txt'.")

    except FileNotFoundError:
        logging.error("La ruta de la imagen %s no es válida.", image_path)
    except Exception as e:
        logging.error("Ocurrió un error al procesar la imagen %s: %s", image_path, str(e))


if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description="Interpretar metadatos de una imagen.")
    parser.add_argument("image_path", type=str, help="Ruta de la imagen")

    # Obtener la ruta de la imagen desde los argumentos
    args = parser.parse_args()
    image_path = args.image_path

    # Interpretar los metadatos de la imagen y guardarlos en un archivo de texto
    interpret_metadata(image_path)
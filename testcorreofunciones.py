# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:46:03 2023

@author: edo-s

Encargado de Mandar un correo electronico con los informes generados
"""
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse

# Configurar el registro de errores
logging.basicConfig(filename='error.log', level=logging.ERROR)

def obtener_datos_remitente():
    """Obtiene los datos del remitente desde archivos de texto."""
    correo = ""
    contraseña = ""
    try:
        with open('correopassword.txt', 'r') as archivo:
            contraseña = archivo.read()
    except FileNotFoundError as e:
        # Registrar el error utilizando logging
        logging.error(str(e))
        print(f"No se encontró el archivo correopassword.txt.")
    
    try:
        with open('correo.txt', 'r') as archivo:
            correo = archivo.read()
    except FileNotFoundError as e:
        # Registrar el error utilizando logging
        logging.error(str(e))
        print(f"No se encontró el archivo correo.txt.")
    
    return correo, contraseña

def enviar_correo(correo, contraseña, destinatario, nombre_archivo):
    """Envía un archivo de texto por correo electrónico."""
    # Leer el contenido del archivo de texto
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError as e:
        # Registrar el error utilizando logging
        logging.error(str(e))
        print(f"El archivo {nombre_archivo} no existe.")
        return
    
    # Configurar el mensaje de correo electrónico
    mensaje = MIMEMultipart()
    mensaje["From"] = correo
    mensaje["To"] = destinatario
    
    if nombre_archivo == "domain_info.txt":
        mensaje["Subject"] = "Informe Análisis del dominio"
    elif nombre_archivo == "metadatos.txt":
        mensaje["Subject"] = "Informe Análisis de metadatos"
    
    elif nombre_archivo == "testscrapy.txt":
        mensaje["Subject"] = "Informe Análisis Scrapy"
    
    else:
        mensaje["Subject"] = "Informe Análisis de nmap"
    
    # Cuerpo del mensaje como texto plano
    cuerpo = MIMEText(contenido, "plain")
    mensaje.attach(cuerpo)
    
    # Enviar el correo electrónico
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor_smtp:
            servidor_smtp.ehlo()
            servidor_smtp.starttls()
            servidor_smtp.login(correo, contraseña)
            servidor_smtp.sendmail(correo, destinatario, mensaje.as_string())
        print("Correo electrónico enviado con éxito.")
    except Exception as e:
        # Registrar el error utilizando logging
        logging.error(str(e))
        print("No se pudo enviar el correo electrónico.")
    
    #print("Correo electrónico enviado con éxito.")


def main(args):
    """Invoca las funciones de este modulo
    Encargado de obtener los datos del remitente, destinatario
    asi como obtener el archivo de texto que se mandara. Para al final mandar el correo."""
    # Obtener los datos del remitente
    correo, contraseña = obtener_datos_remitente()
    
    # Datos del destinatario
    destinatario = "ingrese el correo al que quieras que lleguen los informes"
    
    # Obtener el nombre del archivo seleccionado
    nombre_archivo = args.archivo + ".txt"
    
    # Enviar el correo electrónico
    enviar_correo(correo, contraseña, destinatario, nombre_archivo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enviar archivo de texto por correo")
    parser.add_argument("archivo", choices=["domain_info", "metadatos", "IP_informe", "testscrapy"], help="Archivo de texto a enviar")
    args = parser.parse_args()
    main()

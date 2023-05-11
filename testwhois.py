# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:01:02 2023

Este script verifica si una página web está en funcionamiento y obtiene información sobre el creador de la página web.

Autor: edo-s
"""
import argparse
import subprocess
import whois

def obtener_creador(url):
    """
    Obtiene el creador de la página web utilizando la biblioteca whois.

    :param url: URL de la página web.
    :type url: str

    :return: Información sobre el creador de la página web.
    :rtype: str
    """
    domain_info = whois.whois(url)

    resultado = f"-INFORME-\n"
    resultado += f"Nombre del dominio: {domain_info.domain_name}\n"
    resultado += f"Registrante: {domain_info.registrar}\n"
    resultado += f"Fecha de registro: {domain_info.creation_date}\n"

    with open("domain_info.txt", "w") as archivo:
        archivo.write(resultado)

    #print(resultado)

def verificar_pagina_web(url):
    """
    Verifica si una página web está en funcionamiento y obtiene información sobre el creador de la página web si está en funcionamiento.
    Lo realizamos utilizando powershell dentro de python
    :param url: URL de la página web.
    :type url: str
    """
    ps_script = '''
    $webUrl = "{url}"  # URL proporcionada por el usuario

    try {{
        $webRequest = [System.Net.WebRequest]::Create($webUrl)
        $webResponse = $webRequest.GetResponse()
        $webResponse.Close()
        Write-Output "La pagina web esta en funcionamiento."
    }} catch {{
        Write-Output "La pagina web no esta en funcionamiento."
        exit 1
    }}
    '''.format(url=url)

    result = subprocess.run(['powershell', '-Command', ps_script], capture_output=True, text=True)

    #print(result.stdout)

    if result.returncode == 0:
        obtener_creador(url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Verificar si una página web está en funcionamiento.')
    parser.add_argument('url', help='URL de la página web')

    args = parser.parse_args()

    verificar_pagina_web(args.url)


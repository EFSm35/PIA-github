# -*- coding: utf-8 -*-

"""
Created on Sun May 7 14:57:10 2023
@author: edo-s
Script encargad de utilizar los modulos que creamos por medio de subcomando de argparse
"""

import argparse
import testimagen
from testimagen import interpret_metadata
import iptest
from iptest import scan_host
from iptest import save_results
import testwhois
from testwhois import verificar_pagina_web
import testcorreofunciones
from testcorreofunciones import main
import scraptheweb
from scraptheweb import run_scraper


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Herramientas de análisis")
    subparsers = parser.add_subparsers(title="Subcomandos", dest="subcommand")

    # Subcomando para interpretar metadatos de una imagen
    parser_metadata = subparsers.add_parser("metadata", help="Interpretar metadatos de una imagen")
    parser_metadata.add_argument("image_path", type=str, help="Ruta de la imagen")

    # Subcomando para análisis de direcciones IP
    parser_ip = subparsers.add_parser("ip", help="Análisis de direcciones IP")
    parser_ip.add_argument("ip", type=str, help="Dirección IP a analizar")

    # Subcomando para verificar una página web
    parser_web = subparsers.add_parser("web", help="Verificar si una página web está en funcionamiento")
    parser_web.add_argument("url", help="URL de la página web")

    # Subcomando para enviar un archivo de texto por correo
    parser_correo = subparsers.add_parser("correo", help="Enviar archivo de texto por correo")
    parser_correo.add_argument("archivo", choices=["domain_info", "metadatos", "IP_informe", "testscrapy"], help="Archivo de texto a enviar")

    # Subcomando para ejecutar el rastreador web
    parser_scrape = subparsers.add_parser("scrape", help="Ejecutar el rastreador web")
    parser_scrape.add_argument("--url", type=str, help="URL para analizar")

    args = parser.parse_args()

    if args.subcommand == "metadata":
        # Interpretar los metadatos de la imagen y guardarlos en un archivo de texto
        interpret_metadata(args.image_path)
    elif args.subcommand == "ip":
        # Realizar el análisis de puertos abiertos
        open_ports = scan_host(args.ip)

        # Guardar los resultados en un archivo de texto
        save_results(args.ip, open_ports)
    elif args.subcommand == "web":
        # Verificar si la página web está en funcionamiento
        verificar_pagina_web(args.url)
    elif args.subcommand == "correo":
        # Enviar archivo de texto por correo
        main(args)
    elif args.subcommand == "scrape":
        # Ejecutar el rastreador web
        if args.url:
            run_scraper(args.url)
        else:
            run_scraper("https://www.example.com")  # Analizar www.example.com como predeterminado

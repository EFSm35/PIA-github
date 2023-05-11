# -*- coding: utf-8 -*-
"""
MODULO encargado de usar scrapy para rastrear informacion de un sitio web para
despues guardarla en una archivo de texto
"""

import argparse
import scrapy
from scrapy.crawler import CrawlerProcess

# Define una araña personalizada para Scrapy
class MySpider(scrapy.Spider):
    name = "myspider"

    def __init__(self, url=None, *args, **kwargs):
        """
        Inicializa la araña personalizada.

        Args:
            url (str): URL para analizar.
            *args: Argumentos posicionales adicionales.
            **kwargs: Argumentos de palabras clave adicionales.
        """
        super().__init__(*args, **kwargs)
        self.start_urls = [url or 'http://www.example.com']

    def parse(self, response):
        """
        Método para el procesamiento de la respuesta del rastreo.

        Args:
            response (scrapy.http.Response): Objeto de respuesta de la solicitud.

        Returns:
            None
        """
        # Extrae y procesa el título de la página
        title = response.css('h1::text').get()
        result = "Título de la página: " + title

        # Extrae y procesa los enlaces de la página
        links = response.css('a::attr(href)').getall()
        result += "\nEnlaces de la página:\n"
        for link in links:
            result += link + "\n"

        with open("testscrapy.txt", "w") as file:
            file.write("-TestScrapy-\n")
            file.write(result)


def run_scraper(url):
    """
    Ejecuta el rastreador de Scrapy.

    Args:
        url (str): URL para analizar.

    Returns:
        None
    """
    # Crea una instancia del proceso del rastreador de Scrapy
    process = CrawlerProcess()

    # Agrega la araña personalizada al proceso del rastreador
    process.crawl(MySpider, url=url)

    # Inicia el proceso del rastreador
    process.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script de Scrapy')

    parser.add_argument('--scrape', action='store_true', help='Ejecutar el rastreador web')
    parser.add_argument('--url', type=str, help='URL para analizar')

    args = parser.parse_args()

    if args.scrape:
        if args.url:
            run_scraper(args.url)
        else:
            run_scraper(None)  # Analizar www.example.com como predeterminado
    else:
        print("No se proporcionó ningún comando. Usa '--scrape' para ejecutar el rastreador.")

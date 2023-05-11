# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:13:06 2023

@author: edo-s

Encargado de escanear los puertos abiertos
"""


import argparse
import nmap

def scan_host(ip_address):
    """
    Escanea un host en busca de puertos abiertos.

    Args:
        ip_address (str): Dirección IP del host a analizar.

    Returns:
        list: Lista de puertos abiertos encontrados.
    """
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments='-p 1-65535 -T4')

    open_ports = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    if nm[host][proto][port]['state'] == 'open':
                        open_ports.append(port)

    return open_ports

def save_results(ip_address, open_ports):
    """
    Guarda los resultados en un archivo de texto.

    Args:
        ip_address (str): Dirección IP analizada.
        open_ports (list): Lista de puertos abiertos.
    """
    filename = 'IP_informe.txt'
    with open(filename, 'w') as file:
        file.write(f"Informe de análisis para la dirección IP: {ip_address}\n\n")
        file.write("Puertos abiertos:\n")
        for port in open_ports:
            file.write(f"- {port}\n")
    #print(f"Los resultados se han guardado en el archivo '{filename}'.")

def main():
    """
    Se configura los comando para usar una IP como argumento (str)
    Realiza las funciones del modulo llamando a las funciones del modulo
    """
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Análisis de direcciones IP.')
    parser.add_argument('ip', type=str, help='Dirección IP a analizar')

    # Obtener la dirección IP como argumento
    args = parser.parse_args()
    ip_address = args.ip

    # Realizar el análisis de puertos abiertos
    open_ports = scan_host(ip_address)

    # Guardar los resultados en un archivo de texto
    save_results(ip_address, open_ports)

if __name__ == '__main__':
    """
    Se configura los comando para usar una IP como argumento (str)
    Realiza las funciones del modulo
    """
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Análisis de direcciones IP.')
    parser.add_argument('ip', type=str, help='Dirección IP a analizar')

    # Obtener la dirección IP como argumento
    args = parser.parse_args()
    ip_address = args.ip

    # Realizar el análisis de puertos abiertos
    open_ports = scan_host(ip_address)

    # Guardar los resultados en un archivo de texto
    save_results(ip_address, open_ports)
    #main()
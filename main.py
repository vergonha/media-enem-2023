from calculo import ENEM
from colorama import Fore
import os

class Interface():

    @staticmethod
    def calcular_media():
        linguagem = float(input(f"{Fore.YELLOW}Nota em Linguagens: "))
        humanas = float(input("Nota em Humanas: "))
        natureza = float(input("Nota em Natureza: "))
        matematica = float(input("Nota em Matemática: "))
        redacao = float(input(f"Nota em Redação: "))
        MEDIA = ENEM(linguagem, humanas, natureza, matematica, redacao)
        return MEDIA.media()

    @staticmethod
    def start():
        os.system('cls||clear')
        ASCII_text = """
    
            .-''-.  ,---.   .--.    .-''-.  ,---.    ,---.        
          .'_ _   \ |    \  |  |  .'_ _   \ |    \  /    |        
         / ( ` )   '|  ,  \ |  | / ( ` )   '|  ,  \/  ,  |        
        . (_ o _)  ||  |\_ \|  |. (_ o _)  ||  |\_   /|  |        
        |  (_,_)___||  _( )_\  ||  (_,_)___||  _( )_/ |  |        
        '  \   .---.| (_ o _)  |'  \   .---.| (_ o _) |  |        
         \  `-'    /|  (_,_)\  | \  `-'    /|  (_,_)  |  |        
          \       / |  |    |  |  \       / |  |      |  |        
           `'-..-'  '--'    '--'   `'-..-'  '--'      '--'        
        ,---.    ,---.    .-''-.   ______     .-./`)    ____      
        |    \  /    |  .'_ _   \ |    _ `''. \ .-.') .'  __ `.   
        |  ,  \/  ,  | / ( ` )   '| _ | ) _  \/ `-' \/   '  \  \  
        |  |\_   /|  |. (_ o _)  ||( ''_'  ) | `-'`"`|___|  /  |  
        |  _( )_/ |  ||  (_,_)___|| . (_) `. | .---.    _.-`   |  
        | (_ o _) |  |'  \   .---.|(_    ._) ' |   | .'   _    |  
        |  (_,_)  |  | \  `-'    /|  (_.\.' /  |   | |  _( )_  |  
        |  |      |  |  \       / |       .'   |   | \ (_ o _) /  
        '--'      '--'   `'-..-'  '-----'`     '---'  '.(_,_).'   
                                                                  
    
    """
        print(f"{Fore.MAGENTA}{ASCII_text}{Fore.RESET}")
        media = Interface.calcular_media()
        print(f"{Fore.YELLOW}Sua média foi de: {Fore.MAGENTA}{media}{Fore.YELLOW} pontos.")



if __name__ == "__main__":
    Interface.start()
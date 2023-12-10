from colorama import init
init()
from colorama import Fore, Back, Style

def log(text, com): #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
    if com == "info":
        print(Fore.BLUE + "[Информация]: " + Fore.RESET + text)
    if com == "error":
        print(Fore.RED + "[Ошибка]: " + Fore.RESET + text)
    if com == "warning":
        print(Fore.YELLOW + "[Предупреждение]: " + Fore.RESET + text)
    if com == "complete":
        print(Fore.GREEN + "[Успешно]: " + Fore.RESET + text)
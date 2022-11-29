import os
import time

def clear():
    os.system('clear||cls')
def print_menu4():
    print('**********************************************************************************************************************************************************************')
    print('*                                                                                                                                                                    *')
    print('*                                                                                                                                                                    *')
    print('*                                                                 \u001b[33;1m ███████╗████████╗ █████╗  ██████╗██╗  ██╗ \u001b[37m                                                        *')
    print('*                                                                 \u001b[33;1m ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝ \u001b[37m                                                        *')
    print('*                                                                 \u001b[33;1m ███████╗   ██║   ███████║██║     █████╔╝  \u001b[37m                                                        *')
    print('*                                                                 \u001b[33;1m ╚════██║   ██║   ██╔══██║██║     ██╔═██╗   \u001b[37m                                                       *')
    print('*                                                                 \u001b[33;1m ███████║   ██║   ██║  ██║╚██████╗██║  ██╗  \u001b[37m                                                       *')
    print('*                                                                 \u001b[33;1m ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝  \u001b[37m                                                       *')
    print('*                                                                                                                                                                    *')
    print("*                                                                                    1.Play                                                                          *")
    print("*                                                                                    2.How to Play                                                                   *")
    print("*                                                                                    3.Back                                                                          *")
    print('*                                                                                                                                                                    *')
    print("**********************************************************************************************************************************************************************")


    option=input("Enter your choice: ")
    if option == "1":
    
     from stack import create_game
    elif option == "2":
     print("4 in a row is a game that........")
     time.sleep(10.0)
     clear()
     print_menu4()
     
    elif option == "3":
          time.sleep(1.0) 
          from menu import print_menu1     
          
          
print(print_menu4())
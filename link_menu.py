import os

def clear():
    os.system('clear||cls')
def print_menu5():
    print("*********************************************************************************************************")
    print('*                                                                                                       *')
    print('*          ██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗       ██╗     ██╗███████╗████████╗              *')
    print('*          ██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗      ██║     ██║██╔════╝╚══██╔══╝              *')
    print('*          ██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██║  ██║█████╗██║     ██║███████╗   ██║                 *')
    print('*          ██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║  ██║╚════╝██║     ██║╚════██║   ██║                 *')
    print('*          ███████╗██║██║ ╚████║██║  ██╗███████╗██████╔╝      ███████╗██║███████║   ██║                 *')
    print('*          ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═════╝       ╚══════╝╚═╝╚══════╝   ╚═╝                 *')
    print('*                                                                                                       *')
    print("*                                          1.Play                                                       *")
    print("*                                          2.How to Play                                                *")
    print("*                                          3.Back                                                       *")
    print('*                                                                                                       *')
    print("*********************************************************************************************************")

    option=input("                                    Enter your choce:")
    if option == "1":  

     from snake import create_snake
    elif option == "2":
     print("Snake game implemeted linked-list. You can enjoy playing it by just clicking up,right,left and down button.")
     clear()

     print_menu5()

     
    elif option == "3":
     clear()
    from menu import print_menu1
     
print(print_menu5())
import time
import os
import time, sys

def clear():
    os.system('clear||cls') 
def print_menu1():
    print('*******************************************************************************')
    print('*                                                                             *')
    print('*                                                                             *')
    print('*                      ██████╗  █████╗ ███╗   ███╗███████╗                    *')
    print('*                     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝                    *')
    print('*                     ██║  ███╗███████║██╔████╔██║█████╗                      *')
    print('*                     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                      *')
    print('*                     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                    *')
    print('*                      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                    *')    
    print("*                                                                             *")
    print("*                                    1.Stack                                  *")
    print("*                                    2.Queue                                  *")
    print("*                                    3.Link-List                              *")
    print("*                                    4.Quit                                   *")
    print('*                                                                             *')
    print("*******************************************************************************")
    
    option=input("Enter your choice: ")
    if option == "1":
     time.sleep(2.0)
     clear()
     from stack_menu import print_menu4
    elif option == "2":
      clear()
      from queue_menu import print_menu3

 
    elif option == "3":
      clear()
      from link_menu import print_menu5

    elif option == "4":
      exit()

    print(print_menu1())

     


print_menu1()
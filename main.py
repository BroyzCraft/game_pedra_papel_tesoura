# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:40:22 2022

@author: x290372
"""

import random

def game(user_choice):
    
    ''' 
    
    Bot escolhe um numero aleatorio entre 0 e 2 indicado como: 
    0 - Pedra, 
    1 - Papel, 
    2 - Tesoura 
    
    '''
    choice = random.randint(0, 2)
    
    ### Calcula vencedor ###
    if user_choice == choice:
        return "Resultado: Empate", choice
    
    elif user_choice == 0 and choice == 2:
        return "Resultado: Você ganhou! =) ", choice
    
    elif user_choice == 1 and choice == 0:
        return "Resultado: Você ganhou! =) ", choice
    
    elif user_choice == 2 and choice == 1:
        return"Resultado: Você ganhou! =) ", choice
    
    else:
        return "Resultado: Você perdeu! =( ", choice

def main():
    
    options = ("Pedra", "Papel", "Tesoura")
    
    ### MENU ###
    print("###  Jogo PEDRA PAPEL E TESOURA  ### \n")
    print("0 - Pedra ")
    print("1 - Papel ")
    print("2 - Tesoura ")
    try:
        user_choice = int(input("Escolha sua opção: "))
    
        ### VALIDA A OPÇÃO DO USUARIO ###
        if (user_choice == 0) or (user_choice == 1) or (user_choice == 2):
            
            msg, bot_choice = game(user_choice)
            
            print("\n")
            print("Sua escolha: " + options[user_choice])
            print("Escolha do Bot: " + options[bot_choice])
            print(msg)
            print("\n")
        
        else:
            print("\n")
            print("Opção Invalida, Tente novamente!")
            print("\n")
            
    except ValueError:
        print("\n")
        print("Opção Invalida, Tente novamente!")
        print("\n")

if __name__ == '__main__':
    while True:
        main()
    
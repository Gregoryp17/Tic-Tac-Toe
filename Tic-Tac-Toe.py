from random import randrange
import os

global lst 

# TABLERO

def display_board(win):

    os.system('cls' if os.name == 'nt' else 'clear')

    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")
    print("|       |       |       |")
    print("|  ",lst[0],"  |  ",lst[1],"  |  ",lst[2],"  |")
    print("|       |       |       |")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")
    print("|       |       |       |")
    print("|  ",lst[3],"  |  ",lst[4],"  |  ",lst[5],"  |")
    print("|       |       |       |")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")
    print("|       |       |       |")
    print("|  ",lst[6],"  |  ",lst[7],"  |  ",lst[8],"  |")
    print("|       |       |       |")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")

    if win == 1:
        print("Usted ha ganado,felicidades :).")
        return
    elif win == 2:
        print("Ha ganado la computadora ;(.")
        return
    elif win == 3:
        print("El juego ha quedado empate :|.")
        return
    elif win == 4:
        print("El movimiento introducido, ya ha sido utilizado. Por favor, intentelo nuevamente. :/")
        enter_move()
    else:
        for i in range(1,9):
            if type(lst[i])==int:
                enter_move()
                break
            if i == 8:
                display_board(3)
                break

# MOVIMIENTO DEL USUARIO

def enter_move(): 

    try:
        movi = int(input("Ingrese su movimiento: "))
        if movi > 0 and movi < 10:
            movi-=1
            if type(lst[movi]) == str:
                display_board(4)
            else:
                lst[movi]="O"
                if lst[0] == "O" and lst[1] == "O" and lst[2] == "O" or lst[6]=="O" and lst[7]=="O" and lst[8]=="O" or lst[0]=="O" and lst[3]=="O" and lst[6]=="O" or lst[2]=="O" and lst[5]=="O" and lst[8]=="O":
                    display_board(1)
                else:
                    draw_move()
        else:
            print("Ha ingresado un movimiento incorrecto ;/. (Recuerda: El número tiene que estar comprendio entre el 0 y 10.)")
    except:
        print("Se ha producido un error ;/.(Recuerda: El número tiene que ser entero.)")

# MOVIMIENTO DE LA MÁQUINA

def draw_move():

    while True:
        a=randrange(9)
        if type(lst[a])==int:
            lst[a]="X"
            if lst[0] == "X" and lst[1] == "X" and lst[2] == "X" or lst[3] == "X" and lst[4] == "X" and lst[5] == "X" or lst[6] == "X" and lst[7] == "X" and lst[8] == "X" or lst[0] == "X" and lst[3] == "X" and lst[6] == "X" or lst[1] == "X" and lst[4] == "X" and lst[7] == "X" or lst[2] == "X" and lst[5] == "X" and lst[8] == "X" or lst[0] == "X" and lst[4] == "X" and lst[8] == "X" or lst[2] == "X" and lst[4] == "X" and lst[6] == "X":
                display_board(2)
                break
            else:
                display_board(0)
                break
            
lst=[1, 2, 3, 4, "X", 6, 7, 8, 9]
display_board(0)
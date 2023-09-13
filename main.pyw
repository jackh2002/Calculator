import PySimpleGUI as sg
from Operations.indices import *
from Operations.basic import *
display = ""
answer = ""
sg.theme("LightGrey6")
layout =  [
          [sg.Text(display,background_color= "White",size=(30,1),expand_x=True,border_width=0,key= "DISPLAY")],
          [sg.Text(answer,justification="right",background_color= "White",size=(30,2),expand_x=True, border_width=0, key= "ANSWER")],
          [sg.Button("M+",size=(3,1),expand_x=True, key = "M+"),sg.Button("M-",size=(3,1),expand_x=True, key = "M-"),sg.Button("MS",size=(3,1),expand_x=True, key = "MS"),sg.Button("MC",size=(3,1),expand_x=True, key = "MC"),sg.Button("AC",size=(3,1),expand_x=True, key = "CLEAR")],
          [sg.Button("1/x",size=(5,2),expand_x=True, key = "RECIPROCAL"),sg.Button("x^2",size=(5,2),expand_x=True, key = "SQUARE"),sg.Button("sqrt()",size=(5,2),expand_x=True, key = "SQRT"),sg.Button("X",size=(5,2),expand_x=True, key = "MULTIPLY")],
          [sg.Button("7",size=(5,2),expand_x=True, key = "SEVEN"),sg.Button("8",size=(5,2),expand_x=True, key = "EIGHT"),sg.Button("9",size=(5,2),expand_x=True, key = "NINE"),sg.Button("/",size=(5,2),expand_x=True, key = "DIVIDE")],
          [sg.Button("4",size=(5,2),expand_x=True, key = "FOUR"),sg.Button("5",size=(5,2),expand_x=True, key = "FIVE"),sg.Button("6",size=(5,2),expand_x=True, key = "SIX"),sg.Button("+",size=(5,2),expand_x=True, key = "ADD")],
          [sg.Button("1",size=(5,2),expand_x=True, key = "ONE"),sg.Button("2",size=(5,2),expand_x=True, key = "TWO"),sg.Button("3",size=(5,2),expand_x=True, key = "THREE"),sg.Button("-",size=(5,2),expand_x=True, key = "MINUS")],
          [sg.Button("0",size=(5,2),expand_x=True, key = "ZERO"),sg.Button(".",size=(5,2),expand_x=True, key = "DECIMAL"),sg.Button("DEL",size=(5,2),expand_x=True, key = "BACK"),sg.Button("= ",size=(5,2),expand_x=True, key = "EQUALS")]
          ]

window = sg.Window("Calculator", layout, element_justification= "center", background_color= "LightGrey")

while True:
    event, values = window.read()
    if event in [sg.WINDOW_CLOSED]:
        break

    #  NON ERROR SPECIFIC  #
    elif display != "ERROR, PLEASE RESET":

        #  OPERATIONS  #
        if event == "SQUARE":
            try:
                display = str(power(display, 2))
            except:
                display = error()
            window["DISPLAY"].update(display)

        elif event == "SQRT":
            try:
                display = str(root(display, 2))
            except:
                display = error()
            window["DISPLAY"].update(display)

        elif event == "ADD":
            try:
                add_check = True
                display += "+"
            except:
                display = error()
            window["DISPLAY"].update(display)

        elif event == "MINUS":
            try:
                minus_check = True
                display += "-"
            except:
                display = error()
            window["DISPLAY"].update(display)

        elif event == "MULTIPLY":
            try:
                multiply_check = True
                display += "x"
            except:
                display = error()
            window["DISPLAY"].update(display)

        elif event == "DIVIDE":
            try:
                divide_check = True
                display += "/"
            except:
                display = error()
            window["DISPLAY"].update(display)

        elif event == "RECIPROCAL":
            display = str(divide(1, display))
            window["DISPLAY"].update(display)


        #  EQUALS  #
        elif event == "EQUALS":
            try:
                if multiply_check == True:
                    backend = display.split("x")
                    answer = multiply(backend[0],backend[1])
                if divide_check == True:
                    backend = display.split("/")
                    answer = divide(backend[0],backend[1])
                if add_check == True:
                    backend = display.split("+")
                    answer = add(backend[0],backend[1])
                if minus_check == True:
                    backend = display.split("-")
                    answer = subtract(backend[0],backend[1])
                display = ""
                window["ANSWER"].update(answer)
                answer = ""
                add_check = False
                minus_check = False
                divide_check = False
                multiply_check = False
            except:
                display = error()
            window["DISPLAY"].update(display)


        #  DELETION  #
        elif event == "CLEAR":
            display = ""
            answer = ""
            window["DISPLAY"].update(display)
            window["ANSWER"].update(answer)

        elif event == "BACK":
            display = display[0:len(display)-1]
            window["DISPLAY"].update(display)


        #  NUMBERS  #
        elif event == "ONE":
            display += "1"
            window["DISPLAY"].update(display)
        elif event == "TWO":
            display += "2"
            window["DISPLAY"].update(display)
        elif event == "THREE":
            display += "3"
            window["DISPLAY"].update(display)
        elif event == "FOUR":
            display += "4"
            window["DISPLAY"].update(display)
        elif event == "FIVE":
            display += "5"
            window["DISPLAY"].update(display)
        elif event == "SIX":
            display += "6"
            window["DISPLAY"].update(display)
        elif event == "SEVEN":
            display += "7"
            window["DISPLAY"].update(display)
        elif event == "EIGHT":
            display += "8"
            window["DISPLAY"].update(display)
        elif event == "NINE":
            display += "9"
            window["DISPLAY"].update(display)
        elif event == "ZERO":
            display += "0"
            window["DISPLAY"].update(display)


        #  DECIMAL POINT  #
        elif event == "DECIMAL":
            display += "."
            window["DISPLAY"].update(display)


    #  ERROR HANDLING  #
    elif event == "CLEAR":
        add_check = False
        minus_check = False
        divide_check = False
        multiply_check = False
        display = ""
        window["DISPLAY"].update(display)

window.close()

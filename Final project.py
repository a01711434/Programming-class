from strings import rosacea, hidratacion, acne, skincare, exfoliacion, rejuvenecimiento, cuerpo, cabello
from time import sleep
import os
'''LISTAS'''
opciones_si_no=["si","no"]
opciones_main=["skincare", "cuidado del cabello"]
opciones_skincare=["cara","cuerpo","regresar","salir"]
opciones_cara=["acné","rosácea","hidratación","exfoliación","rejuvenecimiento","regresar","salir"]
opciones_hidratacion=["base agua","serúm","crema"]
opciones_exfoliacion=["grasa","mixta","seca","sensible"]
opciones_cuerpo=["higiene personal","exfoliación","hidratación","protección solar","cuidado de las uñas",
"cuidado de los pies","depilación","nutrición y ejercicio","descanso adecuado"]
opciones_cabello=["rizado","ondulado","lacio"]

matriz_validacion=[opciones_si_no,opciones_main,opciones_skincare,opciones_cara,opciones_hidratacion,
opciones_exfoliacion,opciones_cuerpo,opciones_cabello]

'''FUNCIONES'''
#Esperar al usuario
def inputUsuario():
    input("Pulse enter para continuar\n\n>>> ")

#Limpiar pantalla
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def validarOpcion(opcion, lista):
    if opcion.lower() in lista:
        index=lista.index(opcion.lower())
        return True, index
    else:
        return False, 0

def opcion_cara():
    print("¿Sobre qué quieres saber?\n")
    while True:
        print("Las opciones son:\n-acné\n-rosácea\n-hidratación\n-exfoliación\n-rejuvenecimiento\n-regresar\n-salir")
        opcion=input(">>> ")
        limpiar_pantalla()
        
        validacion=validarOpcion(opcion, matriz_validacion[3])

        if validacion[0]:
            if validacion[1]==0:
                print(acne[0])
                print("\n¿Quieres saber sobre tratamientos para el acné?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print(acne[1])
                            inputUsuario()
                        limpiar_pantalla()
                        break

            elif validacion[1]==1:
                print(rosacea[0])
                print("\n¿Quieres saber sobre tratamientos para la rosácea?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print(rosacea[1])
                        break
                print("\n¿Quieres saber sobre factores de riesgo de la rosácea?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print(rosacea[2])
                        break
            elif validacion[1]==2:
                print(hidratacion[0])
                print("¿Te gustaría saber un método de hidratación?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print("¿De cuál te gustaría saber más a detalle?")
                            while True:
                                print("Las opciones son:\n-base agua\n-serúm\n-crema")
                                opcion=input(">>> ")
                                limpiar_pantalla()
                                
                                validacion=validarOpcion(opcion, matriz_validacion[4])

                                if validacion[0]:
                                    if validacion[1]==0:
                                        print(hidratacion[1])
                                    elif validacion[1]==1:
                                        print(hidratacion[2])
                                    elif validacion[1]==2:
                                        print(hidratacion[3])
                                    break
                        break
            elif validacion[1]==3:
                print(exfoliacion[0])
                print("¿Qué tipo de piel tienes?")
                while True:
                    print("Las opciones son:\n-grasa\n-mixta\n-seca\n-sensible")
                    opcion=input(">>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[5])

                    if validacion[0]:
                        tipo_cara=validacion[1]
                        if validacion[1]==0:
                            print(exfoliacion[1])
                        elif validacion[1]==1:
                            print(exfoliacion[2])
                        elif validacion[1]==2:
                            print(exfoliacion[3])
                        elif validacion[1]==3:
                            print(exfoliacion[4])
                        break
                print("¿Quieres conocer un tratamiento para tú tipo de piel?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if tipo_cara==0:
                            print(exfoliacion[5][0])
                        elif tipo_cara==1:
                            print(exfoliacion[5][1])
                        elif tipo_cara==2:
                            print(exfoliacion[5][2])
                        elif tipo_cara==3:
                            print(exfoliacion[5][3])
                        break
            elif validacion[1]==4:
                print(rejuvenecimiento[0])
                print("¿Desea conocer datos útiles sobre el rejuvenecimiento de la piel?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        print(rejuvenecimiento[1])
                        print("¿Te gustaría saber sobre procedimientos de rejuvenecimiento?")
                        while True:
                            opcion=input("Debes contestar con si o no\n>>> ")
                            limpiar_pantalla()

                            validacion=validarOpcion(opcion, matriz_validacion[0])

                            if validacion[0]:
                                print(rejuvenecimiento[2])
                                break
                        break
            elif validacion[1]==5:
                opcion_skincare()
            break
    
def opcion_cuerpo():
    print(cuerpo[0])
    print("¿Sobre cuál quieres saber?")
    while True:
        opcion=input("Las prácticas son:\n-Higiene Personal\n-Exfoliación\n"
        "-Hidratación\n-Protección Solar\n-Cuidado de las uñas\n-Cuidado de los pies\n"
        "-Depilación\n-Nutrición y ejercicio\n-Descanso adecuado\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[6])

        if validacion[0]:
            if validacion[1]==0:
                print(cuerpo[1])
            elif validacion[1]==1:
                print(cuerpo[2])
            elif validacion[1]==2:
                print(cuerpo[3])
            elif validacion[1]==3:
                print(cuerpo[4])
            elif validacion[1]==4:
                print(cuerpo[5])
            elif validacion[1]==5:
                print(cuerpo[6])
            elif validacion[1]==6:
                print(cuerpo[7])
            elif validacion[1]==7:
                print(cuerpo[8])
            elif validacion[1]==8:
                print(cuerpo[9])
            break

def opcion_skincare():
    print("¿De qué tema quieres saber?\n")
    while True:
        print("Las opciones son:\n-cara\n-cuerpo\n-regresar\n-salir\n")
        opcion=input(">>> ")
        limpiar_pantalla()
        
        validacion=validarOpcion(opcion, matriz_validacion[2])

        if validacion[0]:
            if validacion[1]==0:
                opcion_cara()
            elif validacion[1]==1:
                opcion_cuerpo()
            elif validacion[1]==2:
                informacion()
            break

def opcion_cabello():
    print(cabello[0])
    print("¿Sobre cuál tipo de cabello quieres saber?")
    while True:
        opcion=input("Los tipos son:\n-Rizado\n-Ondulado\n-Lacio\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[7])

        if validacion[0]:
            if validacion[1]==0:
                print(cabello[1])
                print("\n¿Quieres saber acerca del tratamiento de este tipo de cabello?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print(cabello[2])
                        break
            elif validacion[1]==1:
                print(cabello[3])
                print("\n¿Quieres saber acerca del tratamiento de este tipo de cabello?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print(cabello[4])
                        break
            elif validacion[1]==2:
                print(cabello[5])
                print("\n¿Quieres saber acerca del tratamiento de este tipo de cabello?")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()

                    validacion=validarOpcion(opcion, matriz_validacion[0])

                    if validacion[0]:
                        if validacion[1]==0:
                            print(cabello[6])
                        break
            break

def informacion():
    print("¿De qué tema quieres saber?\n")
    while True:        
        opcion=input("Las opciones son:\n- skincare\n- cuidado del cabello\n\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[1])

        if validacion[0]:
            if validacion[1]==0:
                opcion_skincare()
            else:
                opcion_cabello()
            break
        
    print("\n¿Quieres regresar al menú principal?\n")
    while True:
        opcion=input("Debes contestar con si o no\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[0])

        if validacion[0]:
            if validacion[1]==0:
                informacion()
            break

def main():
    print("Hola me llamo Belleza de Gangnam, es un placer conocerte.\n¿Con quién tengo el placer?")
    nombre=(input(">>> "))
    limpiar_pantalla()

    print("Hola",nombre,"es un placer estar contigo, espero que te podamos ayudar en algo")
    inputUsuario()
    limpiar_pantalla()

    print("Calculemos la cantidad recomendada de agua que debes de ingerir al día...")
    weight=float(input("Ingresa tu peso en kg: "))
    limpiar_pantalla()

    print(f"Para tener una piel saludable, se recomienda consumir aproximadamente {weight*30} ml de agua")
    inputUsuario()
    limpiar_pantalla()

    #Enlistado de las opciones de los temas que maneja el programa: si o no 
    print("Antes de pasar a la información\n"
          "¿Te gustaría una breve definición de skincare y de cuidado del cabello?")
    
    while True:
        opcion=input("Debes contestar con si o no\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, matriz_validacion[0])

        #Definición skincare
        if validacion[0]:
            if validacion[1]==0:
                print(skincare)
                inputUsuario()
                limpiar_pantalla()
            break

    informacion()
    
    print("Hasta luego,", nombre)

main()
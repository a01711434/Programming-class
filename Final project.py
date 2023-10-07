from time import sleep
import os

'''
Listas
'''
lista=["si","no"]
lista1=["skincare", "cuidado del cabello"]
lista2=["cara","cuerpo","regresar","salir"]
lista3=["acné","rosácea","hidratación","exfoliación","rejuvenecimiento","regresar","salir"]
lista4=["base agua","serúm","crema"]

'''
INFORMACIÓN
'''
#Definición skincare y cuidado del cabello
skincare_i=("Skincare:\n"
"Es el cuidado que le damos a nuestra piel para mantenerla saludable.\n"
"Se asocia con las rutinas que seguimos y los productos que usamos.\n"
"Para que la piel de nuestro rostro o cuerpo luzca fresca y sana.\n"
"\nCuidado del Cabello:\n"
"El cuidado del cabello son cuidados que se aplican al cabello.\n"
"Su finalidad es mantener la salud y buena apariencia del mismo.")

acne_i=("El acné es una afección frecuente de la piel (cutánea) que ocurre cuando los folículos pilosos debajo de esta se obstruyen.\n"
"La grasa y las células muertas de la piel tapan los poros "
"y puede haber brotes de lesiones (a menudo llamados granos o espinillas).\n"
"Para la mayoría de las personas, el acné tiende a desaparecer al llegar a los 30 años, "
"pero algunas otras continúan teniendo este problema de la piel aun cuando llegan a los 40 o 50 años.\n\n"
"Un tratamiento promedio dura 21 días y tiene un promedio de 7 días de mejora.\n"
"Si sigues un tratamiento para el acné, te tomará aproximadamente 28 días para ver mejoras en tu piel.\n")

acne_t=("Aquí están los siguientes tratamientos:\n"
"Los objetivos que se persiguen en el tratamiento de esta enfermedad son:\n"
"\tRegular la seborrea.\n"
"\tEvitar la obstrucción del folículo.\n"
"\tDisminuir la población bacteriana.\n"
"\tEvitar las cicatrices.")

rosacea_i=("Es una afección común de la piel que causa rubor o enrojecimiento y vasos sanguíneos visibles en la cara.\n"
"Además, puede producir pequeños bultos llenos de pus.\n"
"Estos signos y síntomas pueden aparecer durante semanas o meses y luego desaparecer por un tiempo\n"
"La rosácea puede confundirse con el acné, otros problemas de la piel o la rubicundez natural.\n\n"
"Algunos síntomas son:\n"
"\tRubor o enrojecimiento facial\n"
"\tVenas visibles\n"
"\tProtuberancias hinchadas\n"
"\tSensación de ardor\n"
"\tProblemas oculaes\n"
"\tNariz agrandada")

rosacea_t=("Medicamentos tópicos que reducen el rubor:\n"
"Para la rosácea leve, el médico puede recetar una crema o un gel que se aplica "
"en la piel afectada.\nLa brimonidina y la oximetazolina reducen el rubor "
"dentro de las 12 horas después de su uso.\n"
"El medicamento debe aplicarse regularmente para mantener las mejoras.\n\n"
"Antibióticos orales:\n"
"El médico puede recetar un antibiótico oral como doxiciclina "
"para la rosácea moderada a grave con protuberancias y granos")

rosacea_a=("Cualquier persona puede desarrollar rosácea.\n"
"Pero es más probable que la tengas si:\n"
"\t-Eres mujer\n"
"\t-Tienes una piel que se quema facilmente con el sol\n"
"\t-Tienes más de 30 años\n"
"\t-Fumas\n"
"\t-Tienes antecedentes familiares de rosácea")


hidratacion_i=("Una piel hidratada es una piel feliz.\n"
"La importancia de la hidratación facial es clave para conseguir una complexión sana y luminosa.\n"
"Una piel hidratada pareca más joven. Los humectantes ayudan a mantener la humedad de la piel y "
"la hidratación le añade agua.\nLa piel deshidratada puede estar seca y grasa a la vez. La piel seca "
"se caracteriza por tener una producción baja de grasa, mientrás que la pied deshidratada simplemente "
"le falta agua.\nCuando tu piel está deshidrata, puede estar más apagada, sin brillo, tirante y con tendencia "
"a inflamarse, congestionarse y a tener erupciones.")

exfoliacion_i=("")

rejuvenecimiento_i=("")

'''
Funciones
'''
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
        
        validacion=validarOpcion(opcion, lista3)

        if validacion[0]:
            if validacion[1]==0:
                print(acne_i)
                print("\n¿Quieres saber sobre tratamientos para el acné?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, lista)

                    if validacion[0]:
                        if validacion[1]==0:
                            print(acne_t)
                            inputUsuario()
                        limpiar_pantalla()
                        break

            elif validacion[1]==1:
                print(rosacea_i)
                print("\n¿Quieres saber sobre tratamientos para la rosácea?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, lista)

                    if validacion[0]:
                        if validacion[1]==0:
                            print(rosacea_t)
                        break
                print("\n¿Quieres saber sobre factores de riesgo de la rosácea?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, lista)

                    if validacion[0]:
                        if validacion[1]==0:
                            print(rosacea_a)
                        break
            elif validacion[1]==2:
                print(hidratacion_i)
                print("¿Te gustaría saber un método de hidratación?\n")
                while True:
                    opcion=input("Debes contestar con si o no\n>>> ")
                    limpiar_pantalla()
                    
                    validacion=validarOpcion(opcion, lista)

                    if validacion[0]:
                        if validacion[1]==0:
                            print("¿De cuál te gustaría saber más a detalle?")
                            while True:
                                print("Las opciones son:\n-base agua\n-serúm\n-crema")
                                opcion=input(">>> ")
                                limpiar_pantalla()
                                
                                validacion=validarOpcion(opcion, lista4)

                                if validacion[0]:
                                    if validacion[1]==0:
                                        print(lista4[0])
                                    elif validacion[1]==1:
                                        print(lista4[1])
                                    elif validacion[1]==2:
                                        print(lista4[2])
                                    break
                        break
            elif validacion[1]==3:
                print(exfoliacion_i)
            elif validacion[1]==4:
                print(rejuvenecimiento_i)
            elif validacion[1]==5:
                opcion_skincare()
            break
    
def opcion_cuerpo():
    print("El cuidado corporal se refiere a las prácticas y rutinas\
          que una persona realiza para mantener la salud y el bienestarde\
          su cuerpo, especialmente la piel y otras partes externas. Existen\
          algunas prácticas comunes del cuidado corporal.")

def opcion_skincare():
    print("¿De qué tema quieres saber?\n")
    while True:
        print("Las opciones son:\n-cara\n-cuerpo\n-regresar\n-salir\n")
        opcion=input(">>> ")
        limpiar_pantalla()
        
        validacion=validarOpcion(opcion, lista2)

        if validacion[0]:
            if validacion[1]==0:
                opcion_cara()
            elif validacion[1]==1:
                opcion_cuerpo()
            elif validacion[1]==2:
                informacion()
            break

def opcion_cabello():
    print("Cabello")

def informacion():
    print("¿De qué tema quieres saber?\n")
    while True:        
        opcion=input("Las opciones son:\n- skincare\n- cuidado del cabello\n\n>>> ")
        limpiar_pantalla()

        validacion=validarOpcion(opcion, lista1)

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

        validacion=validarOpcion(opcion, lista)

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

        validacion=validarOpcion(opcion, lista)

        #Definición skincare
        if validacion[0]:
            if validacion[1]==0:
                print(skincare_i)
                inputUsuario()
                limpiar_pantalla()
            break

    informacion()
    
    print("Hasta luego,", nombre)

main()

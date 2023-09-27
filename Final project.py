
import time
import os 
import random
numero=random.randint(1,100)

#S=skincare, CC=cuidado del cabello
skincare="skincare" 
cuidado_cabello="cuidado del cabello"  
#A=si y B=NO
si="si"
no="no"
#a=cara, b=cuerpo,
lista2=["cara","cuerpo"]
cara ="cara" 
cuerpo="cuerpo" 
##Lista de la c=acné,d=rosácea,e)hidratación,f=exfoliación,g=rejuvecimiento
lista1=["acné","rosácea","hidratación","exfoliación","rejuvecimiento"] 
acne="acné" 
rosacea="rosácea" 
hidratacion="hidratación" 
exfoliacion="exfoliación" 
rejuvecimiento="rejuvecimiento" 
#Productos base de agua, serums, crema de noche
productos_cara_base_agua="productos base de agua" 
serums_cara1="serums" 
crema_noche_cara1="crema de noche" 
#Tipo de piel
sensible="sensible"
mixta= "mixta"
grasa="grasa"
seca="seca"

def buena_eleccion_pregunta():
    while True:
        eleccion = ("¿Fue una buena elección? (si/no): ").lower()
        if eleccion == "si":
            break
        elif eleccion == "no":
            return
#muy bien
def esta_bien():
    return("Esta bien")
    
#Limpiar pantalla
def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

#Introducción al programa, pedir nombre y edad
#Intro problema
def di_hola(nombre):
    print("\nHola",nombre,"es un placer estar contigo.") 
#Water Intake
def water_intake(weight):
    water_intake=weight*30 
    print(f"Para tener una piel saludable, se recomienda consumir aproximadamente {water_intake} ml de agua")

def respuesta(pregunta):
    print(pregunta,"\nMuy bien")
#Definición skincare y cuidado del cabello
def skincare_definición ():
     print("Skincare:\
        \nEs el cuidado que le damos a nuestra piel para mantenerla saludable.\
        \nSe asocia con las rutinas que seguimos y los productos que usamos.\
        \nPara que la piel de nuestro rostro o cuerpo luzca fresca y sana.\
        \n\nCuido del Cabello:\
        \nEl cuidado del cabello son cuidados que se aplican al cabello.\
        \nSu finalidad es mantener la salud y buena apariencia del mismo.")
#Buena elección
#Definición Acné
def acné_definición():
    print("El acé es una afección frecuente de la piel (cutánea) que ocurre cuando los folículos pilosos debajo de esta se obstruyen.\
                \nLa grasa y las células muertas de la piel tapan los poros\
 y puede haber brotes de lesiones (a menudo llamados granos o espinillas).\
                \nPara la mayoría de las personas, el acné tiende a desaparecer al llegar a los 30 años,\
 pero algunas otras continúan teniendo este problema de la piel aun cuando llegan a los 40 o 50 años.") 
    time.sleep(18)
#Tratamiento acne promedio
def tratamiento_acné_promedio():
    print("Un tratamiento promedio dura 21 días y tiene un promedio de 7 días de mejora.")
    time.sleep(6)
#Total de días de un tratamiento de acne:
def acne_duracion_tratamiento():
    tratamiento_dias= 21
    mejora_dias=7
    total_dia = tratamiento_dias + mejora_dias 
    print(f"Si sigues un tratamiento para el acné, te tomará aproximadamente {total_dia} días para ver mejoras en tu piel.")
    time.sleep(6)
#Tratamientos acné:
def tratamientos_acne():
    print("Aquí están los siguientes tratamientos:\
    \nLos objetivos que se persiguen en el tratamiento de esta enfermedad son:\
    \n\tRegular la seborrea.\
    \n\tEvitar la obstrucción del folículo.\
    \n\tDisminuir la población bacteriana.\
    \n\tEvitar las cicatrices.")
    time.sleep(5)
    limpiar_pantalla()
#Información completa para imprimir del acné y los tratamientos 
def completo_acne():
    acné_definición()
    limpiar_pantalla()
    tratamiento_acné_promedio()
    limpiar_pantalla()
    acne_duracion_tratamiento()
    limpiar_pantalla()
    pregunta1=str(input("¿Qiéres saber sobre algún tratamiento?\nSi o no: ")).lower
    if pregunta1==si:
        tratamientos_acne()
        limpiar_pantalla()

#definicion rosácea
def definicion_rosacea():
    print("Es una afección común de la piel que causa rubor o enrojecimiento y vasos sanguíneos visibles en la cara.\
    \nAdemás, puede producir pequeños bultos llenos de pus.\
    \nEstos signos y síntomas pueden aparecer durante semanas o meses y luego desaparecer por un tiempo\
    \nLa rosácea puede confundirse con el acné, otros problemas de la piel o la rubicundez natural.\
    \nAlgunos síntomas son:\
    \n\tRubor o enrojecimiento facial\
    \n\tVenas visibles\
    \n\tProtuberancias hinchadas\
    \n\tSensación de ardor\
    \n\tProblemas oculaes\
    \n\tNariz agrandada")
    time.sleep(20)
    limpiar_pantalla()
#Tratamiento Rosacea:
def tratamiento_rosacea():
    print("Medicamentos tópicos que reducen el rubor:\
\nPara la rosácea leve, el médico puede recetar una crema o un gel que se aplica\
 en la piel afectada.\nLa brimonidina y la oximetazolina reducen el rubor\
 dentro de las 12 horas después de su uso.\
        \nEl medicamento debe aplicarse regularmente para manterner las mejoras\
        \n\nAntibióticos orales:\
        \nEl médico puede recetar un antibiótico oral como doxiciclina\
        para la rosácea moderada a grave con protuberancias y granos")
    time.sleep(13)
    limpiar_pantalla()

#antecedentes rosácea
def antecedentes_rosacea(lista3):
    lista3=("-Eres mujer","-Tienes una piel que se quema facilmente con el sol",
            "-Tienes más de 30 años","-Fumas","-Tienes antecedentes familiares de rosácea")
    print("Cualquier persona puede desarrollar rosácea.\
 Pero es más probable que la tengas si: ")
    antecedentes_rosacea(lista3)         
    time.sleep(7)
    limpiar_pantalla()
def trata_rosacea():
    #definicion rosacea
    definicion_rosacea()
    while True:
        pregunta2=str(input("¿Quiéres saber de algún tratamiento?\
    \n si o no\
    \n ")).lower()
        esta_bien()
        time.sleep(3)
        limpiar_pantalla()
        if pregunta2 == no: 
            esta_bien()
            break
        elif pregunta2==si: 
            tratamiento_rosacea()
        else: 
            print("Tienes que responder con si o no")
            input("Respuesta: ")
        break
    while True: 
        pregunta3=str(input("¿Quiéres saber los factores de riesgo?\
        \n si o no\
        \n ")).lower()
        time.sleep(3)
        limpiar_pantalla()
        if pregunta3==no: 
            esta_bien()
            break
        elif pregunta3 == si:
        #antecedenstes rosacea o factores de riesgo
            antecedentes_rosacea()
        else: 
            print ("Tienes que responder con si o no")
            input("Respuesta: ")
        break

#hidratación
def hidratacion_cara():
     print("Una piel hidratada es una piel feliz.\
    \nLa importancia de la hidratación facial es clave para conseguir una complexión sana y\
    luminosa.\nUna piel hidratada pareca más joven. Los humectantes ayudan a mantener la humedad de la piel y\
    la hidratación le añade agua.\nLa piel deshidratada puede estar seca y grasa a la vez. La piel seca\
    se caracteriza por tener una producción baja de grasa, mientrás que la pied deshidratada simplemente\
    le falta agua.\nCuando tu piel está deshidrata, puede estar más apagada, sin brillo, tirante y con tendencia\
    a inflamarse, congestionarse y a tener erupciones.")
    
    
#Metodos de hidratación
def metodos_hidratacion():
    lista4=print("1.Utiliza productos con base de agua\n2.Añade serums a tu rutina\n3.Utiliza una crema de noche")
    time.sleep(4)
    limpiar_pantalla()
#Metodo hidratacion base agua cara
def hidratacion_base_agua_cara():
    print("La clave para la hidratación es el agua. Prueba un gel hidratante a base de agua después\
 de una rutina de limieza y exfoliación facila para recuperar la hidratación en tu cara\
    \nAlgunos ejemplos son:\nThe True Cream Moisturizing Bob de Belif:\
 Esta crea está formulada con extracto de hoja de consuelda, un igrediente humectante.\
    \nMoisture Surge 100H Auto-Replenishing Hydrator De Cliniquie:\
 Formulada con aloe ver y ácido hialurónico.\nVicky Aqualia Thermal Ligera 50ml:\
 Es una crema hidratante de textura ligera está indicada especialemente para el cuidado\
 de la piel sensible y deshidratada.\nGel Hydro Boost de Neutrogena:\
 No contiene ni aceites ni perfumes. Refresca la peil y es recomendada para pieles\
 muy secas.\nGel Crema Non-Stop 48 Horas de Hidratación de Yves Rocher:\
 Hidrata la piel durante 48 horas, además deja un rostro fresco y luminoso desde la mañana hasta la noche.\
    \nBioderma Hydrabio Gel-Creme: Alisa la textura de la piel, a la vez que aporta una\
 sensación de frescura y bienestar.\nEstas son algunas cremas a base de agua que son ligeras y no engrasan la piel.") 
    time.sleep(30)
    limpiar_pantalla()
# Hidratacion serum cara
def hidratacion_serum_cara():
    print("El serum es un concentrado cosmético que se aplica antes de la crema hidratante\
 por la mañana y por la noche sobre rostro, cuello y escote.\nA diferencia de la crema hidratante, el sérum lleva una concentración\
 mayor, por lo que solo es necesario aplicar unas pequeñas gotas para que el producto\
 penetre sobre la piel y lo repare.\nLos serums tienen normalmente una textura muy ligera que se absorbe de forma fácil,\
 además de no dejar sensación grasa ni pegajosa en la piel.\nEs un producto\
 fundamental en el cuidado diario del rostro.\nAlgunos serums en el mercado son:\
\nVera & the Birds Plum Up Serum\nIsidin Hyaluronic Concetrate\nFilorga Age-Purify Intensive\
\nLancôme Advanced Génifique Youth Activating Serum\nL'Oréal Paris 1.5% Hyaluronic Acid Revitalift Filler Serum")
    time.sleep(30)
    limpiar_pantalla()
#Hidratacion crema noche cara
def crema_noche_cara():
    print("Estas cremas reparan, hidratan y protegen la piel por la noche\
\nUriage 'Age Lift'\nRoC 'Retinol Correxion'\nCocunat 'The Absolute'\nGarnier 'Aloe Hialurónico'\
\nOlay Retinol 24\nNivea 'Cellular Luminous'")
    time.sleep(10)
    limpiar_pantalla()
def pregunta7():
    pregunta7=input("¿Quiéres saber de algun tratamiento en el mercado para tu tipo de piel?\nSi o no:").lower()
    return (pregunta7)
def sabermás():
    print("¿Quiéres conocer sobre tres productos con este tratamiento? ")
#Secreto de la hidratación:
def secreto():   
        while True:    
            secreto1=str(input("Tenemos un ingrediente secreto de la exfoliación, para poder saberlo tendrás que adivinar un numero random\
 del 1 al 100.\n¿Estás dispuesto?\nsi o no: "))
            if secreto1.lower()== no:
                print("¡Hasta luego!")
                break #Sale del juego si el usuario dice que no

            if secreto1.lower() == si: 
                numero=random.randint(1,100)
                intento=0 
                conteo=0
          
                while True:
                        intento=int(input("En que número estoy pensando\n"))
                        conteo += 1

                        if intento > numero: 
                            print("El número que estoy pensando es menor")
                        elif intento < numero: 
                            print("El numero que estoy pensando es mayor")
                        else:
                            print("Felicidades, adivinaste el número")
                            time.sleep(1)  

                        if 1<= conteo <=7:
                            print("Intentos:", conteo)
                            print("Gran trabajo! Acaso lees la mente?\nEl ingrediente secreto de la exfoliación es...")
                            time.sleep(3)
                            print("El Ácido Hialurónico")
                            time.sleep(6)
                        else: 
                            print("lo lograste, pero tus intentos fueron más del límite.")
                        
                        break
            else:
                print("Por favor, ingresa si o no.")
                continue
            break
def trata_hidratación():
    hidratacion_cara()
    time.sleep(25)
    limpiar_pantalla()
    while True:
        pregunta4=str(input("¿Te gustaría saber un método de hidratación?\nSi o no: "))
        esta_bien()
        limpiar_pantalla()
        if pregunta4== no: 
            esta_bien()
            break 
        elif pregunta4==si:
            metodos_hidratacion()
            esta_bien()
            while True: 
                curious=str(input("¿Te gustaría saber más a detalle de cada uno?\nSi o no: "))
                if curious== no:
                    esta_bien()
                    break
                elif curious==si:
                    while True: 
                        curious2=str(input("¿De cuál te gustaría saber más a detalle?\
    \n1.Productos base de agua\n2.Serums\n3.Crema de noche\nRespuesta: ")).lower()
                        time.sleep(4)
                        limpiar_pantalla()
                        if curious2==productos_cara_base_agua:
                            #hidratación base agua cara
                            hidratacion_base_agua_cara()
                        elif curious2==serums_cara1:
                            #hidratacion serum cara
                            hidratacion_serum_cara()
                        elif curious2==crema_noche_cara1:
                            #hidratacion crema noche cara
                            crema_noche_cara()
                        else: 
                            print("Tienes que responder con Productos base de agua\nSreum\Crema de noche\n")
                            continue
                        break
        else: 
            print("Tienes que responder con si o no: ")
            continue
        
        secreto()
        break

def exfoliación_info(): 
    while True:
        pregunta5=str(input("Quiéres saber de algún exfoliante?\n Si o no: ")).lower()
        print("Exfoliar la cara es una rutina completamente necesaria, una de las tareas\
            más básicas para disfrutar de un cutis sano y sin impurezas.\
            \nLa exfoliación es una parte importante de la limpieza de la piel, ya que\
            además de eliminar las células muertas que se quedan pegadas en la superficie,\
            favorecen la renovación celular y devuelve a la pie su suavidad y luminosidad, ayudando a\
            eliminar las marcas de la piel y manteniéndola oxigenada.")
        time.sleep(15)
        limpiar_pantalla()
        print(pregunta5)
        esta_bien()
        if pregunta5==no:
            print({esta_bien()},". Adiós")
            break
        elif pregunta5== si:
                print("Como en todos los pasos de una rutina de cuidado facial, a la hora\
                    de exfoliar la cara es importante elegir un producto que se adapte\
                    a las necesidades de tu piel.\nEs por eso que: ")
                while True:
                    pregunta6=str(input("¿Qué tipo de piel tienes?:\nGrasa\nMixta\nSeca\nSensible\n")).lower()
                    print(pregunta6)
                    time.sleep(8)
                    limpiar_pantalla()
                    if pregunta6==sensible:
                        print("Un exceso de producto puede provocar picor, quemazón, aumentar el enrojecimiento o los brotes de acné\
                        y en algunos casos puede producir hasta manchas. Se recomienda exfoliar la piel solo una vez o como máximo dos veces por\
                        semana.\nUna sustancia que es muy utilizada por su propiedad para exfoliar y ablandar las capas más superficiales \
                        es el ácido láctico, una sustancia derivada de la proteína de leche vegetal.\
                        \nEl uso de este es mediante un peeling facial de ácido láctico que se aplica directamente dobre la piel. ")
                        pregunta7()
                        if pregunta7==si:
                            time.sleep(12)
                            limpiar_pantalla()
                            print("Algunos enfoliantes en el mercado son:\nExfoliante Fisiológico Ultra Fino de la Roche Posay\
                            \nManuka Tree Pasta Exfoliante de Ziaja\nRose Sugar Scrub Exfoliante Facial de Lancôme\
                            \nExfoliante Suave Purificante de Avene\nNumee Sérum Exfoliante Ácido Láctico")
                            time.sleep(8)
                            limpiar_pantalla()
                    elif pregunta6==grasa:
                        print("Cuando tienes piel grasa, las células muertas tienden a permanecer más tiempo. Por ello\
                        la exfoliación es clave.")
                        pregunta7()
                        if pregunta7==si:
                            print(" Se roecomienda someterse a un peeling de ácido salicílico, un betahidroxiácido\
                        capaz de eliminar la grasa que obstruye los poros. Es un tipo de exfoliación muy segura para todo\
                        tipo de pieles y sin efectos secundarios. También ayuda a reducir eficazmente las espinillas\
                        sin dejar imperfecciones o cicatrices importantes. Sin embargo, estos peeling no deben practicarse en casa\
                        \nDebe realizarlos en una clínica un médico especializado.") 
                        time.sleep(13)
                        limpiar_pantalla()
                        print
                    elif pregunta6==seca:
                        print("Las pieles más secas se pueden exfoliar cada 15 días. Es importante que entiendas que no\
                    por exfoliar con frecuencia tu piel vas a conseguir una apariencia más sana y suave.")
                        time.sleep(10)
                        limpiar_pantalla()
                        pregunta7()
                        if pregunta7==si:
                            print("El ácido glicólico, generalmente se usa en piel seca por su capacidad de exfoliar\
                        las células muertas y mejorar la hidratación de la piel. Lo ideal es usarlo en productos que puedan\
                        dejarse en la piel por tiempo prolongado, esto permite ir eliminando los enlaces que\
                        mantienen unidas las células muertas en la piel.")
                    elif pregunta6==mixta:
                        print("Los exfoliantes para las pieles secas eliminan impurezas y además purifica la piel\
                    eliminando la aparicion de cebo y dejando la piel mate. ")
                        pregunta7()
                        if pregunta7==si:                
                            print("Los exfoliantes beta-hidroxiácidos (BHA) son un tipo de ácidos óleo-solubles,\
                    lo que les permite penetrar en los folículos de la piel y eliminar la suciedad y el sebo acumulado en los poros")
                    else:
                        print("Debes contestar con alguna de las opciones")
                        continue
                    break
        else:
            print("Responder con si o no")
            continue
        break

def trata_rejuvecimiento():
    print("Se refiere a las diversas prácticas, productos y técnicas dirigidas a mantener una apariencia facial juvenil y saludable a medida que uno envejece.")
    time.sleep(5)
    limpiar_pantalla()
    while True: 
        rutina_piel=str(input("¿Quiéres saber acerca de algunos puntos claves para la piel?\nRespuesta si o no: ")).lower()
        if rutina_piel=="si":
            print("1-Rutina de cuidado de la piel: Es un aspecto fundamental del rejuvecimiento de la piel.\
            \n\tEsto a menudo incluye limpieza, exfoliación, hidratación u la aplicación de bloqueador solar.\
            \n\tLa limpieza regular ayuda a eliminar la suciedad e impurezas, la exfoliación ayuda a eliminar celúlas muertas de la\
piel y la hidratación mantiene la piel hidratada. ")
            time.sleep(15)
            limpiar_pantalla()
            print("2-Protección solar: Proteje la piel de los dañinos rayos UV del sol, es una de las estrategias más\
efectivas contra el envejecimiento. La exfoliación prolongada al sol puede llevar al envejecimiento prematuro, incluyendo arrugas, lineas finas\
y manchas de la edad. Siempre use protector solar con protección de amplio espectro, use ropa protectora y utilice gafas de sol y sombreros.")
            time.sleep(15)
            limpiar_pantalla()
            while True:
                procedimientos=str(input("¿Te gustaría saber sobre algunos procedimientos?\nRespuesta si o no: ")).lower()
                if procedimientos==no:
                    print("Esta bien")
                    break
                elif procedimientos==si:
                    print("Procedimientos de Rejuvecimiento Facial:\n1Botox y rellenos dérmicos: Se utilizan para suavizar arrugas y lineas finas, asi como para restaurar\
 volumen en áreas como los labios y las mejillas.\n2-Lifting facial: También conocido como ritidectomia, es un procedimiento quirúrgico\
 elimina el exceso de piel y reafirma los tejidos subayacentes para reducir la flacidez y mejorar la apariencia del rostro.\n3-Peelings químicos: Implican la aplicación\
 de una solución química en la piel para eliminar las capas superficiales dañadas y estimular la regeneración celular. Esto puede mejorar la tectura\
 y el tono de la piel.\n4.Microdermoabrasión: Este procedimiento exfolia suavemente la capa superior de la piel para eliminar las células muertas y prover\
 la producción de colágeno, lo que puede mejorar la apariencia de la piel.\n5-Terapia con láser: Los tratamientos con láser \
 se utilizan para tratar arrugas, cicatrices, manchas solares y otros problemas de la piel mediante la estimulación del colágeno")
                    time.sleep(25)
                    limpiar_pantalla()
                else: 
                    print("Debes elegir si o no")
                    continue
                break
            while True: 
                dieta=str(input("¿Quiéres sabes sobre alguna dieta?\nRespuesta si o no: ")).lower()
                if dieta==no:
                    esta_bien()
                    break
                elif dieta==si:
                    print("Una nutrición adecuada desempeña un papel crucial en el mantenimiento de una piel saludable y juvenil.\
                          \nUna dieta rica en antioxidantes, vitaminas (especialmente las vitaminas A, C y E) y \
 ácidos grasos esenciales puede promover una piel sana. Manténgase hidratado bebiendo suficiente agua.")
                    time.sleep(14)
                    limpiar_pantalla()
                else:
                    print("Debes elegir si o no")
                    continue
                break
            while True:
                estilo_vida=str(input("¿Quiéres saber los factores de estilo de vida?\nRespuesta si o no: ")).lower()
                time.sleep(3)
                limpiar_pantalla()
                if estilo_vida==no:
                    esta_bien()
                elif estilo_vida==si:
                    print("Las elecciones de estilo de vida, como no fumar y limitar el consumo de alcohol,\
pueden contribuir a una piel con mejor aspecto. Fumar, en particular, puede acelerar el proceso de envejecimiento y causar arrugas.")
                    time.sleep(9)
                    limpiar_pantalla()
                else:
                    print("Debes elegir si o no")
                    time.sleep(3)
                    limpiar_pantalla()
                    continue
                break
            while True:
                ejercicio=str(input("¿Quiéres saber si el ejercicio influye?\nRespuesta si o no: ")).lower()
                time.sleep(2)
                limpiar_pantalla()
                if ejercicio==no:
                    esta_bien()
                    break
                elif ejercicio==si:
                    print("La actividad física regular puede mejorar la circulación,lo que puede beneficiar a la piel al proporcionar más nutrientes y oxígeno a las células cutáneas.\
                    \nEl ejercicio también puede ayudar a reducir el estrés, que se sabe que afecta la salud de la piel.")
                    time.sleep(10)
                    limpiar_pantalla()
                else: 
                    print("Debes elegir si o no")
                    time.sleep(3)
                    limpiar_pantalla()
                    continue
                break
            while True:
                sueño=str(input("¿Quiéres averiguar si el sueño influye en algo?\nRespuesta si o no: ")).lower()
                time.sleep(2)
                limpiar_pantalla()
                if sueño==no:
                    esta_bien()
                elif sueño==si:
                    print("Un sueño adecuado es esencial para la regeneración y reparación de la piel.\
                          \nLa falta de sueño puede llevar a ojeras y una piel de aspecto cansado.")
                    time.sleep(8)
                    limpiar_pantalla()
                else:
                    print("Debes elegir si o no")
                    time.sleep(2)
                    limpiar_pantalla()
                    continue
                break
        break
def cuerpo_info():    
    print("El cuidado corporal se refiere a las prácticas y rutinas que una persona realiza para mantener la salud y el bienestar\
de su cuerpo, especialmente la piel y otras partes externas.\nExisten algunas prácticas comunes del cuidado corporal.")
    time.sleep(6)
    limpiar_pantalla()
    while True: 
        practicas_comunes=str(input("Las prácticas comunes son:\nHigiene Personal\nExfoliación\nHidratación\nProtección Solar\nCuidado de las uñas\
        \nCuidado de los pies\nDepilación\nNutrición y ejercicio\nDescanso adecuado\nSi no quieres saber de ninguno pon 'no'.\n¿Cuál eliges?: ")).lower()
        time.sleep(2)
        limpiar_pantalla()
        if practicas_comunes==no:
            esta_bien()
            break
        elif practicas_comunes== "higiene personal":
            print("El cuidado corporal comienza con la higiene personal diaria. Esto incluye tomar baños o duchas regulares para mantener la piel limpia y\
libre de suciedad y sudor. El uso de jabón suave y agua tibia es esencial para no eliminar los aceites naturales de la piel.\
\nOtro factor que va a ayudar mucho al lavado de todas las áreas del cuerpo de una persona, es el cambio y el lavado de las ropas de forma periódica,\
además del uso de las prendas de vestir y tener los mismos, muy limpios y también que sean adecuados a las circunstancias del entorno en el que se encuentra.\
\nLos Objetivos de la Higiene Personal, son las conservación y la prevención de las infecciones y de las enfermedades, como también el mejorar la salud física de una persona.")
            time.sleep(20)
            limpiar_pantalla()
            continue
        elif practicas_comunes=="exfoliación":
            print(" La exfoliación se refiere a la eliminación de células muertas de la piel. Puedes hacerlo utilizando exfoliantes suaves o cepillos corporales.\
            \nLa exfoliación regular puede ayudar a mantener la piel suave y renovada.\nEsta técnica del peeling corporal puede realizarse tanto en invierno como en verano.\
            \nY según el tipo de piel y de producto específico utilizado, se puede exfoliar de dos a tres veces por semana. Una buena forma de aplicarlo es en la ducha, sobre la piel mojada, con una manopla o con\nlas propias manos.\
            \nSe deben realizar movimientos suaves, en sentido circular y ascendentes. Y al finalizar el tratamiento, hay que aclarar con agua tibia y terminar con agua más fría.\
            \nEste proceso no es doloroso ya que consiste en exfoliar la capa más superficial de la piel con la finalidad de eliminar las estrías, cicatrices, acné o cualquier tipo de imperfecciones.")
            time.sleep(25)
            limpiar_pantalla()
            continue
        elif practicas_comunes=="hidratación":
            print("Es importante mantener la piel hidratada para prevenir la sequedad y la descamación. Usar lociones o cremas hidratantes después de la ducha puede ayudar a retener la humedad en la piel.\
            \nMantener una correcta hidratación es fundamental para nuestro bienestar.\
            \nDe acuerdo a los especialistas del sector salud, una hidratación adecuada favorece el buen funcionamiento del intestino y de los riñones, regula la temperatura corporal, ayuda a la digestión de los alimentos,etc...\
            \nDe esta forma, explican que, para mantener una buena salud no sólo es importante la dieta correcta, sino una adecuada hidratación del cuerpo, dependiendo del peso, talla, edad y temporada de año.")
            time.sleep(16)
            limpiar_pantalla()
            continue
        elif practicas_comunes=="protección solar":
            print("Todos los días, tu piel está expuesta a la radiación ultravioleta del sol y está potencialmente sometida a sus múltiples daños: quemaduras solares, envejecimiento y, lo más importante, cáncer de piel.\
            \nLa protección contra los daños causados por el sol es crucial. El uso de protector solar antes de exponerse al sol ayuda a prevenir el envejecimiento prematuro de la piel y reduce el riesgo de cáncer de piel.")
            time.sleep(15)
            limpiar_pantalla()
            while True:
                definicion_protector_solar=str(input("¿Quiéres saber que es el protector solar?\nRespuesta si o no: ")).lower()
                if definicion_protector_solar==no:
                    esta_bien()
                    time.sleep(2)
                    limpiar_pantalla()
                    break  
                elif definicion_protector_solar==si:
                    print("El protector solar es un producto cuya función es la de proteger la piel impidiendo el paso de los rayos UV, y reduciendo su penetración con la finalidad de que no perjudiquen nuestros tejidos ni las células existentes en ellos.\
                    \nLa importancia del protector solar recae en la capa de seguridad que ofrece en contra de los rayos UVB y los UVA;\
los primeros son los causantes de las quemaduras en la piel, mientras que los segundos ocasionan la pérdida de elasticidad, arrugas y otros efectos relacionados al fotoenvejecimiento.")  
                    time.sleep(19)
                    limpiar_pantalla()
                    break
                else: 
                    print("Debes contestar con si o no")
                    continue
            continue
                
        elif practicas_comunes=="cuidado de las uñas":
            print("Mantener las uñas limpias y recortadas es parte del cuidado corporal. También puedes aplicar esmalte de uñas si lo deseas.")
            time.sleep(5)
            limpiar_pantalla()
            continue
        elif practicas_comunes=="cuidado de los pies":
            print("El cuidado de los pies implica mantenerlos limpios, recortar las uñas de los pies y usar calzado adecuado para prevenir problemas como los hongos en las uñas o los callos.\
            \nEn muchos sitios se ofrecen servicios de pedicura, tratamientos cosméticos embellecedores y hasta sesiones de masajes exclusivamente para los pies.\
            \nSi bien no vienen mal de vez en cuando, no son suficiente para darle un buen cuidado a esta parte del cuerpo.\
            \nAdoptar una buena rutina de cuidado de los pies es lo ideal. De esta manera los mantendremos saludables, además de que lucirán hermosos. Para ello, existen distintos remedios y consejos son muy fáciles de llevar a cabo.")
            time.sleep(20)
            limpiar_pantalla()
            while True:
                consejos_pies=str(input("¿Quiéres saber algunos consejos para el cuidado de la piel?\nRespuesta si o no: ")).lower()
                limpiar_pantalla()
                if consejos_pies==no:
                    esta_bien()
                    time.sleep(2)
                    limpiar_pantalla()
                    break
                elif consejos_pies==si:
                    lista_pies=["Usa el calzado adecuado","Elige los mejores calcetines","Ten cuidado al andar descalzo","Evita caminar por ciertas superficies","Date masajes y prepárate baños para pies"\
                    "Hidrata tus pies regularmene","Ocúpate de las durezas y callos","Cuida las uñas","Lava y seca tus pies a diario"]
                    print (lista_pies)
                    time.sleep(7)
                    limpiar_pantalla()
                    break
                else:
                    print("Debes contestar con si o no ")
                    time.sleep(2)
                    limpiar_pantalla()
                    continue
            continue
        elif practicas_comunes=="depilación":
            print(" Algunas personas también incluyen el cuidado del cabello corporal en su rutina de cuidado corporal. Esto puede incluir el afeitado o depilación de ciertas áreas del cuerpo.\
            \nExisten varios tipos de serviciós en los centros de estética. Por alta demando, en el séctor se han ido desarrollando métodos más eficaces e indoloros\
para eliminar eficazmente el vello de cualquier parte del cuerpo. Existen 8 tipos de depilación:")              
            depilación_lista=["Con cuchilla","Con cera","Con crema","Con hilo","Con aparatos mecánicos","Con láser","Luz Pulsada","Termoquímica"]
            print (depilación_lista)
            time.sleep(16)
            limpiar_pantalla()
            while True:
                tipos_depilación=str(input("¿Quiéres saber sobre alguno de estos a profundidad?\nRespuesta si o no ")).lower()
                time.sleep(2)
                limpiar_pantalla()
                if tipos_depilación==no:
                    esta_bien()
                    time.sleep(2)
                    limpiar_pantalla()
                    break
                elif tipos_depilación==si:
                    print(depilación_lista)
                    time.sleep(6)
                    cual_depilación=str(input("¿Acerca de cuál quieres saber?:\n")).lower() 
                    limpiar_pantalla()
                    if cual_depilación=="con cuchilla":
                        print("Es el método más utilizado, el más rápido y sencillo para eliminar el vello de cualquier parte del cuerpo. Puedes realizarlo cómodamente en casa.\
                        \nPero tiene el inconveniente de que el pelo no se arranca de raíz, por lo que crece en un breve plazo de tiempo.")
                        time.sleep(9)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="con cera":
                        print("Es uno de los métodos más tradicionales. Se sigue usando por su coste más económico y porque es una técnica duradera y rápida. Se adapta muy bien a cualquier parte del cuerpo.\
                        \nPero este tipo de depilación cada vez está siendo menos demandado debido a las técnicas más nuevas que están apareciendo en el mercado, menos dolorosas y más efectivas.\
                        \nExisten varios tipos de depilación a la cera: fría, caliente o tibia.")
                        time.sleep(7)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="con crema":
                        print("su efectividad en bastante pobre, pues el pelo se rasura, no se arranca de raíz, de manera que crece en 2 o 3 días.\
                        \nPosee la ventaja de que es totalmente indoloro y no irritan la piel. Su uso es muy sencillo: extender la crema sobre la zona a tratar, dejarla actuar un tiempo y retirar con una espátula.")
                        time.sleep(7)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="con hilo":
                        print("Este método es más recomendado para las zonas faciales (bigote, cejas, mentón…), pues muy idóneo para perfilar y definir.\
                        Es rápido, poco doloroso y muy eficaz. Pero no vale para zonas más grandes, por una cuestión de tiempo y paciencia…")
                        time.sleep(7)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="con aparatos mecánicos":
                        print("Las maquinillas eléctricas son un tipo de depilación muy habitual en las casas, pues es cómodo de usar, duradero y rápido.\
                            \nPero como contra, es bastante doloroso y tiende a producir problemas con el vello enconado.")
                        time.sleep(7)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="con láser":
                        print("Este es el tipo de depilación más popular y demandado actualmente.\
                        \nSu principal ventaja es su eficacia pues es una manera definitiva de eliminar el vello.\
                        \nExisten varios tipos de láser en función del tipo de vello y piel, pero todos ellos tienen igual eficacia.\
                        \nEl coste es mayor, pero su eficacia y resultados inigualables.")
                        time.sleep(7)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="luz pulsada":
                        print("Esta depilación es similar al láser en que también es totalmente definitiva.\
                            \nTiene la ventaja añadida de que es eficaz para todo tipo de piel (el láser funciona mejor en pieles más oscuras).\
                            \nDe igual manera el coste es más alto, pero es totalmente definitivo, lo que supone una ventaja importante.\
                            \nEs el adiós definitivo.")
                        time.sleep(15)
                        limpiar_pantalla()
                        break
                    elif cual_depilación=="termoquímica":
                        print("La depilación termoquímica es un tipo de depilación sin dolor y muy efectiva. Es bastante desconocida.\
                                \nConsiste en aplicar un elemento químico que hace reacción al calor, destruyendo la raíz del vello.")
                        time.sleep(6)
                        limpiar_pantalla()
                        break
                    else:
                        print("Debes elegir una de las opciones anteriores")
                        continue
                else:
                    print("Debes elegir si o no")
                    continue
            continue   
        elif practicas_comunes=="nutrición y ejercicio":
            print("Una parte esencial del cuidado corporal es mantener una dieta equilibrada y hacer ejercicio regularmente.\
            \nEsto no solo beneficia a tu piel, sino a tu salud en general.\nEl consumo de alimentos y bebidas saludables,\
junto con el ejercicio físico regular, podría ayudarle a lograr y mantener un peso que sea adecuado para usted. Mantener ese peso,\
 dormir bien y controlar \nel estrés también podrían ayudarle a evitar algunos problemas de salud.")
            time.sleep(20)
            limpiar_pantalla()
            continue
        elif practicas_comunes=="descanso adecuado":
            print("El sueño adecuado es esencial para el cuidado corporal. Un buen descanso permite que la piel se repare y regenere.\
            \nLas horas que debemos dedicar a este descanso varían en función de la edad.\
            \nSegún las recomendaciones de la Fundación Nacional del Sueño de EEUU, los adultos deberían dedicar a dormir entre siete y nueve horas diarias.\
            \nAdemás de elegir un colchón, una almohada y un pijama que resulte cómodo para el descanso, para poder descansar se recomienda seguir un horario\
de sueño y, siempre que sea posible, mantenerlo también los fines de semana.")
            time.sleep(24)
            limpiar_pantalla()
            continue
        else: 
            print("Debes elegir una de las opciones anteriores")
            continue
        break
       

def cuidado_cabello_info():
    while True:
        tipos_hair:["rizado","ondulado","lacio"]
        tipo_cabello=str(input("¿Qué tipo de cabello tienes?",tipos_hair)).lower()
        if tipo_cabello=="rizado":
            print("es un tipo de cabello que tiene una forma naturalmente ondulada o rizada en lugar de ser liso y recto.\
            \nEste tipo de cabello es muy común en personas de ascendencia africana, afroamericana, mediterránea y de algunas otras regiones.\
            \nLa textura del cabello rizado puede variar desde fina hasta gruesa. A menudo el cabello rizado puede parecer más\
 grueso y voluminoso debido a la forma en que se enrollan los rizos.")
            while True:
                mantenimiento=str(input("¿Quiéres saber su cuidado y mantenimiento?\nRespuesta si o no: ")).lower()
                if mantenimiento==no:
                    esta_bien()
                    time.sleep(2)
                    limpiar_pantalla()
                    break
                elif mantenimiento==si:
                    print("El cuidado adecuado del cabello rizado implica hidratación regular y el uso de productos diseñados\
 específicamente para cabello rizado, como acondicionadores sin sulfatos y productos para definir rizos.\
                    \nEvitar el uso excesivo de calor y productos químicos agresivos es esencial para mantener la salud del cabello rizado.")
                else:
                    print("Debes elegir si o no")
                    continue
            while True:
                estilismo_rizado=str(input("¿Quiéres saber sobre el peinado y estilismo?\nRespuesta si o no: ")).lower()
                if estilismo_rizado==no:
                    esta_bien()
                    time.sleep(2)
                    limpiar_pantalla()
                    break
                elif estilismo_rizado==si:
                    print("Para mantener la forma y la definición de los rizos,\
 es común utilizar técnicas como el 'plopping' o el 'scrunching' después de lavar el cabello.\nMuchas personas\
 con cabello rizado optan por dejarlo al natural, mientras que otras pueden alisarlo ocasionalmente con herramientas de calor.\
 \nHay una amplia variedad de peinados que pueden lograrse con cabello rizado, desde rizos sueltos hasta peinados recogidos elegantes.")
                else:
                    print("Debes elegir si o no")
                    continue
                break
            



def main():
    print("Hola me llamo Belleza de Gangnam, es un placer conocerte.\n¿Con quién tengo el placer? ")
    nombre=(input("\n"))
    di_hola(nombre)
    time.sleep (2)
    limpiar_pantalla()

    print(f"Espero que te podamos ayudar en algo {nombre}")
    time.sleep(5)
    limpiar_pantalla()

    print("Calculando la cantidad recomendada que debes de ingerir de agua al día...")
    weight=float(input("Ingresa tu peso en kg: "))
    water_intake(weight)
    time.sleep(6)
    limpiar_pantalla()


    #Enlistado de las opciones de los temas que maneja el programa: si o no 
    print("Pero antes de pasar a la información\
        \n¿Te gustaría una breve definición de skincare y de cuidado del cabello?")
    while True:
        pregunta=input("si o no: ").lower()
        respuesta(pregunta) 
        time.sleep(3)
        limpiar_pantalla()

        #Definición skincare
        if pregunta== no: 
            print("Esta bien, pasemos a lo siguiente")
            break
        elif pregunta==si:
            skincare_definición ()
            time.sleep(12)
            limpiar_pantalla()
            break
        else:
            print("Debes contestar con si o no")
            continue
        

    while True:        
            show_error="show error"   
            if show_error:
                print("Debes contestar con las opciones anteriores")
                show_error= False
            lista=input("¿De qué tema quieres saber?\n-skincare\n-cuidados del cabello\n").lower()
            print("De acuerdo")
            time.sleep(3)
            limpiar_pantalla()

            while True: 
                if lista== skincare:
                    menu_principal=menu_principal
                    show_error==False
                    #Preguntar si quiere saber sobre a=cara o b=cuerpo
                      
                    if show_error:
                        print("Debes de contestar con las opciones anteriores")
                    print("¿De qué tema quieres saber?\n-cara\n-cuerpo\nSi quieres regresar a menu principal pon 'menu principal'")
                    print("Si quieres salir del cóidigo pon 'salir'")
                    lista2=input("Respuesta: ").lower()
                    time.sleep(4)
                    limpiar_pantalla()
                    
                    if lista2=="salir":
                        exit()

                    elif lista2 == cara:
                        #Lista de la c=acné,d=rosácea,e)hidratación,f=exfoliación,g=rejuvecimiento
                            while True:
                                trata=input("\n¿Quiéres saber sobre?\
                                \nacné\nrosácea\nhidratación\nexfoliación\nrejuvecimiento\
                                \nSi quieres regresar al menu anterior ingresa sub menu \
                                \nSi quieres salir del código pon 'salir'\
                                \n¿Cuál es tu elección?\
                                \n").lower()
                                time.sleep(4)
                                limpiar_pantalla()
                                #Definición acné
                                if trata == "submenu":
                                    break
                                elif trata=="salir":
                                    exit()
                                elif trata==acne:
                                    completo_acne()
                                    show_error=False
                                    continue 

                                elif trata==rosacea:
                                    trata_rosacea()
                                    show_error=False
                                    continue

                                #hidratación
                                elif trata==hidratacion:
                                    trata_hidratación()
                                    limpiar_pantalla()
                                    show_error=False   
                                    continue                    

                                elif trata==exfoliacion:
                                    exfoliación_info()
                                    show_error=False
                                    continue
                                elif trata==rejuvecimiento:
                                    trata_rejuvecimiento()
                                    show_error=False
                                    continue

                                else:
                                    show_error=True
                                    break
                                
                            
                    elif lista2==cuerpo:
                        pregunta=input("Si quieres regresar al sub menu pon 'sub menu'. Si quieres seguir pon 'no'\
                                        \nRespuesta: ").lower()
                        time.sleep(1)
                        limpiar_pantalla()
                        if pregunta=="submenu":
                            break
                        else:
                            cuerpo_info()
                            show_error=False
                            break

                    elif lista2==menu_principal:
                        break

                    else:
                        show_error=True
                        break  
                    
                elif lista==cuidado_cabello:
                    show_error==False
                    pass 
                    break
                else:
                    show_error==True
                    break
                
        
main()





#print bibliografías:
# \nhttps://nudaest.com/blogs/blog/skin-care-que-es-y-sus-rutinas#uno\
# \nhttps://www.elsevier.es/es-revista-offarm-4-articulo-el-acne-su-tratamiento-13018369\
# \nhttps://www.mayoclinic.org/es/diseases-conditions/rosacea/symptoms-causes/syc-20353815
#\nhttps://www.clara.es/belleza/cara/cremas-hidratantes-ligeras-a-base-agua_25177 
#https://www.cosmopolitan.com/es/belleza/tratamientos-cara-cuerpo/g40563936/serums-hidratantes-piel/
#https://www.cosmopolitan.com/es/belleza/tratamientos-cara-cuerpo/g37616098/cremas-faciales-noche/
#https://www.garnier.es/consejos-belleza/cuidado-piel/acne-puntos-negros/exfoliar-cara-granos 
#https://www.vogue.es/belleza/articulos/como-exfoliar-piel-segun-tipo
#https://inoutbarcelona.com/peeling-facial-con-acido-lactico-beneficios/#:~:text=El%20%C3%A1cido%20l%C3%A1ctico%20es%20una,epidermis%20de%20forma%20poco%20abrasiva.
#https://blog.primor.eu/exfoliantes-para-piel-sensible/ 
#https://doblementesaludable.com/c-mejorar-la-salud/higiene-personal/
#https://escuelaorigen.com/que-es-la-exfoliacion-corporal-y-que-beneficios-tiene/
#https://mejorconsalud.as.com/como-cuidar-correctamente-tus-pies/
#https://www.materialestetica.com/blog/es/tipos-depilacion/
#https://www.niddk.nih.gov/health-information/informacion-de-la-salud/control-de-peso/alimentacion-saludable-actividad-fisica-vida
#https://www.institutotomaspascualsanz.com/importancia-de-un-descanso-adecuado-para-la-salud/



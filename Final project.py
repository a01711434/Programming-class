	
	import  time
	import  os
	import  random
	numero=random.randint(1,100)

	#S=skincare, CC=cuidado del cabello
	skincare="skincare"
	cuidado_cabello="cuidado del cabello"
	#A=si y B=NO
	si="si"
	no="no"
	#a=cara, b=cuerpo,
	lista2=["cara","cuerpo"]
	cara  ="cara"
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
	mixta=  "mixta"
	grasa="grasa"
	seca="seca"

	  

	def  buena_eleccion():
		while  True:
			eleccion  = ("¿Fue una buena elección? (si/no): ").lower()
			if  eleccion  ==  "si":
				break
			elif  eleccion  ==  "no":
				return

	#muy bien
	def  esta_bien():
		return("Esta bien")
		

	#Limpiar pantalla
	def  limpiar_pantalla():
		if  os.name  ==  "posix":
			os.system("clear")
		else:
			os.system("cls")

	  

	#Introducción al programa, pedir nombre y edad
	#Intro problema
	def  di_hola(nombre):
		print("\nHola",nombre,"es un placer estar contigo.")
		

	#Water Intake
	def  water_intake(weight):
		water_intake=weight*30
		print(f"Para tener una piel saludable, se recomienda consumir aproximadamente {water_intake} ml de agua")

	  

	def  respuesta(pregunta):
		print(pregunta,"\nMuy bien")
		

	#Definición skincare y cuidado del cabello
		def  skincare_definición ():
			print("Skincare:\
			\nEs el cuidado que le damos a nuestra piel para mantenerla saludable.\
			\nSe asocia con las rutinas que seguimos y los productos que usamos.\
			\nPara que la piel de nuestro rostro o cuerpo luzca fresca y sana.\
			\n\nCuido del Cabello:\
			\nEl cuidado del cabello son cuidados que se aplican al cabello.\
			\nSu finalidad es mantener la salud y buena apariencia del mismo.")
			

	#Buena elección
	def  buena_eleccion():
		print("Buena elección")
		

	#Definición Acné
	def  acné_definición():
		print("El acné es una afección frecuente de la piel (cutánea) que ocurre cuando los folículos pilosos debajo de esta se obstruyen.\
		\nLa grasa y las células muertas de la piel tapan los poros\
		y puede haber brotes de lesiones (a menudo llamados granos o espinillas).\
		\nPara la mayoría de las personas, el acné tiende a desaparecer al llegar a los 30 años,\
		pero algunas otras continúan teniendo este problema de la piel aun cuando llegan a los 40 o 50 años.")
		time.sleep(18)


	#Tratamiento acne promedio
	def  tratamiento_acné_promedio():
		print("Un tratamiento promedio dura 21 días y tiene un promedio de 7 días de mejora.")
		time.sleep(6)


	#Total de días de un tratamiento de acne:
	def  acne_duracion_tratamiento():
		tratamiento_dias=  21
		mejora_dias=7
		total_dia  =  tratamiento_dias  +  mejora_dias
		print(f"Si sigues un tratamiento para el acné, te tomará aproximadamente {total_dia} días para ver mejoras en tu piel.")
		time.sleep(6)
		

	#Tratamientos acné:
	def  tratamientos_acne():
		print("Aquí están los siguientes tratamientos:\
		\nLos objetivos que se persiguen en el tratamiento de esta enfermedad son:\
		\n\tRegular la seborrea.\
		\n\tEvitar la obstrucción del folículo.\
		\n\tDisminuir la población bacteriana.\
		\n\tEvitar las cicatrices.")
		time.sleep(5)
		limpiar_pantalla()
		

	#Información completa para imprimir del acné y los tratamientos
	def  completo_acne():
		acné_definición()
		limpiar_pantalla()
		tratamiento_acné_promedio()
		limpiar_pantalla()
		acne_duracion_tratamiento()
		limpiar_pantalla()
		pregunta1=str(input("¿Qiéres saber sobre algún tratamiento?\nSi o no: ")).lower
		if  pregunta1==si:
			tratamientos_acne()
			limpiar_pantalla()

		  

	#definicion rosácea
	def  definicion_rosacea():
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
	def  tratamiento_rosacea():
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
	def  antecedentes_rosacea(lista3):
		lista3=("-Eres mujer","-Tienes una piel que se quema facilmente con el sol",
		"-Tienes más de 30 años","-Fumas","-Tienes antecedentes familiares de rosácea")
		print("Cualquier persona puede desarrollar rosácea.\
		Pero es más probable que la tengas si: ")
		antecedentes_rosacea(lista3)
		time.sleep(7)
		limpiar_pantalla()


	def  trata_rosacea():
	#definicion rosacea
	definicion_rosacea()
		while  True:
			pregunta2=str(input("¿Quiéres saber de algún tratamiento?\
			\n si o no\
			\n ")).lower()
			buena_eleccion()
			time.sleep(3)
			limpiar_pantalla()

			if  pregunta2  ==  no:
				esta_bien()
				break
			elif  pregunta2==si:
				tratamiento_rosacea()
			else:
				print("Tienes que responder con si o no")
				input("Respuesta: ")
				break
		while  True:
			pregunta3=str(input("¿Quiéres saber los factores de riesgo?\
			\n si o no\
			\n ")).lower()
			time.sleep(3)
			limpiar_pantalla()
			if  pregunta3==no:
				esta_bien()
				break
			elif  pregunta3  ==  si:
			#antecedenstes rosacea o factores de riesgo
				antecedentes_rosacea()
			else:
				print ("Tienes que responder con si o no")
				input("Respuesta: ")
				break

	#hidratación

	def  hidratacion_cara():
		print("Una piel hidratada es una piel feliz.\
		\nLa importancia de la hidratación facial es clave para conseguir una complexión sana y\
		luminosa.\nUna piel hidratada pareca más joven. Los humectantes ayudan a mantener la humedad de la piel y\
		la hidratación le añade agua.\nLa piel deshidratada puede estar seca y grasa a la vez. La piel seca\
		se caracteriza por tener una producción baja de grasa, mientrás que la pied deshidratada simplemente\
		le falta agua.\nCuando tu piel está deshidrata, puede estar más apagada, sin brillo, tirante y con tendencia\
		a inflamarse, congestionarse y a tener erupciones.")
		

	#Metodos de hidratación

	def  metodos_hidratacion():
		lista4=print("1.Utiliza productos con base de agua\n2.Añade serums a tu rutina\n3.Utiliza una crema de noche")
		time.sleep(4)
		limpiar_pantalla()

	#Metodo hidratacion base agua cara
	def  hidratacion_base_agua_cara():
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
	def  hidratacion_serum_cara():
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
	def  crema_noche_cara():
		print("Estas cremas reparan, hidratan y protegen la piel por la noche\
		\nUriage 'Age Lift'\nRoC 'Retinol Correxion'\nCocunat 'The Absolute'\nGarnier 'Aloe Hialurónico'\
		\nOlay Retinol 24\nNivea 'Cellular Luminous'")
		time.sleep(10)
		limpiar_pantalla()


	def  pregunta7():
		pregunta7=input("¿Quiéres saber de algun tratamiento en el mercado para tu tipo de piel?\nSi o no:").lower()
		return  (pregunta7)


	def  sabermás():
		print("¿Quiéres conocer sobre tres productos con este tratamiento? ")


	#Secreto de la hidratación:
	def  secreto():
		while  True:
			secreto1=str(input("Tenemos un ingrediente secreto de la exfoliación, para poder saberlo tendrás que adivinar un numero random\
	del 1 al 100.\n¿Estás dispuesto?\nsi o no: "))
		if  secreto1.lower()==  no:
			print("¡Hasta luego!")
			break  #Sale del juego si el usuario dice que no
		if  secreto1.lower() ==  si:
			numero=random.randint(1,100)
		intento=0
		conteo=0
		while  True:
			intento=int(input("En que número estoy pensando\n"))
			conteo  +=  1
			if  intento  >  numero:
				print("El número que estoy pensando es menor")
			elif  intento  <  numero:
				print("El numero que estoy pensando es mayor")
			else:
				print("Felicidades, adivinaste el número")
				time.sleep(1)
	
			if  1<=  conteo  <=7:
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


	def  trata_hidratación():
		hidratacion_cara()
		time.sleep(25)
		limpiar_pantalla()
		while  True:
			pregunta4=str(input("¿Te gustaría saber un método de hidratación?\nSi o no: "))
			buena_eleccion()
			limpiar_pantalla()
			if  pregunta4==  no:
				esta_bien()
			break
			elif  pregunta4==si:
				metodos_hidratacion()
				buena_eleccion()
				while  True:
					curious=str(input("¿Te gustaría saber más a detalle de cada uno?\nSi o no: "))
					if  curious==  no:
						esta_bien()
					break
					elif  curious==si:
					while  True:
						curious2=str(input("¿De cuál te gustaría saber más a detalle?\
						\n1.Productos base de agua\n2.Serums\n3.Crema de noche\nRespuesta: ")).lower()
						time.sleep(4)
						limpiar_pantalla()
						if  curious2==productos_cara_base_agua:
						#hidratación base agua cara*()
							hidratacion_base_agua_cara()
					
						elif  curious2==serums_cara1:
						#hidratacion serum cara
							hidratacion_serum_cara()
						elif  curious2==crema_noche_cara1:
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

	  
	def  exfoliación_info():
		while  True:
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
			buena_eleccion()
			if  pregunta5==no:
				print({esta_bien()},". Adiós")
				break
			elif  pregunta5==  si:
				print("Como en todos los pasos de una rutina de cuidado facial, a la hora\
				de exfoliar la cara es importante elegir un producto que se adapte\
				a las necesidades de tu piel.\nEs por eso que: ")	
				while  True:
					pregunta6=str(input("¿Qué tipo de piel tienes?:\nGrasa\nMixta\nSeca\nSensible\n")).lower()
					print(pregunta6)
					time.sleep(8)
					limpiar_pantalla()
					if  pregunta6==sensible:
						print("Un exceso de producto puede provocar picor, quemazón, aumentar el enrojecimiento o los brotes de acné\
						y en algunos casos puede producir hasta manchas. Se recomienda exfoliar la piel solo una vez o como máximo dos veces por\
						semana.\nUna sustancia que es muy utilizada por su propiedad para exfoliar y ablandar las capas más superficiales \
						es el ácido láctico, una sustancia derivada de la proteína de leche vegetal.\
						\nEl uso de este es mediante un peeling facial de ácido láctico que se aplica directamente dobre la piel. ")
						pregunta7()
						if  pregunta7==si:
							time.sleep(12)
							limpiar_pantalla()
							print("Algunos enfoliantes en el mercado son:\nExfoliante Fisiológico Ultra Fino de la Roche Posay\
							\nManuka Tree Pasta Exfoliante de Ziaja\nRose Sugar Scrub Exfoliante Facial de Lancôme\
							\nExfoliante Suave Purificante de Avene\nNumee Sérum Exfoliante Ácido Láctico")
							time.sleep(8)
							limpiar_pantalla()
						elif  pregunta6==grasa:
							print("Cuando tienes piel grasa, las células muertas tienden a permanecer más tiempo. Por ello\
							la exfoliación es clave.")
							pregunta7()
							if  pregunta7==si:
								print(" Se roecomienda someterse a un peeling de ácido salicílico, un betahidroxiácido\
								capaz de eliminar la grasa que obstruye los poros. Es un tipo de exfoliación muy segura para todo\
								tipo de pieles y sin efectos secundarios. También ayuda a reducir eficazmente las espinillas\
								sin dejar imperfecciones o cicatrices importantes. Sin embargo, estos peeling no deben practicarse en casa\
								\nDebe realizarlos en una clínica un médico especializado.")
								time.sleep(13)
								limpiar_pantalla()
							elif  pregunta6==seca:
								print("Las pieles más secas se pueden exfoliar cada 15 días. Es importante que entiendas que no\
								por exfoliar con frecuencia tu piel vas a conseguir una apariencia más sana y suave.")
								time.sleep(10)
								limpiar_pantalla()
								pregunta7()
								if  pregunta7==si:
									print("El ácido glicólico, generalmente se usa en piel seca por su capacidad de exfoliar\
									las células muertas y mejorar la hidratación de la piel. Lo ideal es usarlo en productos que puedan\
									dejarse en la piel por tiempo prolongado, esto permite ir eliminando los enlaces que\
									mantienen unidas las células muertas en la piel.")
								elif  pregunta6==mixta:
									print("Los exfoliantes para las pieles secas eliminan impurezas y además purifica la piel\
									eliminando la aparicion de cebo y dejando la piel mate. ")
									pregunta7()
									if  pregunta7==si:
										print("Los exfoliantes beta-hidroxiácidos (BHA) son un tipo de ácidos óleo-solubles,\
										lo que les permite penetrar en los folículos de la piel y eliminar la suciedad y el sebo acumulado en los poros")
								else:
									print("Debes contestar con alguna de las opciones")
									continue
				else:
					print("Responder con si o no")
					continue
				break

	  

	def  main():
		print("Hola me llamo Belleza de Gangnam, es un placer conocerte.\n¿Con quién tengo el placer? ")
		nombre=(input("\n"))
		di_hola(nombre)
		time.sleep (2)
		limpiar_pantalla()

	  
		print("Espero que te podamos ayudar en algo,{nombre}.")
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
		while  True:
			pregunta=input("si o no: ").lower()
			respuesta(pregunta)
			time.sleep(3)
			limpiar_pantalla()
		
			#Definición skincare
			if  pregunta==  no:
				print("Esta bien, pasemos a lo siguiente")
				break
			elif  pregunta==si:
				skincare_definición ()
				time.sleep(12)
				limpiar_pantalla()
			else:
				print("Debes contestar con si o no")
				continue
			break

		while  True:
			menu_principal  =  "main menu"
			if  menu_principal  ==  "main menu":
				lista=input("¿De qué tema quieres saber?\n-skincare\n-cuidados del cabello\n").lower()
				print("De acuerdo")
				time.sleep(3)
				limpiar_pantalla()
				

			while  True:
				if  lista==  skincare:
				#Preguntar si quiere saber sobre a=cara o b=cuerpo
					while  True:
					lista2=input("¿De qué tema quieres saber?\n-cara\n-cuerpo\
					\nSi quieres regresar al menu principal ingresa: main menu\nRespuesta: ").lower()
					buena_eleccion()
					time.sleep(4)
					limpiar_pantalla()
					
						if  lista2  ==  cara:
						#Lista de la c=acné,d=rosácea,e)hidratación,f=exfoliación,g=rejuvecimiento
							while  True:
							trata=input("\n¿Quiéres saber sobre?\
							\nacné\nrosácea\nhidratación\nexfoliación\nrejuvecimiento\
							\nSi quieres regresar al menu principal ingresa main menu\
							\n¿Cuál es tu elección?\
							\n").lower()
							buena_eleccion()
							time.sleep(4)
							limpiar_pantalla()
							break
							if trata==menu_principal:
								return
							#Definición acné
							if  trata==acne:
								completo_acne()
								break
							elif  trata==rosacea:
								trata_rosacea()
								break
							#hidratación
							elif  trata==hidratacion:
								trata_hidratación()
								break 
								limpiar_pantalla()
							elif  trata==exfoliacion:
								exfoliación_info()
							else:
								print("Debes de contestar con alguna de las opciones anteriores")
								continue
							break
					elif  lista2==cuerpo:
						pass
					elif lista2==menu_principal:
						break	
					else:
						print("Debes de contestar con alguna de las opciones anteriores")
						continue
					break	
		elif lista==cuidado_cabello:
			pass
		else:
			print("Debes de contestar con las opciones anteriores")
			continue
		break
	

	pass

 
	
	#print("bibliografías\
	 # \nhttps://nudaest.com/blogs/blog/skin-care-que-es-y-sus-rutinas#uno\
	  # \nhttps://www.elsevier.es/es-revista-offarm-4-articulo-el-acne-su-tratamiento-13018369\ 
	  # \nhttps://www.mayoclinic.org/es/diseases-conditions/rosacea/symptoms-causes/syc-20353815
	   #\nhttps://www.clara.es/belleza/cara/cremas-hidratantes-ligeras-a-base-agua_25177 #https://www.cosmopolitan.com/es/belleza/tratamientos-cara-cuerpo/g40563936/serums-hidratantes-piel/ #https://www.cosmopolitan.com/es/belleza/tratamientos-cara-cuerpo/g37616098/cremas-faciales-noche/


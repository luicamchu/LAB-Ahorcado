

#added ejercicio 3 apartado a
def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
    f.close()
    return res
    
    
import random

#added ejercicio 3 apartado b
def elegir_palabra(palabras):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.
    '''
    #pass
    #with open(palabras, mode="r", encoding="utf-8") as f1:
    #    contenido = f1.read()
    #    print(contenido)
    
    seleccionada:str = random.choice(palabras)
    print(seleccionada)
    return seleccionada
    
#added ejercicio 3 apartado c
def enmascarar_palabra(palabra, letras_probadas:str):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    #pass
    empty_list = []
    #i:int = len(palabra)         
    for c in palabra:
        if c in letras_probadas:
            empty_list.append(c)
        else:
            empty_list.append("_")
        #print(c)
    return ' '.join(empty_list)

#added ejercicio 3 apartado d
def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
    #pass
    letra:str = input("Introduzca una letra: ").lower()
    if letra in letras_probadas:
        letra:str = input("Introduzca otra letra diferente: ").lower()
    
    return letra

#added ejercicio 3 apartado e
def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    #pass
    flag = False
    #for l in palabra_secreta:
    if letra in  palabra_secreta:
        flag = True
        print("La letra ya estaba en la palabra secreta!.")
    else:
        flag = False
    return flag

#added ejercicio 3 apartado f
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    '''
    #pass
    '''conjunto = {}
    for l in palabra_secreta:
        #conjunto.add(l)
        print("")
    if conjunto.issubset(letras_probadas):
        return True
    else:
        return False'''
    
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False
        else:
            return True
    
#added ejercicio 3 apartado g
def ejecutar_turno(palabra_secreta, letras_probadas):
    '''
    Ejecutar un turno de juego:
    - Mostrar la palabra enmascarada
    - Pedir la nueva letra
    - Comprobar si la letra está en la palabra (acierto) o no (fallo)
    - Añadir la letra al conjunto de letras probadas
    - Devolver True si la letra fue un acierto, False si fue un fallo
    Ayuda:
    - Recuerda las funciones que ya has implementado para mostrar la palabra, pedir la letra y comprobarla
    '''
    #pass
    #enmascarar_palabra(palabra_secreta, letras_probadas)
    resultado = enmascarar_palabra(palabra_secreta, letras_probadas)
    print(f"Palabra enmascarada: {resultado}")

    #pedir_letra(letras_probadas)
    letra = pedir_letra(letras_probadas)
    print(f"Letra introducida: {letra}")

    #comprobar_letra(palabra_secreta, letras_probadas)
    resultado = comprobar_palabra_completa(palabra_secreta, letras_probadas)
    
    if (resultado):
        print("¡Bien hecho! Esa letra está en la palabra.")
        return True
    else:
        return False



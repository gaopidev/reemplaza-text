import sys
import re

'''
Script para reemplazar PALABRAS en archivos de texto
'''

if __name__ == "__main__":
    # Palaba que vas a reemplazar
    old_word = "html"
    # Palabra por la cual reemplazaras
    new_word = "python"
    # Archivo de entrada
    inp_file = open("demofile.txt", "r")
    # Archivo de salida
    new_file = open("new_demofile.txt", "w")
    
    # Obtenemos cada linea del archivo
    new_text=""
    for line in inp_file:
        # Se guarda una nueva linea reemplazando, mediante regex, las palabras indicadas ignorando el uso de mayusculas y minusculas
        # Regex:    r = raw string
        #           f = f-string permite insertar valores de variables dentro de {} (remplaza string.format())
        #           \b omite los caracteres no alfanumericos
        new_text += re.sub(rf"\b{old_word}\b", new_word, line, flags=re.IGNORECASE)
    new_file.write(new_text)
    new_file.close()
    inp_file.close()

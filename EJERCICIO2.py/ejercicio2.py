def main():
    texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    # Paso 1: Dividir el texto en frases
    frases = texto_original.split("#")

    # Paso 2 y 3: Capitalizar y añadir puntuación
    frases_formateadas = [frase.capitalize() + "." for frase in frases]

    # Añadir '...' al final de la primera frase para simular una pausa
    frases_formateadas[0] = frases_formateadas[0].replace(".", "...")

    # Paso 4: Unir las frases con saltos de línea
    dialogo_formateado = "\n\n".join(frases_formateadas)

    print(dialogo_formateado)

if __name__ == "__main__":
    main()
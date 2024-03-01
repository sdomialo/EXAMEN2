#Ejercicio 3: La Magia de las Listas Numéricas
#Crea una función llamada magia_numerica() que realice varias transformaciones en una lista de números sin modificar la lista original. Las tareas son las siguientes:
#Eliminar los elementos duplicados.
#Ordenar la lista de mayor a menor.
#Eliminar todos los números impares.
#Sumar todos los números que quedan.
#Colocar esta suma como el primer elemento de la lista.
class ListaMagica:
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros

    def eliminar_duplicados(self):
        self.lista_numeros = list(set(self.lista_numeros))

    def ordenar_de_mayor_a_menor(self):
        self.lista_numeros.sort(reverse=True)

    def eliminar_impares(self):
        self.lista_numeros = [num for num in self.lista_numeros if num % 2 == 0]

    def sumar_numeros(self):
        suma_total = sum(self.lista_numeros)
        self.lista_numeros.insert(0, suma_total)

    def verificar_suma(self):
        suma_primero = self.lista_numeros[0]
        suma_resto = sum(self.lista_numeros[1:])
        return suma_primero == suma_resto

    def magia_numerica(self):
        self.eliminar_duplicados()
        self.ordenar_de_mayor_a_menor()
        self.eliminar_impares()
        self.sumar_numeros()
        return self.lista_numeros, self.verificar_suma()


if __name__ == "__main__":
    lista_original = [4, 2, 40, 12, 56, 6, 8, 3, 56, 7]
    lista_magica = ListaMagica(lista_original)
    resultado, verificacion = lista_magica.magia_numerica()

    print(f"Lista original: {lista_original}")
    print(f"Resultado después de la magia: {resultado}")
    print(f"Verificación: {verificacion}")

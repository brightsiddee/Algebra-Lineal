#Programa Para Crear una matriz, Asignando los valores
#3er Semestre Grupo 4
#Álgebra Lineal


def Autores():
    #Datos de los Autores
    print("Melchor De La Cruz Luis Erick") 
    print("Rossi Aureli Montiel Hernandez")
    print("Edwin Yael Hernandez")
    print("Diana Ivett Cruz Garcia")

class Matriz:
    def __init__(self, numfil, numcol):
        self.filas = numfil
        self.columnas = numcol
        self.matriz = []

    def ingresarValores(self):
        for i in range(self.filas):
            self.matriz.append([])
            for j in range(self.columnas):
                ingnum = int(input(f"Ingrese valor para: {i + 1}, {j + 1}: "))
                self.matriz[i].append(ingnum)

    def showMatriz(self):
        print("La Matriz es: ")
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.matriz[i][j], end = ' ')
            print()    
    
    def determinante(self):
        deter = 1
        for x in range(self.filas):
            deter= self.matriz[x][x]*deter
        print('\nEl determinante de la matriz es = ', deter)
    

numfil = int(input("Ingrese numero filas: "))
numcol = int(input("Ingrese numero columnas: "))
matriz = Matriz(numfil, numcol)
 
# Impresión  
Autores()
matriz.ingresarValores()
matriz.showMatriz()
matriz.determinante()

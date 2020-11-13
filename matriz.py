#Programa Para Crear una matriz, Asignando los valores



def Autor():
    #Escribir Aqui Sus Nombres
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
    
    

numfil = int(input("Ingrese numero filas: "))
numcol = int(input("Ingrese numero columnas: "))
matriz = Matriz(numfil, numcol)
 
# Impresión  
Autor()
matriz.ingresarValores()
matriz.showMatriz()
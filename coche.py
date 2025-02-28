class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustible = 100  

    def conducir(self, km):
       
        combustible_consumido = km / 10
        
        
        if combustible_consumido > self.combustible:
            print(f"\n{self.marca} {self.modelo}: No hay suficiente combustible para recorrer {km} km.")
            print(f"Solo puedes recorrer {self.combustible * 10} km con el combustible actual.")
            self.combustible = 0  
        else:
            self.combustible -= combustible_consumido
            print(f"\n{self.marca} {self.modelo}: Has recorrido {km} km. Combustible restante: {self.combustible:.2f} litros.")

    def repostar(self, litros):
        
        if self.combustible + litros > 100:
            self.combustible = 100
            print(f"\n{self.marca} {self.modelo}: El depósito está lleno (100 litros).")
        else:
            self.combustible += litros
            print(f"\n{self.marca} {self.modelo}: Has repostado {litros} litros. Combustible actual: {self.combustible:.2f} litros.")

    def estado(self):
        
        print(f"\n{self.marca} {self.modelo}: Combustible restante: {self.combustible:.2f} litros.")


def mostrar_menu():
    print("\n Menú del Coche ")
    print("1. Conducir")
    print("2. Repostar combustible")
    print("3. Ver estado del coche")
    print("4. Salir")



def main():
    
    marca = input("Ingresa la marca del coche: ")
    modelo = input("Ingresa el modelo del coche: ")
    mi_coche = Coche(marca, modelo)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            km = float(input("Ingresa los kilómetros a conducir: "))
            mi_coche.conducir(km)
        elif opcion == '2':
            litros = float(input("Ingresa los litros a repostar: "))
            mi_coche.repostar(litros)
        elif opcion == '3':
            mi_coche.estado()
        elif opcion == '4':
            print(f"\nGracias por usar el coche {mi_coche.marca} {mi_coche.modelo}.")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 4.")



if __name__ == "__main__":
    main()
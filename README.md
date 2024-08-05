# juego-de-poo

   # def crearJugador(self):
   
  def creaJugador(self):
        posiblesOpciones = (self.rojo, self.azul, self.amarillo, self.verde)
        while True:
            opcion = input("Elige los colores de tu secuencia (r/b/y/g)")
            if len(self.secuencia) <= 4:
                match opcion:
                    case "r":
                        self.secuencia.append(posiblesOpciones[0])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case "b":
                        self.secuencia.append(posiblesOpciones[1])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case "y":
                        self.secuencia.append(posiblesOpciones[2])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case "g":
                        self.secuencia.append(posiblesOpciones[3])
                        print("|", "".join(self.secuencia) + self.reset, "|")
                    case _:
                        print("Introduzca una respuesta correcta.")
                        #En caso de haber alcanzado el limite de espacio.
                if len(self.secuencia) == 4:
                    confirm = input(f"¿Confirmar secuencia? (S/N): ").strip().lower()
                    if confirm == "s":
                        self.eleccionAzar()
                        break
                    else:
                        self.secuencia = []
        return self.secuencia

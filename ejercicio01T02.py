import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Primera ventana

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. Configuración de la ventana (Modificado para Parte A)
        self.setWindowTitle("Gestor de Tareas Dayneira")
        self.resize(600, 350)
        self.setMinimumSize(400, 250)

        # 2. Creación del botón con texto personalizado
        self.boton = QPushButton("Crear nueva tarea")

        # 3. Colocación del botón en el centro
        self.setCentralWidget(self.boton)


# Desarrolla tu propia ventana

class VentanaAlternativa(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración inicial y dimensiones solicitadas
        self.setWindowTitle("Visor de Mapas de Fantasía")
        self.resize(500, 300)
        self.setMinimumSize(350, 200)

        # Creación del botón central adaptado a la temática
        self.boton = QPushButton("Generar nuevo mapa")

        # Establecer el botón como widget central de la ventana principal
        self.setCentralWidget(self.boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    # ventana = VentanaAlternativa()
    
    ventana.show()

    sys.exit(app.exec())
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Primera ventana

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana (Modificado para Parte A)
        self.setWindowTitle("Gestor de Tareas Dayneira")
        self.resize(600, 350)
        self.setMinimumSize(400, 250)

        # Creación del botón con texto personalizado
        self.boton = QPushButton("Crear nueva tarea")

        # Colocación del botón en el centro
        self.setCentralWidget(self.boton)


# Ventana propia

class VentanaAlternativa(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración inicial y dimensiones solicitadas
        self.setWindowTitle("Visor de Mapas de Fantasía")
        self.resize(500, 300)
        self.setMinimumSize(350, 200)

        # Creación del botón central 
        self.boton = QPushButton("Generar nuevo mapa")
        self.setCentralWidget(self.boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = Ventana()
    # ventana = VentanaAlternativa()

    ventana.show()

    sys.exit(app.exec())
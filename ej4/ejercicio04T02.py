import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class VentanaProyecto(QMainWindow):
    def __init__(self):
        super().__init__()

        # Estado inicial por defecto 
        self.setWindowTitle("Proyecto sin nombre")
        self.resize(450, 150)
        self.setMinimumSize(300, 100)

        self.campo = QLineEdit()

        # Agregar un marcador de posición
        self.campo.setPlaceholderText("Escribe el nombre del proyecto...")
        self.campo.setMaxLength(30)

        # Conectar la señal textChanged para actualizar automáticamente
        self.campo.textChanged.connect(self.actualizar_titulo)
        self.setCentralWidget(self.campo)

    # Utilizar @Slot(str) en el método receptor
    @Slot(str)
    def actualizar_titulo(self, texto):
        # Limpiar los espacios en blanco de los extremos
        nombre_limpio = texto.strip()

        # Validar si hay contenido: Mayúsculas o texto por defecto
        if nombre_limpio:
            self.setWindowTitle(nombre_limpio.upper())
        else:
            self.setWindowTitle("Proyecto sin nombre")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaProyecto()
    ventana.show()

    sys.exit(app.exec())
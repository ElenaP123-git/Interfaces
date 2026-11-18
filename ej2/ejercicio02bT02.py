import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class VentanaPulsador(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control de Pulsación")
        self.resize(400, 200)
        self.setMinimumSize(300, 150)

        self.boton = QPushButton("Pulsar")

        # Conectar las señales pressed y released a métodos diferentes
        self.boton.pressed.connect(self.al_presionar)
        self.boton.released.connect(self.al_liberar)

        self.setCentralWidget(self.boton)

    @Slot()
    def al_presionar(self):
        # Mientras esté presionado, cambia el texto a «Soltar»
        self.boton.setText("Soltar")
        print("Botón presionado")

    @Slot()
    def al_liberar(self):
        # Cuando se libere, recupera el texto «Pulsar»
        self.boton.setText("Pulsar")
        print("Botón liberado")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaPulsador()
    ventana.show()

    sys.exit(app.exec())
import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class VentanaVigilancia(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Vigilancia: Desactivado")
        self.resize(450, 220)
        self.setMinimumSize(350, 150)

        # Botón con setCheckable(True)
        self.boton = QPushButton("Activar Sistema")
        self.boton.setCheckable(True)

        # Utilizar clicked y toggled conectándolas a sus respectivos métodos
        self.boton.clicked.connect(self.registrar_activacion_consola)
        self.boton.toggled.connect(self.actualizar_interfaz_estado)

        self.setCentralWidget(self.boton)

    # Definir métodos diferentes y utilizar @Slot(bool)
    @Slot(bool)
    def registrar_activacion_consola(self, marcado):
        # Registra las activaciones en consola cuando se hace clic
        estado_texto = "Activado" if marcado else "Desactivado"
        print("[EVENTO CLICK] El sistema ha cambiado a estado:" + estado_texto)

    @Slot(bool)
    def actualizar_interfaz_estado(self, activo):
        # Actualiza el título de la ventana y el texto del botón según su estado
        if activo:
            self.setWindowTitle("Sistema de Vigilancia: Activado")
            self.boton.setText("Desactivar Sistema")
        else:
            self.setWindowTitle("Sistema de Vigilancia: Desactivado")
            self.boton.setText("Activar Sistema")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaVigilancia()
    ventana.show()
    sys.exit(app.exec())
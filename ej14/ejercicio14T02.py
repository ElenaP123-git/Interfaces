import sys
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow


class VentanaMenuArchivo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menú Archivo — Actividad 14")
        self.resize(500, 280)
        self.setMinimumSize(360, 200)

        self.contador_titulos = 1

        self.accion_mostrar_mensaje = QAction("Mostrar mensaje", self)
        self.accion_mostrar_mensaje.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_mostrar_mensaje.triggered.connect(self.mostrar_mensaje)

        self.accion_cambiar_titulo = QAction("Cambiar título", self)
        self.accion_cambiar_titulo.setShortcut(QKeySequence("Ctrl+L"))
        self.accion_cambiar_titulo.triggered.connect(self.cambiar_titulo)

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut(QKeySequence("Ctrl+Q"))
        self.accion_salir.triggered.connect(self.close)

        menu_archivo = self.menuBar().addMenu("&Archivo")
        menu_archivo.addAction(self.accion_mostrar_mensaje)
        menu_archivo.addAction(self.accion_cambiar_titulo)

        menu_archivo.addSeparator()
        menu_archivo.addAction(self.accion_salir)

    @Slot()
    def mostrar_mensaje(self):
        print("Hola desde el menú")

    @Slot()
    def cambiar_titulo(self):
        nuevo_titulo = "Título actualizado #" + str(self.contador_titulos)
        self.setWindowTitle(nuevo_titulo)
        print("Título cambiado a: " + nuevo_titulo)
        self.contador_titulos = self.contador_titulos + 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaMenuArchivo()
    ventana.show()

    sys.exit(app.exec())
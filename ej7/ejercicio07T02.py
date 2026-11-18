import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow


class VentanaSelectorTecnologia(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selector de tecnología")
        self.resize(450, 200)
        self.setMinimumSize(350, 150)

        # QComboBox con al menos cinco tecnologías
        self.combo = QComboBox()
        self.combo.addItem("Python", "py")
        self.combo.addItem("Java", "java")
        self.combo.addItem("JavaScript", "js")
        self.combo.addItem("Kotlin", "kt")
        self.combo.addItem("C++", "cpp")

        # AMPLIACIÓN 
        # Convertir el desplegable en editable
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        self.combo.setMaxCount(10)
        self.combo.setDuplicatesEnabled(False)

        # Detecta los cambios mediante currentIndexChanged
        self.combo.currentIndexChanged.connect(self.actualizar_seleccion)
        self.setCentralWidget(self.combo)

    @Slot(int)
    def actualizar_seleccion(self, indice):
        if indice >= 0:
            nombre = self.combo.currentText()
            codigo = self.combo.currentData()
            self.setWindowTitle("Tecnología seleccionada: " + nombre)

            print("Índice seleccionado: " + str(indice))
            print("Tecnología: " + nombre)
            print("Identificador (Dato interno): " + str(codigo))
            print("-" * 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaSelectorTecnologia()
    ventana.show()

    sys.exit(app.exec())
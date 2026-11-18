import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox

class VentanaNotificaciones(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notificaciones desactivadas")
        self.resize(400, 200)
        self.setMinimumSize(300, 150)

        # QCheckBox como widget central
        self.casilla = QCheckBox("Activar notificaciones")

        # (Ampliación) Activar tres estados (tristate)
        self.casilla.setTristate(True)
        self.casilla.checkStateChanged.connect(self.actualizar_notificaciones)
        self.setCentralWidget(self.casilla)

    @Slot(Qt.CheckState)
    def actualizar_notificaciones(self, estado):
        # Gestionar los tres estados (Ampliación) y registrar en consola
        if estado == Qt.CheckState.Unchecked:
            self.setWindowTitle("Notificaciones desactivadas")
            print("Estado: Desmarcado (Notificaciones desactivadas)")
            
        elif estado == Qt.CheckState.PartiallyChecked:
            self.setWindowTitle("Notificaciones parciales")
            print("Estado: Parcialmente marcado (Notificaciones parciales)")
            
        elif estado == Qt.CheckState.Checked:
            self.setWindowTitle("Notificaciones activadas")
            print("Estado: Marcado (Notificaciones activadas)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaNotificaciones()
    ventana.show()

    sys.exit(app.exec())
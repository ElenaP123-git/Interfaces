import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


class VentanaEditorNotas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editor de notas — 0 caracteres (0 palabras)")
        self.resize(550, 400)
        self.setMinimumSize(400, 300)

        # QTextEdit como widget central de la ventana
        self.editor = QTextEdit()

        # «Escribe aquí tus notas» como marcador de posición
        self.editor.setPlaceholderText("Escribe aquí tus notas")

        self.editor.setAcceptRichText(False)

        # Detectar los cambios mediante la señal textChanged
        self.editor.textChanged.connect(self.actualizar_contadores)
        self.setCentralWidget(self.editor)

    # Utiliza @Slot() en el método receptor (sin argumentos)
    @Slot()
    def actualizar_contadores(self):
        texto = self.editor.toPlainText()
        num_caracteres = len(texto)
        palabras = texto.split()
        num_palabras = len(palabras)

        # Actualiza automáticamente el título de la ventana
        titulo = "Editor de notas — " + num_caracteres + " caracteres (" + num_palabras + " palabras)"
        self.setWindowTitle(titulo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = VentanaEditorNotas()
    ventana.show()

    sys.exit(app.exec())
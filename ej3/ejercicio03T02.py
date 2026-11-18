import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


# CLASE 1: Pantalla de bienvenida con texto

class VentanaBienvenida(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bienvenido a EventosFácil")
        self.resize(500, 300)
        self.setMinimumSize(350, 200)

        # QLabel como widget central
        self.etiqueta = QLabel()
        self.setCentralWidget(self.etiqueta)

        mensaje = (
            "¡Te damos la bienvenida a EventosFácil!\n"
            "Tu plataforma para la gestión y reserva de eventos."
        )
        self.etiqueta.setText(mensaje)

        fuente = self.etiqueta.font()
        fuente.setPointSize(20)
        self.etiqueta.setFont(fuente)

        # Centrar el texto horizontal y verticalmente
        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Permitir varias líneas si es necesario
        self.etiqueta.setWordWrap(True)


# CLASE 2: Pantalla de bienvenida con imagen (Ampliación)

class VentanaImagen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visor de Imagen")
        self.resize(600, 400)
        self.setMinimumSize(400, 300)

        # Crear QLabel central para la imagen
        self.etiqueta_imagen = QLabel()
        self.setCentralWidget(self.etiqueta_imagen)
        ruta_imagen = Path(__file__).resolve().parent / "recursos" / "images.jpg"

        # Cargar la imagen mediante QPixmap
        imagen = QPixmap(str(ruta_imagen))

        # Comprobar si la imagen se ha cargado correctamente
        if imagen.isNull():
            self.etiqueta_imagen.setText(
                "Error: No se pudo encontrar la imagen en 'recursos/'."
            )
            self.etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            # Ajustar tamaño
            imagen_ajustada = imagen.scaled(
                400,
                300,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

            # Mostrar la imagen ajustada y centrarla
            self.etiqueta_imagen.setPixmap(imagen_ajustada)
            self.etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)


# ==========================================
# BLOQUE PRINCIPAL (Selector de clases)
# ==========================================
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Elige qué clase deseas ejecutar descomentando una u otra:
    
    ventana = VentanaBienvenida()  # Ejecuta la versión de texto
    # ventana = VentanaImagen()     # Ejecuta la versión de imagen

    ventana.show()
    sys.exit(app.exec())
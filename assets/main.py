from gui import GUI, QApplication

# MODEL PREDICTS THE PRICE OF A FLAT 20m2 - 80m2 IN POLAND

if __name__ == "__main__":
    app = QApplication()
    window = GUI()
    window.show()
    app.exec()


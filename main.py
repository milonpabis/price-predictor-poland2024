from assets.gui import GUI, QApplication, EntryForm

# MODEL PREDICTS THE PRICE OF A FLAT 20m2 - 80m2 IN POLAND

if __name__ == "__main__":
    app = QApplication()
    window = EntryForm()
    window.show()
    app.exec()
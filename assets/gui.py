from UI.MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon
from functools import partial
import numpy as np
import joblib
from babel.numbers import format_currency

class GUI(QMainWindow, Ui_MainWindow):

    model = joblib.load("../models//rf_79k.joblib")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons = [self.bt_balcony, self.bt_garden, self.bt_garage, self.bt_lift, self.bt_terrace, self.bt_city, self.bt_ownership, self.bt_status]
        self.YES_ICON = QIcon("images/yes.png")
        self.NO_ICON = QIcon("images/no.png")

        self.bt_calculate.clicked.connect(self.predict)
        self.bt_reset.clicked.connect(self.reset)

        self.setWindowTitle("Flat Price Prediction - Poland 2024")
        self.setWindowIcon(QIcon("images/house.jpg"))
        self.lb_prediction.setText("")
        self.setup_buttons()


    def setup_buttons(self) -> None:
        
        for b in self.buttons:
            b.setIcon(QIcon("images/no.png"))
            b.setStyleSheet("border-radius: 2px;")
            b.clicked.connect(partial(self.change_icon, b))


    def change_icon(self, button: QPushButton) -> None:
        if button.isChecked():
            button.setIcon(self.YES_ICON)
        else:
            button.setIcon(self.NO_ICON)


    def create_vector(self) -> np.ndarray:
        """
        AREA OWNERSHIP ROOMS STATUS FLOOR BALCONY TERRACE GARDEN GARAGE BUILDYEAR LIFT CITY
        """
        return np.array([self.sb_area.value(),
                         self.bt_ownership.isChecked(),
                         self.sb_rooms.value(),
                         self.bt_status.isChecked() + 1,
                         self.sb_floor.value(),
                         self.bt_balcony.isChecked(),
                         self.bt_terrace.isChecked(),
                         self.bt_garden.isChecked(),
                         self.bt_garage.isChecked(), 
                         self.sb_year.value(), 
                         self.bt_lift.isChecked(), 
                         self.bt_city.isChecked()]).reshape(1, -1)
    
    def predict(self) -> None:
        """
        MAE of the model = 79k
        """
        prediction = self.model.predict(self.create_vector())[0]
        lower_bound = format_currency(prediction - 79000, "PLN", locale="pl_PL")
        upper_bound = format_currency(prediction + 79000, "PLN", locale="pl_PL")
        self.lb_prediction.setText(f"{lower_bound} - {upper_bound}")


    def reset(self) -> None:
        self.sb_area.setValue(20)
        self.sb_rooms.setValue(1)
        self.sb_floor.setValue(0)
        self.sb_year.setValue(2024)
        self.lb_prediction.setText("")

        for b in self.buttons:
            b.setIcon(self.NO_ICON)
            b.setChecked(False)




    



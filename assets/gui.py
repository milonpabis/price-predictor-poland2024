from assets.UI.MainWindow import Ui_MainWindow
from assets.UI.EntryForm import Ui_Form
from assets.UI.MainWindowKrk import Ui_MainWindow as Ui_MainWindowKrk
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PySide6.QtGui import QIcon, QPixmap, QPainter, QPen, QColor, QPolygon
from PySide6.QtCore import QPoint
from functools import partial
import numpy as np
import joblib
from babel.numbers import format_currency

from assets.static.shadows import *


class PolandPrediction(QMainWindow, Ui_MainWindow):
    """
    Main window of the application, with predictions for whole Poland,
    without specifying the exact location.
    """

    # loading the model
    model = joblib.load("models//rf_79k.joblib")

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons = [self.bt_balcony, self.bt_garden, self.bt_garage, self.bt_lift, self.bt_terrace, self.bt_city, self.bt_ownership, self.bt_status]
        
        self.YES_ICON = QIcon("assets/images/yes.png")
        self.NO_ICON = QIcon("assets/images/no.png")
        self.GB_ICON = QIcon("assets/images/goback.webp")

        # connecting buttons to functions
        self.bt_calculate.clicked.connect(self.predict)
        self.bt_reset.clicked.connect(self.reset)
        self.bt_goback.clicked.connect(self.go_back)

        # setting window properties
        self.setWindowTitle("Flat Price Prediction - Poland 2024")
        self.setWindowIcon(QIcon("assets/images/house.jpg"))

        # setting default values
        self.lb_prediction.setText("")
        self.setup_buttons()


    def setup_buttons(self) -> None:    

        def setup_style():  # adding shadows
            self.bt_calculate.setGraphicsEffect(SHADOW_CALC)
            self.bt_reset.setGraphicsEffect(SHADOW_RESET)
            self.bt_goback.setGraphicsEffect(SHADOW_GOBACK)
            
        # go back button
        self.bt_goback.setIcon(self.GB_ICON)
        self.bt_goback.setStyleSheet("border-radius: 2px;")
        
        # option buttons
        for idx, b in enumerate(self.buttons):
            b.setIcon(self.NO_ICON)
            b.setStyleSheet("border-radius: 2px;")
            b.setGraphicsEffect(SHADOWS_ICONS[idx])
            b.clicked.connect(partial(self.change_icon, b))
            
        setup_style()


    def change_icon(self, button: QPushButton) -> None:
        if button.isChecked():
            button.setIcon(self.YES_ICON)
        else:
            button.setIcon(self.NO_ICON)


    def create_vector(self) -> np.ndarray:  # creates a vector from the inputs that will be passed to the model
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
    

    def predict(self) -> None: # uses the model to generate a prediction
        """
        MAE of the model = 79k
        """
        prediction = self.model.predict(self.create_vector())[0]
        lower_bound = format_currency(prediction - 79000, "PLN", locale="pl_PL")
        upper_bound = format_currency(prediction + 79000, "PLN", locale="pl_PL")
        self.lb_prediction.setText(f"{lower_bound} - {upper_bound}")


    def reset(self) -> None:    # resets the inputs and the prediction
        self.sb_area.setValue(20)
        self.sb_rooms.setValue(1)
        self.sb_floor.setValue(0)
        self.sb_year.setValue(2024)
        self.lb_prediction.setText("")

        for b in self.buttons:
            b.setIcon(self.NO_ICON)
            b.setChecked(False)

    
    def go_back(self) -> None:  # returns to the starting window
        self.close()
        self.window = EntryForm()
        self.window.show()



class KrakowPrediction(QMainWindow, Ui_MainWindowKrk):
    """
    Main window of the application, with predictions for Krakow city only,
    user needs to specify the exact location of the building in Krakow.
    """

    model = joblib.load("models//krk_55k.joblib")
    BORDER_V = (49.9417, 50.1497)   # vertical borders of Krakow pixmap
    BORDER_H = (19.7777, 20.2423)   # horizontal borders of Krakow pixmap


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.YES_ICON = QIcon("assets/images/yes.png")
        self.NO_ICON = QIcon("assets/images/no.png")
        self.GB_ICON = QIcon("assets/images/goback.webp")
        self.pixmap = QPixmap("assets/images/krk1.JPG")



        self.latitude = 50.06143
        self.longitude = 19.93658

        self.buttons = [self.bt_balcony, self.bt_garden, self.bt_garage, self.bt_lift,
                         self.bt_terrace, self.bt_ownership, self.bt_status]


        # connecting buttons to functions
        self.bt_goback.clicked.connect(self.go_back)
        self.bt_accept.clicked.connect(self.load_location)
        self.bt_calculate.clicked.connect(self.predict)
        self.bt_reset.clicked.connect(self.reset)

        self.l_map.mousePressEvent = self.load_location_clicked


        # setting window properties
        self.setWindowTitle("Flat Price Prediction - Krakow 2024")
        self.setWindowIcon(QIcon("assets/images/house.jpg"))

        # setting default values
        self.l_map.setPixmap(self.pixmap)
        self.setup_buttons()



    def predict(self) -> None: # uses the model to generate a prediction
        """
        MAE of the model = 79k
        """
        prediction = self.model.predict(self.create_vector())[0]
        lower_bound = format_currency(prediction - 79000, "PLN", locale="pl_PL")
        upper_bound = format_currency(prediction + 79000, "PLN", locale="pl_PL")
        self.l_prediction.setText(f"{lower_bound} - {upper_bound}")


    def create_vector(self) -> np.ndarray:  # creates a vector from the inputs that will be passed to the model
        """
        AREA OWNERSHIP ROOMS STATUS FLOOR BALCONY TERRACE GARDEN GARAGE LIFT LONGITUDE LATITUDE AGE
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
                                  self.bt_lift.isChecked(),
                                   self.longitude,
                                    self.latitude,
                                     self.convert_age(self.sb_year.value())]).reshape(1, -1)
    

    def convert_age(self, year: int) -> int:  # converts the year of the building to its age
        return 2 if year > 2016 else 1 if year > 2000 else 0
    

    def load_location(self) -> None:            # loads the location of the building
        if self.le_address.text() == "Krakow, Zielonki":
            self.longitude = 19.921007 
            self.latitude = 50.118023

        

        x, y = self.latlong_to_coords(self.latitude, self.longitude,
                                       self.BORDER_V, self.BORDER_H,
                                         (self.pixmap.width(), self.pixmap.height()))
        self.draw_point_on_map(x, y)
        print(self.latitude, self.longitude)



    def load_location_clicked(self, event) -> None:  # loads the location of the building after clicking on the map
        x, y = event.pos().x(), event.pos().y()
        x = x / self.l_map.width() * self.pixmap.width()    # mapping to the Pixmap real size
        y = y / self.l_map.height() * self.pixmap.height()

        self.longitude, self.latitude = self.coords_to_latlong(x, y,
                                                                self.BORDER_V, self.BORDER_H,
                                                                  (self.pixmap.width(), self.pixmap.height()))
        self.draw_point_on_map(x, y)
        print(self.latitude, self.longitude)



    def draw_point_on_map(self, x: int, y: int) -> None:  # draws a point on the map
        painter = QPainter()
        pixmap = QPixmap("assets/images/krk1.JPG")
        painter.begin(pixmap)
        painter.setPen(QPen(QColor(255, 0, 0), 5))
        triangle_size = 10  # size of the triangle
        triangle = QPolygon([QPoint(x, y),
                              QPoint(x - triangle_size, y - triangle_size),
                               QPoint(x + triangle_size, y - triangle_size)])
        
        painter.drawPolygon(triangle)
        painter.end()
        self.l_map.setPixmap(pixmap)


    def coords_to_latlong(self, x: int, y: int, lat_edges: tuple, long_edges: tuple, coords_shape: tuple) -> tuple:  # converts the coordinates of the map to latitude and longitude
        lat_range = lat_edges[1] - lat_edges[0]
        long_range = long_edges[1] - long_edges[0]

        longitude = long_edges[0] + x/coords_shape[0] * long_range
        latitude = lat_edges[0] + (1 - y/coords_shape[1]) * lat_range
        
        return longitude, latitude
    

    def latlong_to_coords(self, latitude: float, longitude: float, lat_edges: tuple, long_edges: tuple, coords_shape: tuple) -> tuple:  # converts the latitude and longitude to the coordinates of the map
        lat_range = lat_edges[1] - lat_edges[0]
        long_range = long_edges[1] - long_edges[0]

        x_coord = (longitude-long_edges[0])/long_range * coords_shape[0]
        y_coord = (1-(latitude-lat_edges[0])/lat_range) * coords_shape[1]

        return x_coord, y_coord




    def go_back(self) -> None:
        self.close()
        self.window = EntryForm()
        self.window.show()


    def setup_buttons(self) -> None:    

        def setup_style():  # adding shadows
            self.bt_calculate.setGraphicsEffect(SHADOW_CALC1)
            self.bt_reset.setGraphicsEffect(SHADOW_RESET1)
            self.bt_goback.setGraphicsEffect(SHADOW_GOBACK1)
            self.bt_accept.setGraphicsEffect(SHADOW_ACCEPT)
            
        # go back button
        self.bt_goback.setIcon(self.GB_ICON)
        self.bt_goback.setStyleSheet("border-radius: 2px;")
        
        # option buttons
        for idx, b in enumerate(self.buttons):
            b.setIcon(self.NO_ICON)
            b.setStyleSheet("border-radius: 2px;")
            b.setGraphicsEffect(SHADOWS_ICONS[idx])
            b.clicked.connect(partial(self.change_icon, b))
            
        setup_style()


    def change_icon(self, button: QPushButton) -> None:
        if button.isChecked():
            button.setIcon(self.YES_ICON)
        else:
            button.setIcon(self.NO_ICON)


    def reset(self) -> None:    # resets the inputs and the prediction
        self.sb_area.setValue(20)
        self.sb_rooms.setValue(1)
        self.sb_floor.setValue(0)
        self.sb_year.setValue(2024)
        self.l_prediction.setText("")
        self.latitude = 50.06143
        self.longitude = 19.93658
        self.pixmap = QPixmap("assets/images/krk1.JPG")
        self.l_map.setPixmap(self.pixmap)

        for b in self.buttons:
            b.setIcon(self.NO_ICON)
            b.setChecked(False)




class EntryForm(QDialog, Ui_Form):
    """
    Starting window, asking which model user wants to use.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # connecting buttons to functions
        self.bt_poland.clicked.connect(self.poland)
        self.bt_krakow.clicked.connect(self.krakow)

        # setting window properties
        self.setWindowTitle("Flat Price Prediction 2024")
        self.setWindowIcon(QIcon("assets/images/house.jpg"))

        # setting default values
        self.setup_buttons()


    def poland(self) -> None:   # handles the user's choice - poland prediction model
        self.close()
        self.window = PolandPrediction()
        self.window.show()


    def krakow(self) -> None:   # handles the user's choice - krakow prediction model
        self.close()
        self.window = KrakowPrediction()
        self.window.show()


    def setup_buttons(self) -> None:    # adds shadows to the buttons
        self.bt_poland.setGraphicsEffect(SHADOWS_ENTRY[0])
        self.bt_krakow.setGraphicsEffect(SHADOWS_ENTRY[1])
    




    



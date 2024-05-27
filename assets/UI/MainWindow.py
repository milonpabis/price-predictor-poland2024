# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 675)
        MainWindow.setMinimumSize(QSize(600, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.head = QFrame(self.centralwidget)
        self.head.setObjectName(u"head")
        self.head.setStyleSheet(u"#head {\n"
" background-color: rgba(250, 250, 250, 180);\n"
"background-color: rgba(239, 234, 178, 180);\n"
"}")
        self.head.setFrameShape(QFrame.NoFrame)
        self.head.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.head)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.head)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.head)

        self.f1 = QFrame(self.centralwidget)
        self.f1.setObjectName(u"f1")
        self.f1.setStyleSheet(u"#f1 {\n"
" background-color: rgba(240, 240, 240, 180);\n"
"}")
        self.f1.setFrameShape(QFrame.NoFrame)
        self.f1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.f1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.f1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_17)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_17)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_18)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.sb_area = QSpinBox(self.frame_18)
        self.sb_area.setObjectName(u"sb_area")
        self.sb_area.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(11)
        self.sb_area.setFont(font2)
        self.sb_area.setStyleSheet(u"QComboBox {\n"
"  background-color: #fbeee0;\n"
"  border: 2px solid #422800;\n"
"  border-radius: 5px;\n"
"  color: #422800;\n"
"}\n"
"")
        self.sb_area.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_area.setMinimum(20)
        self.sb_area.setMaximum(80)

        self.verticalLayout_34.addWidget(self.sb_area)


        self.verticalLayout_3.addWidget(self.frame_18)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.f1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_19)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_3 = QLabel(self.frame_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_3)


        self.verticalLayout_5.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_20)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.sb_rooms = QSpinBox(self.frame_20)
        self.sb_rooms.setObjectName(u"sb_rooms")
        self.sb_rooms.setMinimumSize(QSize(0, 30))
        self.sb_rooms.setFont(font2)
        self.sb_rooms.setStyleSheet(u"QComboBox {\n"
"  background-color: #fbeee0;\n"
"  border: 2px solid #422800;\n"
"  border-radius: 5px;\n"
"  color: #422800;\n"
"}\n"
"")
        self.sb_rooms.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_rooms.setMinimum(1)
        self.sb_rooms.setMaximum(5)

        self.verticalLayout_35.addWidget(self.sb_rooms)


        self.verticalLayout_5.addWidget(self.frame_20)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.f1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_21 = QFrame(self.frame_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_21)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_4 = QLabel(self.frame_21)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_22)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.sb_floor = QSpinBox(self.frame_22)
        self.sb_floor.setObjectName(u"sb_floor")
        self.sb_floor.setMinimumSize(QSize(0, 30))
        self.sb_floor.setFont(font2)
        self.sb_floor.setStyleSheet(u"QComboBox {\n"
"  background-color: #fbeee0;\n"
"  border: 2px solid #422800;\n"
"  border-radius: 5px;\n"
"  color: #422800;\n"
"}\n"
"")
        self.sb_floor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_floor.setMaximum(11)

        self.verticalLayout_37.addWidget(self.sb_floor)


        self.verticalLayout_6.addWidget(self.frame_22)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.f1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_23 = QFrame(self.frame_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_5 = QLabel(self.frame_23)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_4)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_24)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.sb_year = QSpinBox(self.frame_24)
        self.sb_year.setObjectName(u"sb_year")
        self.sb_year.setMinimumSize(QSize(0, 30))
        self.sb_year.setFont(font2)
        self.sb_year.setStyleSheet(u"QComboBox {\n"
"  background-color: #fbeee0;\n"
"  border: 2px solid #422800;\n"
"  border-radius: 5px;\n"
"  color: #422800;\n"
"}\n"
"")
        self.sb_year.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_year.setMinimum(1000)
        self.sb_year.setMaximum(2024)
        self.sb_year.setValue(2024)

        self.verticalLayout_36.addWidget(self.sb_year)


        self.verticalLayout_7.addWidget(self.frame_24)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.f1)

        self.f2 = QFrame(self.centralwidget)
        self.f2.setObjectName(u"f2")
        self.f2.setStyleSheet(u"#f2 {\n"
" background-color: rgba(230, 230, 230, 180);\n"
"}")
        self.f2.setFrameShape(QFrame.NoFrame)
        self.f2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.f2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.f2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_25 = QFrame(self.frame_5)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_25)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_6 = QLabel(self.frame_25)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_6)


        self.verticalLayout_11.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_5)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_ownership = QPushButton(self.frame_26)
        self.bt_ownership.setObjectName(u"bt_ownership")
        self.bt_ownership.setMinimumSize(QSize(32, 32))
        self.bt_ownership.setMaximumSize(QSize(32, 32))
        self.bt_ownership.setStyleSheet(u"")
        self.bt_ownership.setIconSize(QSize(32, 32))
        self.bt_ownership.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.bt_ownership)


        self.verticalLayout_11.addWidget(self.frame_26)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.f2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_27 = QFrame(self.frame_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_27)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_7 = QLabel(self.frame_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_7)


        self.verticalLayout_10.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_6)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bt_status = QPushButton(self.frame_28)
        self.bt_status.setObjectName(u"bt_status")
        self.bt_status.setMinimumSize(QSize(32, 32))
        self.bt_status.setMaximumSize(QSize(32, 32))
        self.bt_status.setIconSize(QSize(32, 32))
        self.bt_status.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.bt_status)


        self.verticalLayout_10.addWidget(self.frame_28)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.f2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_29 = QFrame(self.frame_7)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_29)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_8 = QLabel(self.frame_29)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_8)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_7)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.bt_balcony = QPushButton(self.frame_30)
        self.bt_balcony.setObjectName(u"bt_balcony")
        self.bt_balcony.setMinimumSize(QSize(32, 32))
        self.bt_balcony.setMaximumSize(QSize(32, 32))
        self.bt_balcony.setIconSize(QSize(32, 32))
        self.bt_balcony.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.bt_balcony)


        self.verticalLayout_9.addWidget(self.frame_30)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.f2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_31 = QFrame(self.frame_8)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_31)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_9 = QLabel(self.frame_31)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_9)


        self.verticalLayout_8.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_8)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bt_terrace = QPushButton(self.frame_32)
        self.bt_terrace.setObjectName(u"bt_terrace")
        self.bt_terrace.setMinimumSize(QSize(32, 32))
        self.bt_terrace.setMaximumSize(QSize(32, 32))
        self.bt_terrace.setIconSize(QSize(32, 32))
        self.bt_terrace.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.bt_terrace)


        self.verticalLayout_8.addWidget(self.frame_32)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.f2)

        self.f3 = QFrame(self.centralwidget)
        self.f3.setObjectName(u"f3")
        self.f3.setStyleSheet(u"#f3 {\n"
" background-color: rgba(220, 220, 220, 180);\n"
"}")
        self.f3.setFrameShape(QFrame.NoFrame)
        self.f3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.f3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.f3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_33 = QFrame(self.frame_9)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_33)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_10 = QLabel(self.frame_33)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_10)


        self.verticalLayout_12.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_9)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.bt_garden = QPushButton(self.frame_34)
        self.bt_garden.setObjectName(u"bt_garden")
        self.bt_garden.setMinimumSize(QSize(32, 32))
        self.bt_garden.setMaximumSize(QSize(32, 32))
        self.bt_garden.setIconSize(QSize(32, 32))
        self.bt_garden.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.bt_garden)


        self.verticalLayout_12.addWidget(self.frame_34)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.f3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_35 = QFrame(self.frame_10)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_35)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_11 = QLabel(self.frame_35)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_11)


        self.verticalLayout_13.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_10)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.bt_garage = QPushButton(self.frame_36)
        self.bt_garage.setObjectName(u"bt_garage")
        self.bt_garage.setMinimumSize(QSize(32, 32))
        self.bt_garage.setMaximumSize(QSize(32, 32))
        self.bt_garage.setIconSize(QSize(32, 32))
        self.bt_garage.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.bt_garage)


        self.verticalLayout_13.addWidget(self.frame_36)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.f3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_37 = QFrame(self.frame_11)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_37)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_12 = QLabel(self.frame_37)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_12)


        self.verticalLayout_14.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_11)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bt_lift = QPushButton(self.frame_38)
        self.bt_lift.setObjectName(u"bt_lift")
        self.bt_lift.setMinimumSize(QSize(32, 32))
        self.bt_lift.setMaximumSize(QSize(32, 32))
        self.bt_lift.setIconSize(QSize(32, 32))
        self.bt_lift.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.bt_lift)


        self.verticalLayout_14.addWidget(self.frame_38)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.f3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_39 = QFrame(self.frame_12)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_39)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_13 = QLabel(self.frame_39)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_13)


        self.verticalLayout_15.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_12)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.bt_city = QPushButton(self.frame_40)
        self.bt_city.setObjectName(u"bt_city")
        self.bt_city.setMinimumSize(QSize(32, 32))
        self.bt_city.setMaximumSize(QSize(32, 32))
        self.bt_city.setIconSize(QSize(32, 32))
        self.bt_city.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.bt_city)


        self.verticalLayout_15.addWidget(self.frame_40)


        self.horizontalLayout_4.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.f3)

        self.f4 = QFrame(self.centralwidget)
        self.f4.setObjectName(u"f4")
        self.f4.setStyleSheet(u"#f4 {\n"
" background-color: rgba(210, 210, 210, 180);\n"
"}")
        self.f4.setFrameShape(QFrame.NoFrame)
        self.f4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.f4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.f4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lb_prediction = QLabel(self.frame_15)
        self.lb_prediction.setObjectName(u"lb_prediction")
        font3 = QFont()
        font3.setFamilies([u"Rockwell"])
        font3.setPointSize(24)
        font3.setBold(True)
        self.lb_prediction.setFont(font3)
        self.lb_prediction.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.lb_prediction)


        self.horizontalLayout_5.addWidget(self.frame_15)


        self.verticalLayout.addWidget(self.f4)

        self.tail = QFrame(self.centralwidget)
        self.tail.setObjectName(u"tail")
        self.tail.setStyleSheet(u"#tail {\n"
" background-color: rgba(200, 200, 200, 180);\n"
" \n"
" background-color: rgba(239, 234, 178, 180);\n"
"}")
        self.tail.setFrameShape(QFrame.NoFrame)
        self.tail.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.tail)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, 0, 80, 0)
        self.bt_calculate = QPushButton(self.tail)
        self.bt_calculate.setObjectName(u"bt_calculate")
        self.bt_calculate.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.bt_calculate.setFont(font4)
        self.bt_calculate.setStyleSheet(u"QPushButton {\n"
"  background-color: #fbeee0;\n"
"  border: 2px solid #422800;\n"
"  border-radius: 10px;\n"
"  color: #422800;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fff;\n"
"}")

        self.horizontalLayout.addWidget(self.bt_calculate)

        self.bt_reset = QPushButton(self.tail)
        self.bt_reset.setObjectName(u"bt_reset")
        self.bt_reset.setMinimumSize(QSize(0, 50))
        self.bt_reset.setFont(font4)
        self.bt_reset.setStyleSheet(u"QPushButton {\n"
"  background-color: #fbeee0;\n"
"  border: 2px solid #422800;\n"
"  border-radius: 10px;\n"
"  color: #422800;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fff;\n"
"}")

        self.horizontalLayout.addWidget(self.bt_reset)


        self.verticalLayout.addWidget(self.tail)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Price Predictor - Poland 2024", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Area", None))
        self.sb_area.setSuffix("")
        self.sb_area.setPrefix("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of Rooms", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Floor Number", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Build Year", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Full Ownership?", None))
        self.bt_ownership.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ready to Move In?", None))
        self.bt_status.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Balcony?", None))
        self.bt_balcony.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Terrace?", None))
        self.bt_terrace.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Garden?", None))
        self.bt_garden.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Garage?", None))
        self.bt_garage.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Lift?", None))
        self.bt_lift.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Popular City?", None))
        self.bt_city.setText("")
        self.lb_prediction.setText(QCoreApplication.translate("MainWindow", u"100.000PLN - 180.000PLN", None))
        self.bt_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.bt_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1072, 1022)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(1050, 1000))
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(-1081, 0, 5000, 5000))
        self.scrollAreaWidgetContents_10.setMinimumSize(QSize(5000, 5000))
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents_10)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1908, 2335))
        self.verticalLayout_ = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_.setObjectName(u"verticalLayout_")
        self.verticalLayout_.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_ = QHBoxLayout()
        self.horizontalLayout_.setObjectName(u"horizontalLayout_")
        self.horizontalLayout_.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout_.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setSpacing(6)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_ = QGridLayout()
        self.gridLayout_.setObjectName(u"gridLayout_")
        self.gridLayout_.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mirror_hmd = QPushButton(self.layoutWidget)
        self.mirror_hmd.setObjectName(u"mirror_hmd")

        self.gridLayout_.addWidget(self.mirror_hmd, 3, 4, 1, 1)

        self.StartMecBaj_ = QPushButton(self.layoutWidget)
        self.StartMecBaj_.setObjectName(u"StartMecBaj_")

        self.gridLayout_.addWidget(self.StartMecBaj_, 25, 3, 1, 1)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_.addWidget(self.line_2, 15, 2, 1, 1)

        self.EscenarioCapturaEscaleras13 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras13.setObjectName(u"EscenarioCapturaEscaleras13")
        self.EscenarioCapturaEscaleras13.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"__pycache__/imgs/Metro3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras13.setIcon(icon)
        self.EscenarioCapturaEscaleras13.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras13, 17, 4, 1, 1)

        self.groupBox_86 = QGroupBox(self.layoutWidget)
        self.groupBox_86.setObjectName(u"groupBox_86")
        self.groupBox_86.setMinimumSize(QSize(130, 60))
        self.groupBox_86.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_86.setBaseSize(QSize(0, 0))
        self.VolumenMusicaRelajante_ = QSlider(self.groupBox_86)
        self.VolumenMusicaRelajante_.setObjectName(u"VolumenMusicaRelajante_")
        self.VolumenMusicaRelajante_.setGeometry(QRect(10, 30, 110, 25))
        self.VolumenMusicaRelajante_.setMinimumSize(QSize(110, 0))
        self.VolumenMusicaRelajante_.setMaximumSize(QSize(140, 16777215))
        self.VolumenMusicaRelajante_.setSliderPosition(50)
        self.VolumenMusicaRelajante_.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_86, 6, 2, 1, 1)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_.addWidget(self.line_4, 15, 4, 1, 1)

        self.EscalerasAutobus_ = QPushButton(self.layoutWidget)
        self.EscalerasAutobus_.setObjectName(u"EscalerasAutobus_")
        icon1 = QIcon()
        icon1.addFile(u"__pycache__/imgs3/EscBus.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasAutobus_.setIcon(icon1)
        self.EscalerasAutobus_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasAutobus_, 26, 0, 1, 1)

        self.mirror_biosensors = QPushButton(self.layoutWidget)
        self.mirror_biosensors.setObjectName(u"mirror_biosensors")

        self.gridLayout_.addWidget(self.mirror_biosensors, 3, 5, 1, 1)

        self.groupBox_4 = QGroupBox(self.layoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(100, 0))
        self.groupBox_4.setMaximumSize(QSize(197, 16777215))
        self.LCDNumber = QLCDNumber(self.groupBox_4)
        self.LCDNumber.setObjectName(u"LCDNumber")
        self.LCDNumber.setGeometry(QRect(50, 20, 60, 23))
        self.LCDNumber.setMinimumSize(QSize(45, 0))
        self.LCDNumber.setMaximumSize(QSize(75, 16777215))
        self.RestartTimer = QPushButton(self.groupBox_4)
        self.RestartTimer.setObjectName(u"RestartTimer")
        self.RestartTimer.setGeometry(QRect(50, 50, 61, 29))

        self.gridLayout_.addWidget(self.groupBox_4, 0, 5, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_.addWidget(self.label_6, 5, 0, 1, 1)

        self.AudioInstrucciones_ = QCheckBox(self.layoutWidget)
        self.AudioInstrucciones_.setObjectName(u"AudioInstrucciones_")

        self.gridLayout_.addWidget(self.AudioInstrucciones_, 7, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.layoutWidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 50))
        self.groupBox_8.setMaximumSize(QSize(16777215, 50))
        self.reiniciarPos = QPushButton(self.groupBox_8)
        self.reiniciarPos.setObjectName(u"reiniciarPos")
        self.reiniciarPos.setGeometry(QRect(0, 20, 55, 24))
        self.reiniciarPos.setMinimumSize(QSize(55, 0))
        self.reiniciarPos.setMaximumSize(QSize(50, 16777215))
        self.girar180 = QPushButton(self.groupBox_8)
        self.girar180.setObjectName(u"girar180")
        self.girar180.setGeometry(QRect(60, 20, 70, 24))
        self.girar180.setMinimumSize(QSize(70, 0))
        self.girar180.setMaximumSize(QSize(70, 16777215))
        self.girarmenos90 = QPushButton(self.groupBox_8)
        self.girarmenos90.setObjectName(u"girarmenos90")
        self.girarmenos90.setGeometry(QRect(130, 20, 65, 24))
        self.girarmenos90.setMinimumSize(QSize(65, 0))
        self.girarmenos90.setMaximumSize(QSize(65, 16777215))
        self.girar90 = QPushButton(self.groupBox_8)
        self.girar90.setObjectName(u"girar90")
        self.girar90.setGeometry(QRect(200, 20, 65, 24))
        self.girar90.setMinimumSize(QSize(65, 0))
        self.girar90.setMaximumSize(QSize(65, 16777215))

        self.gridLayout_.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.layoutWidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.MasTransparenciaGrisBaj = QPushButton(self.groupBox_9)
        self.MasTransparenciaGrisBaj.setObjectName(u"MasTransparenciaGrisBaj")
        self.MasTransparenciaGrisBaj.setGeometry(QRect(10, 40, 61, 24))
        self.MenosTransparenciaGrisBaj = QPushButton(self.groupBox_9)
        self.MenosTransparenciaGrisBaj.setObjectName(u"MenosTransparenciaGrisBaj")
        self.MenosTransparenciaGrisBaj.setGeometry(QRect(80, 40, 61, 24))

        self.gridLayout_.addWidget(self.groupBox_9, 21, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(120, 60))
        self.VolumenAudioInstruccionesFinales = QSlider(self.groupBox_5)
        self.VolumenAudioInstruccionesFinales.setObjectName(u"VolumenAudioInstruccionesFinales")
        self.VolumenAudioInstruccionesFinales.setGeometry(QRect(10, 30, 111, 22))
        self.VolumenAudioInstruccionesFinales.setMinimumSize(QSize(110, 0))
        self.VolumenAudioInstruccionesFinales.setMaximumSize(QSize(140, 16777215))
        self.VolumenAudioInstruccionesFinales.setSliderPosition(50)
        self.VolumenAudioInstruccionesFinales.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_5, 8, 2, 1, 1)

        self.LanzarVot = QPushButton(self.layoutWidget)
        self.LanzarVot.setObjectName(u"LanzarVot")
        self.LanzarVot.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_.addWidget(self.LanzarVot, 4, 3, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_.addWidget(self.label_8, 16, 0, 1, 1)

        self.groupBox_83 = QGroupBox(self.layoutWidget)
        self.groupBox_83.setObjectName(u"groupBox_83")
        self.groupBox_83.setMaximumSize(QSize(16777215, 70))
        self.VolumenEscalerasMecanicasBajada_ = QSlider(self.groupBox_83)
        self.VolumenEscalerasMecanicasBajada_.setObjectName(u"VolumenEscalerasMecanicasBajada_")
        self.VolumenEscalerasMecanicasBajada_.setGeometry(QRect(10, 30, 81, 25))
        self.VolumenEscalerasMecanicasBajada_.setSliderPosition(99)
        self.VolumenEscalerasMecanicasBajada_.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_83, 25, 2, 1, 1)

        self.EscenarioNeutroMontana = QPushButton(self.layoutWidget)
        self.EscenarioNeutroMontana.setObjectName(u"EscenarioNeutroMontana")
        self.EscenarioNeutroMontana.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"__pycache__/imgs3/Montan\u2560\u00e2a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioNeutroMontana.setIcon(icon2)
        self.EscenarioNeutroMontana.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioNeutroMontana, 11, 3, 1, 1)

        self.AudioInstruccionesFinales = QCheckBox(self.layoutWidget)
        self.AudioInstruccionesFinales.setObjectName(u"AudioInstruccionesFinales")

        self.gridLayout_.addWidget(self.AudioInstruccionesFinales, 8, 1, 1, 1)

        self.CerrarPuertasBusBaj_ = QPushButton(self.layoutWidget)
        self.CerrarPuertasBusBaj_.setObjectName(u"CerrarPuertasBusBaj_")

        self.gridLayout_.addWidget(self.CerrarPuertasBusBaj_, 27, 2, 1, 1)

        self.BarandillaEscalerasInterioresGris_ = QCheckBox(self.layoutWidget)
        self.BarandillaEscalerasInterioresGris_.setObjectName(u"BarandillaEscalerasInterioresGris_")
        self.BarandillaEscalerasInterioresGris_.setMaximumSize(QSize(85, 16777215))
        self.BarandillaEscalerasInterioresGris_.setChecked(True)

        self.gridLayout_.addWidget(self.BarandillaEscalerasInterioresGris_, 20, 1, 1, 1)

        self.EscalerasInterioresGrisesBaj_ = QPushButton(self.layoutWidget)
        self.EscalerasInterioresGrisesBaj_.setObjectName(u"EscalerasInterioresGrisesBaj_")
        icon3 = QIcon()
        icon3.addFile(u"__pycache__/imgs3/GrisesBajada.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasInterioresGrisesBaj_.setIcon(icon3)
        self.EscalerasInterioresGrisesBaj_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasInterioresGrisesBaj_, 21, 0, 1, 1)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_.addWidget(self.line_3, 15, 3, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_.addWidget(self.label_3, 9, 0, 1, 1)

        self.MusicaRelajante_ = QCheckBox(self.layoutWidget)
        self.MusicaRelajante_.setObjectName(u"MusicaRelajante_")
        self.MusicaRelajante_.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_.addWidget(self.MusicaRelajante_, 6, 1, 1, 1)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_.addWidget(self.line_6, 15, 0, 1, 1)

        self.EscenariosNeutros_ = QPushButton(self.layoutWidget)
        self.EscenariosNeutros_.setObjectName(u"EscenariosNeutros_")
        self.EscenariosNeutros_.setMaximumSize(QSize(270, 16777215))
        self.EscenariosNeutros_.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_.addWidget(self.EscenariosNeutros_, 10, 0, 1, 1)

        self.label_54 = QLabel(self.layoutWidget)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 5))

        self.gridLayout_.addWidget(self.label_54, 18, 0, 1, 1)

        self.DesplegableAudioInstrucciones = QComboBox(self.layoutWidget)
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.addItem("")
        self.DesplegableAudioInstrucciones.setObjectName(u"DesplegableAudioInstrucciones")

        self.gridLayout_.addWidget(self.DesplegableAudioInstrucciones, 7, 0, 1, 1)

        self.EscenarioNeutroPlaya2_ = QPushButton(self.layoutWidget)
        self.EscenarioNeutroPlaya2_.setObjectName(u"EscenarioNeutroPlaya2_")
        self.EscenarioNeutroPlaya2_.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"__pycache__/imgs/Playa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioNeutroPlaya2_.setIcon(icon4)
        self.EscenarioNeutroPlaya2_.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioNeutroPlaya2_, 11, 1, 1, 1)

        self.Capturas_Escaleras_ = QPushButton(self.layoutWidget)
        self.Capturas_Escaleras_.setObjectName(u"Capturas_Escaleras_")
        self.Capturas_Escaleras_.setMaximumSize(QSize(270, 16777215))
        self.Capturas_Escaleras_.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_.addWidget(self.Capturas_Escaleras_, 13, 0, 1, 1)

        self.CapturasAmigables03 = QPushButton(self.layoutWidget)
        self.CapturasAmigables03.setObjectName(u"CapturasAmigables03")
        self.CapturasAmigables03.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"__pycache__/imgs3/CapturaExteriorAmigable03.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.CapturasAmigables03.setIcon(icon5)
        self.CapturasAmigables03.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.CapturasAmigables03, 14, 3, 1, 1)

        self.groupBox_10 = QGroupBox(self.layoutWidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.MasTransparenciaNaranjaBaj = QPushButton(self.groupBox_10)
        self.MasTransparenciaNaranjaBaj.setObjectName(u"MasTransparenciaNaranjaBaj")
        self.MasTransparenciaNaranjaBaj.setGeometry(QRect(10, 40, 61, 24))
        self.MenosTransparenciaNaranjaBaj = QPushButton(self.groupBox_10)
        self.MenosTransparenciaNaranjaBaj.setObjectName(u"MenosTransparenciaNaranjaBaj")
        self.MenosTransparenciaNaranjaBaj.setGeometry(QRect(80, 40, 61, 24))

        self.gridLayout_.addWidget(self.groupBox_10, 23, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_.addWidget(self.label_2, 3, 0, 1, 1)

        self.EscalerasInterioresGrises_ = QPushButton(self.layoutWidget)
        self.EscalerasInterioresGrises_.setObjectName(u"EscalerasInterioresGrises_")
        self.EscalerasInterioresGrises_.setMaximumSize(QSize(270, 16777215))
        self.EscalerasInterioresGrises_.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"__pycache__/imgs3/Grises.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasInterioresGrises_.setIcon(icon6)
        self.EscalerasInterioresGrises_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasInterioresGrises_, 20, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.layoutWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.ManoEmpatica = QComboBox(self.groupBox_6)
        self.ManoEmpatica.addItem("")
        self.ManoEmpatica.addItem("")
        self.ManoEmpatica.setObjectName(u"ManoEmpatica")
        self.ManoEmpatica.setGeometry(QRect(10, 20, 141, 22))

        self.gridLayout_.addWidget(self.groupBox_6, 1, 2, 1, 1)

        self.Escenario_Playa_ = QPushButton(self.layoutWidget)
        self.Escenario_Playa_.setObjectName(u"Escenario_Playa_")
        self.Escenario_Playa_.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"__pycache__/imgs3/Rompeolas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Escenario_Playa_.setIcon(icon7)
        self.Escenario_Playa_.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.Escenario_Playa_, 11, 2, 1, 1)

        self.ReproducirAudiosInstrucciones = QPushButton(self.layoutWidget)
        self.ReproducirAudiosInstrucciones.setObjectName(u"ReproducirAudiosInstrucciones")

        self.gridLayout_.addWidget(self.ReproducirAudiosInstrucciones, 7, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_.addWidget(self.label_5, 4, 0, 1, 1)

        self.BarandillaInterioresNaranjasSub_ = QCheckBox(self.layoutWidget)
        self.BarandillaInterioresNaranjasSub_.setObjectName(u"BarandillaInterioresNaranjasSub_")
        self.BarandillaInterioresNaranjasSub_.setChecked(True)

        self.gridLayout_.addWidget(self.BarandillaInterioresNaranjasSub_, 22, 1, 1, 1)

        self.EscenarioNeutroSalonCasa_ = QPushButton(self.layoutWidget)
        self.EscenarioNeutroSalonCasa_.setObjectName(u"EscenarioNeutroSalonCasa_")
        self.EscenarioNeutroSalonCasa_.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"__pycache__/imgs/Salon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioNeutroSalonCasa_.setIcon(icon8)
        self.EscenarioNeutroSalonCasa_.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioNeutroSalonCasa_, 11, 4, 1, 1)

        self.groupBox_7 = QGroupBox(self.layoutWidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.nSesion = QLineEdit(self.groupBox_7)
        self.nSesion.setObjectName(u"nSesion")
        self.nSesion.setGeometry(QRect(10, 40, 113, 22))
        self.nSesion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_.addWidget(self.groupBox_7, 0, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CapturasAmigables01 = QPushButton(self.layoutWidget)
        self.CapturasAmigables01.setObjectName(u"CapturasAmigables01")
        self.CapturasAmigables01.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"__pycache__/imgs3/CapturaExteriorAmigable01.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.CapturasAmigables01.setIcon(icon9)
        self.CapturasAmigables01.setIconSize(QSize(90, 70))

        self.verticalLayout.addWidget(self.CapturasAmigables01)


        self.gridLayout_.addLayout(self.verticalLayout, 14, 1, 1, 1)

        self.AudioCapturasEscaleras_ = QCheckBox(self.layoutWidget)
        self.AudioCapturasEscaleras_.setObjectName(u"AudioCapturasEscaleras_")
        self.AudioCapturasEscaleras_.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_.addWidget(self.AudioCapturasEscaleras_, 13, 1, 1, 1)

        self.groupBox_87 = QGroupBox(self.layoutWidget)
        self.groupBox_87.setObjectName(u"groupBox_87")
        self.groupBox_87.setMinimumSize(QSize(0, 60))
        self.groupBox_87.setMaximumSize(QSize(16777215, 70))
        self.VolumenCapturasEscaleras_ = QSlider(self.groupBox_87)
        self.VolumenCapturasEscaleras_.setObjectName(u"VolumenCapturasEscaleras_")
        self.VolumenCapturasEscaleras_.setGeometry(QRect(10, 30, 131, 25))
        self.VolumenCapturasEscaleras_.setSliderPosition(50)
        self.VolumenCapturasEscaleras_.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_87, 13, 2, 1, 1)

        self.StartMecSub_ = QPushButton(self.layoutWidget)
        self.StartMecSub_.setObjectName(u"StartMecSub_")

        self.gridLayout_.addWidget(self.StartMecSub_, 24, 3, 1, 1)

        self.groupBox_12 = QGroupBox(self.layoutWidget)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 50))
        self.tiempo_votacion = QLineEdit(self.groupBox_12)
        self.tiempo_votacion.setObjectName(u"tiempo_votacion")
        self.tiempo_votacion.setGeometry(QRect(10, 20, 113, 20))
        self.tiempo_votacion.setMinimumSize(QSize(0, 20))
        self.tiempo_votacion.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_.addWidget(self.groupBox_12, 4, 1, 1, 1)

        self.EscenarioCapturaEscaleras05 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras05.setObjectName(u"EscenarioCapturaEscaleras05")
        self.EscenarioCapturaEscaleras05.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"__pycache__/imgs/Dentro2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras05.setIcon(icon10)
        self.EscenarioCapturaEscaleras05.setIconSize(QSize(100, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras05, 16, 5, 1, 1)

        self.button_home_ = QPushButton(self.layoutWidget)
        self.button_home_.setObjectName(u"button_home_")
        self.button_home_.setStyleSheet(u"background-color: rgb(170, 255, 127);")

        self.gridLayout_.addWidget(self.button_home_, 0, 3, 1, 1)

        self.CapturasAmigables02 = QPushButton(self.layoutWidget)
        self.CapturasAmigables02.setObjectName(u"CapturasAmigables02")
        self.CapturasAmigables02.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"__pycache__/imgs3/CapturaExteriorAmigable02.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.CapturasAmigables02.setIcon(icon11)
        self.CapturasAmigables02.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.CapturasAmigables02, 14, 2, 1, 1)

        self.EscalerasInterioresNaranjas_ = QPushButton(self.layoutWidget)
        self.EscalerasInterioresNaranjas_.setObjectName(u"EscalerasInterioresNaranjas_")
        icon12 = QIcon()
        icon12.addFile(u"__pycache__/imgs/VirtualNaranja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasInterioresNaranjas_.setIcon(icon12)
        self.EscalerasInterioresNaranjas_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasInterioresNaranjas_, 22, 0, 1, 1)

        self.EscenarioCapturaEscaleras11 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras11.setObjectName(u"EscenarioCapturaEscaleras11")
        self.EscenarioCapturaEscaleras11.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u"__pycache__/imgs/Metro2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras11.setIcon(icon13)
        self.EscenarioCapturaEscaleras11.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras11, 17, 5, 1, 1)

        self.VisibilidadRayo = QCheckBox(self.layoutWidget)
        self.VisibilidadRayo.setObjectName(u"VisibilidadRayo")
        self.VisibilidadRayo.setChecked(True)

        self.gridLayout_.addWidget(self.VisibilidadRayo, 4, 2, 1, 1)

        self.EscalerasInterioresNaranjasBaj_ = QPushButton(self.layoutWidget)
        self.EscalerasInterioresNaranjasBaj_.setObjectName(u"EscalerasInterioresNaranjasBaj_")
        icon14 = QIcon()
        icon14.addFile(u"__pycache__/imgs3/Naranjas.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasInterioresNaranjasBaj_.setIcon(icon14)
        self.EscalerasInterioresNaranjasBaj_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasInterioresNaranjasBaj_, 23, 0, 1, 1)

        self.groupBox_11 = QGroupBox(self.layoutWidget)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.MasAltura = QPushButton(self.groupBox_11)
        self.MasAltura.setObjectName(u"MasAltura")
        self.MasAltura.setGeometry(QRect(10, 20, 61, 21))
        self.MenosAlutra = QPushButton(self.groupBox_11)
        self.MenosAlutra.setObjectName(u"MenosAlutra")
        self.MenosAlutra.setGeometry(QRect(80, 20, 61, 21))

        self.gridLayout_.addWidget(self.groupBox_11, 1, 1, 1, 1)

        self.groupBox_88 = QGroupBox(self.layoutWidget)
        self.groupBox_88.setObjectName(u"groupBox_88")
        self.groupBox_88.setMaximumSize(QSize(16777215, 70))
        self.MasTransparenciaNaranja = QPushButton(self.groupBox_88)
        self.MasTransparenciaNaranja.setObjectName(u"MasTransparenciaNaranja")
        self.MasTransparenciaNaranja.setGeometry(QRect(10, 30, 61, 24))
        self.MenosTransparenciaNaranja = QPushButton(self.groupBox_88)
        self.MenosTransparenciaNaranja.setObjectName(u"MenosTransparenciaNaranja")
        self.MenosTransparenciaNaranja.setGeometry(QRect(80, 30, 61, 24))

        self.gridLayout_.addWidget(self.groupBox_88, 22, 2, 1, 1)

        self.EscenarioCapturaEscaleras01 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras01.setObjectName(u"EscenarioCapturaEscaleras01")
        self.EscenarioCapturaEscaleras01.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u"__pycache__/imgs/Fuera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras01.setIcon(icon15)
        self.EscenarioCapturaEscaleras01.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras01, 16, 1, 1, 1)

        self.ReproducirMusicaRelajante = QPushButton(self.layoutWidget)
        self.ReproducirMusicaRelajante.setObjectName(u"ReproducirMusicaRelajante")

        self.gridLayout_.addWidget(self.ReproducirMusicaRelajante, 6, 3, 1, 1)

        self.AudioEscenariosNeutros_ = QCheckBox(self.layoutWidget)
        self.AudioEscenariosNeutros_.setObjectName(u"AudioEscenariosNeutros_")
        self.AudioEscenariosNeutros_.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_.addWidget(self.AudioEscenariosNeutros_, 10, 1, 1, 1)

        self.CapturasAmigables04 = QPushButton(self.layoutWidget)
        self.CapturasAmigables04.setObjectName(u"CapturasAmigables04")
        self.CapturasAmigables04.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u"__pycache__/imgs3/CapturaExteriorAmigable04.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.CapturasAmigables04.setIcon(icon16)
        self.CapturasAmigables04.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.CapturasAmigables04, 14, 4, 1, 1)

        self.EscalerasMecanicasBaj_ = QPushButton(self.layoutWidget)
        self.EscalerasMecanicasBaj_.setObjectName(u"EscalerasMecanicasBaj_")
        self.EscalerasMecanicasBaj_.setMaximumSize(QSize(270, 16777215))
        self.EscalerasMecanicasBaj_.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u"__pycache__/imgs2/EscMecBajada.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasMecanicasBaj_.setIcon(icon17)
        self.EscalerasMecanicasBaj_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasMecanicasBaj_, 25, 0, 1, 1)

        self.AbrirPuertasBusSub_ = QPushButton(self.layoutWidget)
        self.AbrirPuertasBusSub_.setObjectName(u"AbrirPuertasBusSub_")

        self.gridLayout_.addWidget(self.AbrirPuertasBusSub_, 26, 1, 1, 1)

        self.AudioEscalerasMecanicasBajada_ = QCheckBox(self.layoutWidget)
        self.AudioEscalerasMecanicasBajada_.setObjectName(u"AudioEscalerasMecanicasBajada_")
        self.AudioEscalerasMecanicasBajada_.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_.addWidget(self.AudioEscalerasMecanicasBajada_, 25, 1, 1, 1)

        self.groupBox_89 = QGroupBox(self.layoutWidget)
        self.groupBox_89.setObjectName(u"groupBox_89")
        self.groupBox_89.setMinimumSize(QSize(265, 95))
        self.label_55 = QLabel(self.groupBox_89)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(30, 20, 60, 50))
        self.label_55.setMinimumSize(QSize(60, 50))
        self.label_55.setMaximumSize(QSize(60, 50))
        self.label_55.setPixmap(QPixmap(u"__pycache__/imgs3/Politecnica.png"))
        self.label_55.setScaledContents(True)
        self.label_58 = QLabel(self.groupBox_89)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(150, 30, 60, 40))
        self.label_58.setMinimumSize(QSize(60, 40))
        self.label_58.setPixmap(QPixmap(u"__pycache__/imgs3/Fundacion.png"))
        self.label_58.setScaledContents(True)
        self.label_62 = QLabel(self.groupBox_89)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(90, 30, 60, 40))
        self.label_62.setMinimumSize(QSize(60, 40))
        self.label_62.setPixmap(QPixmap(u"__pycache__/imgs3/Nokia.png"))
        self.label_62.setScaledContents(True)

        self.gridLayout_.addWidget(self.groupBox_89, 0, 0, 1, 1)

        self.EscenarioCapturaEscaleras09 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras09.setObjectName(u"EscenarioCapturaEscaleras09")
        self.EscenarioCapturaEscaleras09.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u"__pycache__/imgs3/Captura_Naranja_Subida.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras09.setIcon(icon18)
        self.EscenarioCapturaEscaleras09.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras09, 17, 1, 1, 1)

        self.StopMecBaj_ = QPushButton(self.layoutWidget)
        self.StopMecBaj_.setObjectName(u"StopMecBaj_")

        self.gridLayout_.addWidget(self.StopMecBaj_, 25, 4, 1, 1)

        self.EscalerasAutobusBaj_ = QPushButton(self.layoutWidget)
        self.EscalerasAutobusBaj_.setObjectName(u"EscalerasAutobusBaj_")
        icon19 = QIcon()
        icon19.addFile(u"__pycache__/imgs3/Escusaj.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasAutobusBaj_.setIcon(icon19)
        self.EscalerasAutobusBaj_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasAutobusBaj_, 27, 0, 1, 1)

        self.groupBox_84 = QGroupBox(self.layoutWidget)
        self.groupBox_84.setObjectName(u"groupBox_84")
        self.groupBox_84.setMaximumSize(QSize(16777215, 70))
        self.VolumenEscalerasMecanicasSubida_ = QSlider(self.groupBox_84)
        self.VolumenEscalerasMecanicasSubida_.setObjectName(u"VolumenEscalerasMecanicasSubida_")
        self.VolumenEscalerasMecanicasSubida_.setGeometry(QRect(10, 30, 81, 25))
        self.VolumenEscalerasMecanicasSubida_.setSliderPosition(99)
        self.VolumenEscalerasMecanicasSubida_.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_84, 24, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(80, 0))
        self.BateriaGafas = QLabel(self.groupBox_3)
        self.BateriaGafas.setObjectName(u"BateriaGafas")
        self.BateriaGafas.setGeometry(QRect(10, 20, 70, 16))
        self.BateriaGafas.setMinimumSize(QSize(70, 0))

        self.gridLayout_.addWidget(self.groupBox_3, 1, 5, 1, 1)

        self.groupBox_82 = QGroupBox(self.layoutWidget)
        self.groupBox_82.setObjectName(u"groupBox_82")
        self.groupBox_82.setMinimumSize(QSize(120, 60))
        self.VolumenAudioInstrucciones_ = QSlider(self.groupBox_82)
        self.VolumenAudioInstrucciones_.setObjectName(u"VolumenAudioInstrucciones_")
        self.VolumenAudioInstrucciones_.setGeometry(QRect(10, 30, 110, 25))
        self.VolumenAudioInstrucciones_.setMinimumSize(QSize(110, 0))
        self.VolumenAudioInstrucciones_.setMaximumSize(QSize(140, 16777215))
        self.VolumenAudioInstrucciones_.setSliderPosition(50)
        self.VolumenAudioInstrucciones_.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_82, 7, 2, 1, 1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_.addWidget(self.line, 15, 1, 1, 1)

        self.EscenarioCapturaEscaleras08 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras08.setObjectName(u"EscenarioCapturaEscaleras08")
        self.EscenarioCapturaEscaleras08.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u"__pycache__/imgs3/DentroSubida.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras08.setIcon(icon20)
        self.EscenarioCapturaEscaleras08.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras08, 17, 3, 1, 1)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_.addWidget(self.line_5, 15, 5, 1, 1)

        self.PararVot = QPushButton(self.layoutWidget)
        self.PararVot.setObjectName(u"PararVot")
        self.PararVot.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_.addWidget(self.PararVot, 4, 4, 1, 1)

        self.StopMecSub_ = QPushButton(self.layoutWidget)
        self.StopMecSub_.setObjectName(u"StopMecSub_")

        self.gridLayout_.addWidget(self.StopMecSub_, 24, 4, 1, 1)

        self.label_57 = QLabel(self.layoutWidget)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_.addWidget(self.label_57, 19, 0, 1, 1)

        self.EscenarioCapturaEscaleras02 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras02.setObjectName(u"EscenarioCapturaEscaleras02")
        self.EscenarioCapturaEscaleras02.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u"__pycache__/imgs3/Fuera2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras02.setIcon(icon21)
        self.EscenarioCapturaEscaleras02.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras02, 16, 2, 1, 1)

        self.EscenarioCapturaEscaleras06 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras06.setObjectName(u"EscenarioCapturaEscaleras06")
        self.EscenarioCapturaEscaleras06.setCursor(QCursor(Qt.PointingHandCursor))
        icon22 = QIcon()
        icon22.addFile(u"__pycache__/imgs/DentroBajada.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras06.setIcon(icon22)
        self.EscenarioCapturaEscaleras06.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras06, 17, 2, 1, 1)

        self.BarandillaInterioresGrisesBaj_ = QCheckBox(self.layoutWidget)
        self.BarandillaInterioresGrisesBaj_.setObjectName(u"BarandillaInterioresGrisesBaj_")
        self.BarandillaInterioresGrisesBaj_.setEnabled(True)
        self.BarandillaInterioresGrisesBaj_.setChecked(True)

        self.gridLayout_.addWidget(self.BarandillaInterioresGrisesBaj_, 21, 1, 1, 1)

        self.CapturasAmigables05 = QPushButton(self.layoutWidget)
        self.CapturasAmigables05.setObjectName(u"CapturasAmigables05")
        self.CapturasAmigables05.setCursor(QCursor(Qt.PointingHandCursor))
        icon23 = QIcon()
        icon23.addFile(u"__pycache__/imgs3/CapturaExteriorAmigable05.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.CapturasAmigables05.setIcon(icon23)
        self.CapturasAmigables05.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.CapturasAmigables05, 14, 5, 1, 1)

        self.EscenarioCapturaEscaleras03 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras03.setObjectName(u"EscenarioCapturaEscaleras03")
        self.EscenarioCapturaEscaleras03.setCursor(QCursor(Qt.PointingHandCursor))
        icon24 = QIcon()
        icon24.addFile(u"__pycache__/imgs3/Bus2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras03.setIcon(icon24)
        self.EscenarioCapturaEscaleras03.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras03, 16, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_.addWidget(self.label_4, 12, 0, 1, 1)

        self.groupBox_81 = QGroupBox(self.layoutWidget)
        self.groupBox_81.setObjectName(u"groupBox_81")
        self.groupBox_81.setMinimumSize(QSize(0, 60))
        self.groupBox_81.setMaximumSize(QSize(16777215, 70))
        self.VolumenEscenariosNeutros_ = QSlider(self.groupBox_81)
        self.VolumenEscenariosNeutros_.setObjectName(u"VolumenEscenariosNeutros_")
        self.VolumenEscenariosNeutros_.setGeometry(QRect(10, 30, 131, 25))
        self.VolumenEscenariosNeutros_.setSliderPosition(50)
        self.VolumenEscenariosNeutros_.setOrientation(Qt.Horizontal)

        self.gridLayout_.addWidget(self.groupBox_81, 10, 2, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_.addWidget(self.label_7, 14, 0, 1, 1)

        self.VotacionErronea = QPushButton(self.layoutWidget)
        self.VotacionErronea.setObjectName(u"VotacionErronea")
        self.VotacionErronea.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_.addWidget(self.VotacionErronea, 4, 5, 1, 1)

        self.groupBox_85 = QGroupBox(self.layoutWidget)
        self.groupBox_85.setObjectName(u"groupBox_85")
        self.groupBox_85.setMaximumSize(QSize(16777215, 70))
        self.MasTransparenciaGris = QPushButton(self.groupBox_85)
        self.MasTransparenciaGris.setObjectName(u"MasTransparenciaGris")
        self.MasTransparenciaGris.setGeometry(QRect(10, 30, 61, 24))
        self.MenosTransparenciaGris = QPushButton(self.groupBox_85)
        self.MenosTransparenciaGris.setObjectName(u"MenosTransparenciaGris")
        self.MenosTransparenciaGris.setGeometry(QRect(80, 30, 61, 24))

        self.gridLayout_.addWidget(self.groupBox_85, 20, 2, 1, 1)

        self.CerrarPuertasBusSub_ = QPushButton(self.layoutWidget)
        self.CerrarPuertasBusSub_.setObjectName(u"CerrarPuertasBusSub_")

        self.gridLayout_.addWidget(self.CerrarPuertasBusSub_, 26, 2, 1, 1)

        self.DesplegableMusicaRelajante = QComboBox(self.layoutWidget)
        self.DesplegableMusicaRelajante.addItem("")
        self.DesplegableMusicaRelajante.addItem("")
        self.DesplegableMusicaRelajante.setObjectName(u"DesplegableMusicaRelajante")

        self.gridLayout_.addWidget(self.DesplegableMusicaRelajante, 6, 0, 1, 1)

        self.AbrirPuertasBusBaj_ = QPushButton(self.layoutWidget)
        self.AbrirPuertasBusBaj_.setObjectName(u"AbrirPuertasBusBaj_")

        self.gridLayout_.addWidget(self.AbrirPuertasBusBaj_, 27, 1, 1, 1)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(160, 16777215))
        self.idPaciente = QLineEdit(self.groupBox)
        self.idPaciente.setObjectName(u"idPaciente")
        self.idPaciente.setGeometry(QRect(10, 40, 113, 22))
        self.idPaciente.setStyleSheet(u"")

        self.gridLayout_.addWidget(self.groupBox, 0, 1, 1, 1)

        self.EscalerasMecanicas_ = QPushButton(self.layoutWidget)
        self.EscalerasMecanicas_.setObjectName(u"EscalerasMecanicas_")
        self.EscalerasMecanicas_.setMaximumSize(QSize(270, 16777215))
        self.EscalerasMecanicas_.setCursor(QCursor(Qt.PointingHandCursor))
        icon25 = QIcon()
        icon25.addFile(u"__pycache__/imgs/EscMec.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscalerasMecanicas_.setIcon(icon25)
        self.EscalerasMecanicas_.setIconSize(QSize(130, 90))

        self.gridLayout_.addWidget(self.EscalerasMecanicas_, 24, 0, 1, 1)

        self.BarandillaInterioresNaranjasBaj_ = QCheckBox(self.layoutWidget)
        self.BarandillaInterioresNaranjasBaj_.setObjectName(u"BarandillaInterioresNaranjasBaj_")
        self.BarandillaInterioresNaranjasBaj_.setChecked(True)

        self.gridLayout_.addWidget(self.BarandillaInterioresNaranjasBaj_, 23, 1, 1, 1)

        self.button_back_ = QPushButton(self.layoutWidget)
        self.button_back_.setObjectName(u"button_back_")
        self.button_back_.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.gridLayout_.addWidget(self.button_back_, 0, 4, 1, 1)

        self.ReproducirAudioInstruccionesFinales = QPushButton(self.layoutWidget)
        self.ReproducirAudioInstruccionesFinales.setObjectName(u"ReproducirAudioInstruccionesFinales")

        self.gridLayout_.addWidget(self.ReproducirAudioInstruccionesFinales, 8, 3, 1, 1)

        self.AudioEscalerasMecanicasSubida_ = QCheckBox(self.layoutWidget)
        self.AudioEscalerasMecanicasSubida_.setObjectName(u"AudioEscalerasMecanicasSubida_")
        self.AudioEscalerasMecanicasSubida_.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_.addWidget(self.AudioEscalerasMecanicasSubida_, 24, 1, 1, 1)

        self.EscenarioCapturaEscaleras04 = QPushButton(self.layoutWidget)
        self.EscenarioCapturaEscaleras04.setObjectName(u"EscenarioCapturaEscaleras04")
        self.EscenarioCapturaEscaleras04.setCursor(QCursor(Qt.PointingHandCursor))
        icon26 = QIcon()
        icon26.addFile(u"__pycache__/imgs3/Bus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.EscenarioCapturaEscaleras04.setIcon(icon26)
        self.EscenarioCapturaEscaleras04.setIconSize(QSize(90, 70))

        self.gridLayout_.addWidget(self.EscenarioCapturaEscaleras04, 16, 4, 1, 1)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(120, 0))
        self.groupBox_2.setMaximumSize(QSize(200, 16777215))
        self.combo_device_ = QComboBox(self.groupBox_2)
        self.combo_device_.setObjectName(u"combo_device_")
        self.combo_device_.setGeometry(QRect(10, 20, 100, 22))
        self.combo_device_.setMinimumSize(QSize(80, 0))
        self.combo_device_.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_.addWidget(self.groupBox_2, 1, 4, 1, 1)

        self.ActualizarIP = QPushButton(self.layoutWidget)
        self.ActualizarIP.setObjectName(u"ActualizarIP")

        self.gridLayout_.addWidget(self.ActualizarIP, 1, 3, 1, 1)


        self.horizontalLayout_1.addLayout(self.gridLayout_)


        self.horizontalLayout_.addLayout(self.horizontalLayout_1)


        self.verticalLayout_.addLayout(self.horizontalLayout_)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_10)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mirror_hmd.setText(QCoreApplication.translate("MainWindow", u"Ver vista gafas (HMD)", None))
        self.StartMecBaj_.setText(QCoreApplication.translate("MainWindow", u"Poner en movimiento", None))
        self.EscenarioCapturaEscaleras13.setText("")
        self.groupBox_86.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.EscalerasAutobus_.setText(QCoreApplication.translate("MainWindow", u"Autob\u00fas", None))
        self.mirror_biosensors.setText(QCoreApplication.translate("MainWindow", u"Ver vista biosensores (m\u00f3vil)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.RestartTimer.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.label_6.setText("")
        self.AudioInstrucciones_.setText(QCoreApplication.translate("MainWindow", u"Audio con instrucciones", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Posici\u00f3n HMD", None))
        self.reiniciarPos.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.girar180.setText(QCoreApplication.translate("MainWindow", u"Dar la vuelta", None))
        self.girarmenos90.setText(QCoreApplication.translate("MainWindow", u"Girar izq", None))
        self.girar90.setText(QCoreApplication.translate("MainWindow", u"Girar dcha", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Transparencia escalones", None))
        self.MasTransparenciaGrisBaj.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.MenosTransparenciaGrisBaj.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.LanzarVot.setText(QCoreApplication.translate("MainWindow", u"Lanzar votaci\u00f3n", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Temidas    ", None))
        self.groupBox_83.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.EscenarioNeutroMontana.setText(QCoreApplication.translate("MainWindow", u"Monta\u00f1a", None))
        self.AudioInstruccionesFinales.setText(QCoreApplication.translate("MainWindow", u"Audio con instrucciones \n"
" finales", None))
        self.CerrarPuertasBusBaj_.setText(QCoreApplication.translate("MainWindow", u"Cerrar puertas", None))
        self.BarandillaEscalerasInterioresGris_.setText(QCoreApplication.translate("MainWindow", u"Barandilla", None))
        self.EscalerasInterioresGrisesBaj_.setText(QCoreApplication.translate("MainWindow", u"Interiores \n"
" grises \n"
" bajada", None))
        self.label_3.setText("")
        self.MusicaRelajante_.setText(QCoreApplication.translate("MainWindow", u"Musica Relajante", None))
        self.EscenariosNeutros_.setText(QCoreApplication.translate("MainWindow", u"Escenarios \n"
" Neutros", None))
        self.label_54.setText("")
        self.DesplegableAudioInstrucciones.setItemText(0, QCoreApplication.translate("MainWindow", u"Tecnica respiracion", None))
        self.DesplegableAudioInstrucciones.setItemText(1, QCoreApplication.translate("MainWindow", u"Respiracion consciente 1", None))
        self.DesplegableAudioInstrucciones.setItemText(2, QCoreApplication.translate("MainWindow", u"Respiracion consciente 2", None))
        self.DesplegableAudioInstrucciones.setItemText(3, QCoreApplication.translate("MainWindow", u"Como estas", None))
        self.DesplegableAudioInstrucciones.setItemText(4, QCoreApplication.translate("MainWindow", u"Como te encuentras", None))
        self.DesplegableAudioInstrucciones.setItemText(5, QCoreApplication.translate("MainWindow", u"Cuanto miedo te da", None))
        self.DesplegableAudioInstrucciones.setItemText(6, QCoreApplication.translate("MainWindow", u"Que tal estas", None))
        self.DesplegableAudioInstrucciones.setItemText(7, QCoreApplication.translate("MainWindow", u"Que tal te sientes", None))

        self.EscenarioNeutroPlaya2_.setText(QCoreApplication.translate("MainWindow", u"Playa", None))
        self.Capturas_Escaleras_.setText(QCoreApplication.translate("MainWindow", u"Capturas \n"
" Escaleras", None))
        self.CapturasAmigables03.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Transparencia escalones", None))
        self.MasTransparenciaNaranjaBaj.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.MenosTransparenciaNaranjaBaj.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText("")
        self.EscalerasInterioresGrises_.setText(QCoreApplication.translate("MainWindow", u"Interiores \n"
" grises", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Mano Emp\u00e1tica E4", None))
        self.ManoEmpatica.setItemText(0, QCoreApplication.translate("MainWindow", u"Mano izquierda", None))
        self.ManoEmpatica.setItemText(1, QCoreApplication.translate("MainWindow", u"Mano derecha", None))

        self.Escenario_Playa_.setText(QCoreApplication.translate("MainWindow", u"Rompeolas", None))
        self.ReproducirAudiosInstrucciones.setText(QCoreApplication.translate("MainWindow", u"Volver a empezar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"    Votaci\u00f3n", None))
        self.BarandillaInterioresNaranjasSub_.setText(QCoreApplication.translate("MainWindow", u"Barandilla", None))
        self.EscenarioNeutroSalonCasa_.setText(QCoreApplication.translate("MainWindow", u"Salon", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"N\u00ba sesion", None))
        self.CapturasAmigables01.setText("")
        self.AudioCapturasEscaleras_.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.groupBox_87.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.StartMecSub_.setText(QCoreApplication.translate("MainWindow", u"Poner en movimiento", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Tiempo de votaci\u00f3n", None))
        self.tiempo_votacion.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.EscenarioCapturaEscaleras05.setText("")
        self.button_home_.setText(QCoreApplication.translate("MainWindow", u"EMPEZAR APLICACI\u00d3N", None))
        self.CapturasAmigables02.setText("")
        self.EscalerasInterioresNaranjas_.setText(QCoreApplication.translate("MainWindow", u"Interiores \n"
" naranjas", None))
        self.EscenarioCapturaEscaleras11.setText("")
        self.VisibilidadRayo.setText(QCoreApplication.translate("MainWindow", u"Rayo visible", None))
        self.EscalerasInterioresNaranjasBaj_.setText(QCoreApplication.translate("MainWindow", u"Interiores \n"
" naranjas \n"
" bajada", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.MasAltura.setText(QCoreApplication.translate("MainWindow", u"M\u00e1s", None))
        self.MenosAlutra.setText(QCoreApplication.translate("MainWindow", u"Menos", None))
        self.groupBox_88.setTitle(QCoreApplication.translate("MainWindow", u"Transparencia escalones", None))
        self.MasTransparenciaNaranja.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.MenosTransparenciaNaranja.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.EscenarioCapturaEscaleras01.setText("")
        self.ReproducirMusicaRelajante.setText(QCoreApplication.translate("MainWindow", u"Volver a empezar", None))
        self.AudioEscenariosNeutros_.setText(QCoreApplication.translate("MainWindow", u"Audio videos neutros", None))
        self.CapturasAmigables04.setText("")
        self.EscalerasMecanicasBaj_.setText(QCoreApplication.translate("MainWindow", u"Mec\u00e1nicas \n"
" bajada", None))
        self.AbrirPuertasBusSub_.setText(QCoreApplication.translate("MainWindow", u"Abrir puertas", None))
        self.AudioEscalerasMecanicasBajada_.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.groupBox_89.setTitle("")
        self.label_55.setText("")
        self.label_58.setText("")
        self.label_62.setText("")
        self.EscenarioCapturaEscaleras09.setText("")
        self.StopMecBaj_.setText(QCoreApplication.translate("MainWindow", u"Parar", None))
        self.EscalerasAutobusBaj_.setText(QCoreApplication.translate("MainWindow", u"Autob\u00fas \n"
" bajada", None))
        self.groupBox_84.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Bater\u00eda", None))
        self.BateriaGafas.setText("")
        self.groupBox_82.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.EscenarioCapturaEscaleras08.setText("")
        self.PararVot.setText(QCoreApplication.translate("MainWindow", u"Parar Votaci\u00f3n", None))
        self.StopMecSub_.setText(QCoreApplication.translate("MainWindow", u"Parar", None))
        self.label_57.setText("")
        self.EscenarioCapturaEscaleras02.setText("")
        self.EscenarioCapturaEscaleras06.setText("")
        self.BarandillaInterioresGrisesBaj_.setText(QCoreApplication.translate("MainWindow", u"Barandilla", None))
        self.CapturasAmigables05.setText("")
        self.EscenarioCapturaEscaleras03.setText("")
        self.label_4.setText("")
        self.groupBox_81.setTitle(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Amigables    ", None))
        self.VotacionErronea.setText(QCoreApplication.translate("MainWindow", u"Votaci\u00f3n err\u00f3nea", None))
        self.groupBox_85.setTitle(QCoreApplication.translate("MainWindow", u"Transparencia escalones", None))
        self.MasTransparenciaGris.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.MenosTransparenciaGris.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.CerrarPuertasBusSub_.setText(QCoreApplication.translate("MainWindow", u"Cerrar puertas", None))
        self.DesplegableMusicaRelajante.setItemText(0, QCoreApplication.translate("MainWindow", u"Pista 1", None))
        self.DesplegableMusicaRelajante.setItemText(1, QCoreApplication.translate("MainWindow", u"Lluvia", None))

        self.AbrirPuertasBusBaj_.setText(QCoreApplication.translate("MainWindow", u"Abrir puertas", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"ID del paciente", None))
        self.EscalerasMecanicas_.setText(QCoreApplication.translate("MainWindow", u"Mec\u00e1nicas \n"
" subida", None))
        self.BarandillaInterioresNaranjasBaj_.setText(QCoreApplication.translate("MainWindow", u"Barandilla", None))
        self.button_back_.setText(QCoreApplication.translate("MainWindow", u"PARAR APLICACI\u00d3N", None))
        self.ReproducirAudioInstruccionesFinales.setText(QCoreApplication.translate("MainWindow", u"Volver a empezar", None))
        self.AudioEscalerasMecanicasSubida_.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.EscenarioCapturaEscaleras04.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Dispositivo", None))
        self.ActualizarIP.setText(QCoreApplication.translate("MainWindow", u"Actualizar IP dispositivo", None))
    # retranslateUi


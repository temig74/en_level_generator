# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_params = QGroupBox(self.centralwidget)
        self.groupBox_params.setObjectName(u"groupBox_params")
        self.groupBox_params.setMinimumSize(QSize(0, 0))
        self.gridLayout_6 = QGridLayout(self.groupBox_params)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.groupBox_loadEngine = QGroupBox(self.groupBox_params)
        self.groupBox_loadEngine.setObjectName(u"groupBox_loadEngine")
        self.gridLayout = QGridLayout(self.groupBox_loadEngine)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, -1, 5)
        self.checkBox_yo = QCheckBox(self.groupBox_loadEngine)
        self.checkBox_yo.setObjectName(u"checkBox_yo")
        self.checkBox_yo.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_yo, 3, 4, 1, 1)

        self.btn_loadSectors = QPushButton(self.groupBox_loadEngine)
        self.btn_loadSectors.setObjectName(u"btn_loadSectors")
        font = QFont()
        font.setPointSize(7)
        self.btn_loadSectors.setFont(font)

        self.gridLayout.addWidget(self.btn_loadSectors, 1, 2, 1, 1)

        self.label_domain = QLabel(self.groupBox_loadEngine)
        self.label_domain.setObjectName(u"label_domain")

        self.gridLayout.addWidget(self.label_domain, 2, 0, 1, 1)

        self.label_levelNum = QLabel(self.groupBox_loadEngine)
        self.label_levelNum.setObjectName(u"label_levelNum")

        self.gridLayout.addWidget(self.label_levelNum, 4, 0, 1, 1)

        self.label_gameId = QLabel(self.groupBox_loadEngine)
        self.label_gameId.setObjectName(u"label_gameId")

        self.gridLayout.addWidget(self.label_gameId, 3, 0, 1, 1)

        self.lineEdit_domain = QLineEdit(self.groupBox_loadEngine)
        self.lineEdit_domain.setObjectName(u"lineEdit_domain")

        self.gridLayout.addWidget(self.lineEdit_domain, 2, 1, 1, 1)

        self.spinBox_levelNum = QSpinBox(self.groupBox_loadEngine)
        self.spinBox_levelNum.setObjectName(u"spinBox_levelNum")
        self.spinBox_levelNum.setMaximumSize(QSize(40, 16777215))
        self.spinBox_levelNum.setMaximum(1000)
        self.spinBox_levelNum.setValue(1)

        self.gridLayout.addWidget(self.spinBox_levelNum, 4, 1, 1, 1)

        self.label_pass = QLabel(self.groupBox_loadEngine)
        self.label_pass.setObjectName(u"label_pass")

        self.gridLayout.addWidget(self.label_pass, 1, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.groupBox_loadEngine)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 1)

        self.lineEdit_gameId = QLineEdit(self.groupBox_loadEngine)
        self.lineEdit_gameId.setObjectName(u"lineEdit_gameId")

        self.gridLayout.addWidget(self.lineEdit_gameId, 3, 1, 1, 1)

        self.spinBox_startLoad = QSpinBox(self.groupBox_loadEngine)
        self.spinBox_startLoad.setObjectName(u"spinBox_startLoad")
        self.spinBox_startLoad.setMaximum(1000)
        self.spinBox_startLoad.setValue(1)

        self.gridLayout.addWidget(self.spinBox_startLoad, 4, 3, 1, 1)

        self.btn_loadTask = QPushButton(self.groupBox_loadEngine)
        self.btn_loadTask.setObjectName(u"btn_loadTask")
        self.btn_loadTask.setFont(font)

        self.gridLayout.addWidget(self.btn_loadTask, 0, 2, 1, 1)

        self.label_startLoad = QLabel(self.groupBox_loadEngine)
        self.label_startLoad.setObjectName(u"label_startLoad")

        self.gridLayout.addWidget(self.label_startLoad, 4, 2, 1, 1)

        self.spinBox_uploadDelay = QSpinBox(self.groupBox_loadEngine)
        self.spinBox_uploadDelay.setObjectName(u"spinBox_uploadDelay")
        self.spinBox_uploadDelay.setMaximum(100000)
        self.spinBox_uploadDelay.setValue(1500)

        self.gridLayout.addWidget(self.spinBox_uploadDelay, 3, 3, 1, 1)

        self.btn_loadBonuses = QPushButton(self.groupBox_loadEngine)
        self.btn_loadBonuses.setObjectName(u"btn_loadBonuses")

        self.gridLayout.addWidget(self.btn_loadBonuses, 2, 2, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_loadEngine)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_hours = QLabel(self.groupBox)
        self.label_hours.setObjectName(u"label_hours")

        self.gridLayout_7.addWidget(self.label_hours, 1, 0, 1, 1)

        self.label_minutes = QLabel(self.groupBox)
        self.label_minutes.setObjectName(u"label_minutes")

        self.gridLayout_7.addWidget(self.label_minutes, 1, 1, 1, 1)

        self.spinBox_hours = QSpinBox(self.groupBox)
        self.spinBox_hours.setObjectName(u"spinBox_hours")

        self.gridLayout_7.addWidget(self.spinBox_hours, 2, 0, 1, 1)

        self.spinBox_minutes = QSpinBox(self.groupBox)
        self.spinBox_minutes.setObjectName(u"spinBox_minutes")
        self.spinBox_minutes.setMaximum(59)
        self.spinBox_minutes.setValue(1)

        self.gridLayout_7.addWidget(self.spinBox_minutes, 2, 1, 1, 1)

        self.label_seconds = QLabel(self.groupBox)
        self.label_seconds.setObjectName(u"label_seconds")

        self.gridLayout_7.addWidget(self.label_seconds, 1, 2, 1, 1)

        self.spinBox_seconds = QSpinBox(self.groupBox)
        self.spinBox_seconds.setObjectName(u"spinBox_seconds")
        self.spinBox_seconds.setMaximum(59)

        self.gridLayout_7.addWidget(self.spinBox_seconds, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 3, 3, 2)

        self.spinBox_endLoad = QSpinBox(self.groupBox_loadEngine)
        self.spinBox_endLoad.setObjectName(u"spinBox_endLoad")
        self.spinBox_endLoad.setMaximum(1000)

        self.gridLayout.addWidget(self.spinBox_endLoad, 4, 4, 1, 1)

        self.label_login = QLabel(self.groupBox_loadEngine)
        self.label_login.setObjectName(u"label_login")

        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 1)

        self.lineEdit_login = QLineEdit(self.groupBox_loadEngine)
        self.lineEdit_login.setObjectName(u"lineEdit_login")

        self.gridLayout.addWidget(self.lineEdit_login, 0, 1, 1, 1)

        self.label_uploadDelay = QLabel(self.groupBox_loadEngine)
        self.label_uploadDelay.setObjectName(u"label_uploadDelay")

        self.gridLayout.addWidget(self.label_uploadDelay, 3, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_loadEngine, 1, 2, 1, 1)

        self.groupBox_fillImages = QGroupBox(self.groupBox_params)
        self.groupBox_fillImages.setObjectName(u"groupBox_fillImages")
        self.gridLayout_5 = QGridLayout(self.groupBox_fillImages)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, -1, 5)
        self.btn_saveToDisk = QPushButton(self.groupBox_fillImages)
        self.btn_saveToDisk.setObjectName(u"btn_saveToDisk")

        self.gridLayout_5.addWidget(self.btn_saveToDisk, 5, 0, 1, 2)

        self.label_imagesDelay = QLabel(self.groupBox_fillImages)
        self.label_imagesDelay.setObjectName(u"label_imagesDelay")

        self.gridLayout_5.addWidget(self.label_imagesDelay, 2, 0, 1, 1)

        self.spinBox_imagesDelay = QSpinBox(self.groupBox_fillImages)
        self.spinBox_imagesDelay.setObjectName(u"spinBox_imagesDelay")
        self.spinBox_imagesDelay.setMaximum(100000)
        self.spinBox_imagesDelay.setValue(3000)

        self.gridLayout_5.addWidget(self.spinBox_imagesDelay, 2, 1, 1, 1)

        self.label_prefix = QLabel(self.groupBox_fillImages)
        self.label_prefix.setObjectName(u"label_prefix")

        self.gridLayout_5.addWidget(self.label_prefix, 4, 0, 1, 1)

        self.lineEdit_prefix = QLineEdit(self.groupBox_fillImages)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")

        self.gridLayout_5.addWidget(self.lineEdit_prefix, 4, 1, 1, 1)

        self.lineEdit_yandexClass = QLineEdit(self.groupBox_fillImages)
        self.lineEdit_yandexClass.setObjectName(u"lineEdit_yandexClass")

        self.gridLayout_5.addWidget(self.lineEdit_yandexClass, 0, 1, 1, 1)

        self.lineEdit_googleClass = QLineEdit(self.groupBox_fillImages)
        self.lineEdit_googleClass.setObjectName(u"lineEdit_googleClass")

        self.gridLayout_5.addWidget(self.lineEdit_googleClass, 1, 1, 1, 1)

        self.btn_loadImagesYandex = QPushButton(self.groupBox_fillImages)
        self.btn_loadImagesYandex.setObjectName(u"btn_loadImagesYandex")

        self.gridLayout_5.addWidget(self.btn_loadImagesYandex, 0, 0, 1, 1)

        self.btn_loadImagesGoogle = QPushButton(self.groupBox_fillImages)
        self.btn_loadImagesGoogle.setObjectName(u"btn_loadImagesGoogle")

        self.gridLayout_5.addWidget(self.btn_loadImagesGoogle, 1, 0, 1, 1)

        self.label_imagesRelevance = QLabel(self.groupBox_fillImages)
        self.label_imagesRelevance.setObjectName(u"label_imagesRelevance")

        self.gridLayout_5.addWidget(self.label_imagesRelevance, 3, 0, 1, 1)

        self.spinBox_imagesRelevance = QSpinBox(self.groupBox_fillImages)
        self.spinBox_imagesRelevance.setObjectName(u"spinBox_imagesRelevance")
        self.spinBox_imagesRelevance.setValue(30)

        self.gridLayout_5.addWidget(self.spinBox_imagesRelevance, 3, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_fillImages, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_params)

        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setStyleSheet(u"background-color: rgb(255, 217, 103);")
        self.btn_stop.setCheckable(True)
        self.btn_stop.setChecked(False)

        self.verticalLayout.addWidget(self.btn_stop)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_fillAssoc = QGroupBox(self.tab)
        self.groupBox_fillAssoc.setObjectName(u"groupBox_fillAssoc")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_fillAssoc.sizePolicy().hasHeightForWidth())
        self.groupBox_fillAssoc.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox_fillAssoc)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_assocDelay = QLabel(self.groupBox_fillAssoc)
        self.label_assocDelay.setObjectName(u"label_assocDelay")

        self.horizontalLayout.addWidget(self.label_assocDelay)

        self.spinBox_assocDelay = QSpinBox(self.groupBox_fillAssoc)
        self.spinBox_assocDelay.setObjectName(u"spinBox_assocDelay")
        self.spinBox_assocDelay.setMaximum(10000)
        self.spinBox_assocDelay.setValue(50)

        self.horizontalLayout.addWidget(self.spinBox_assocDelay)

        self.label_assocRelevance = QLabel(self.groupBox_fillAssoc)
        self.label_assocRelevance.setObjectName(u"label_assocRelevance")

        self.horizontalLayout.addWidget(self.label_assocRelevance)

        self.spinBox_assocRelevance = QSpinBox(self.groupBox_fillAssoc)
        self.spinBox_assocRelevance.setObjectName(u"spinBox_assocRelevance")
        self.spinBox_assocRelevance.setMinimum(1)
        self.spinBox_assocRelevance.setValue(10)

        self.horizontalLayout.addWidget(self.spinBox_assocRelevance)


        self.gridLayout_2.addWidget(self.groupBox_fillAssoc, 0, 1, 1, 1)

        self.groupBox_genGrid = QGroupBox(self.tab)
        self.groupBox_genGrid.setObjectName(u"groupBox_genGrid")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_genGrid)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_gridHeight = QLabel(self.groupBox_genGrid)
        self.label_gridHeight.setObjectName(u"label_gridHeight")

        self.horizontalLayout_2.addWidget(self.label_gridHeight)

        self.spinBox_gridHeight = QSpinBox(self.groupBox_genGrid)
        self.spinBox_gridHeight.setObjectName(u"spinBox_gridHeight")
        self.spinBox_gridHeight.setMinimum(2)
        self.spinBox_gridHeight.setValue(4)

        self.horizontalLayout_2.addWidget(self.spinBox_gridHeight)

        self.btn_generateGrid = QPushButton(self.groupBox_genGrid)
        self.btn_generateGrid.setObjectName(u"btn_generateGrid")

        self.horizontalLayout_2.addWidget(self.btn_generateGrid)

        self.btn_clearGrid = QPushButton(self.groupBox_genGrid)
        self.btn_clearGrid.setObjectName(u"btn_clearGrid")

        self.horizontalLayout_2.addWidget(self.btn_clearGrid)


        self.gridLayout_2.addWidget(self.groupBox_genGrid, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 721, 332))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.layout_olimp = QGridLayout()
        self.layout_olimp.setObjectName(u"layout_olimp")

        self.gridLayout_3.addLayout(self.layout_olimp, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_formatType = QComboBox(self.groupBox_2)
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.addItem("")
        self.comboBox_formatType.setObjectName(u"comboBox_formatType")

        self.horizontalLayout_3.addWidget(self.comboBox_formatType)

        self.btn_generateDump = QPushButton(self.groupBox_2)
        self.btn_generateDump.setObjectName(u"btn_generateDump")

        self.horizontalLayout_3.addWidget(self.btn_generateDump)

        self.lineEdit_dump1 = QLineEdit(self.groupBox_2)
        self.lineEdit_dump1.setObjectName(u"lineEdit_dump1")
        self.lineEdit_dump1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_dump1)

        self.lineEdit_dump2 = QLineEdit(self.groupBox_2)
        self.lineEdit_dump2.setObjectName(u"lineEdit_dump2")
        self.lineEdit_dump2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_dump2)

        self.lineEdit_answer = QLineEdit(self.groupBox_2)
        self.lineEdit_answer.setObjectName(u"lineEdit_answer")

        self.horizontalLayout_3.addWidget(self.lineEdit_answer)

        self.btn_addDump = QPushButton(self.groupBox_2)
        self.btn_addDump.setObjectName(u"btn_addDump")

        self.horizontalLayout_3.addWidget(self.btn_addDump)

        self.btn_clearDump = QPushButton(self.groupBox_2)
        self.btn_clearDump.setObjectName(u"btn_clearDump")

        self.horizontalLayout_3.addWidget(self.btn_clearDump)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 765, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0437\u0430\u0434\u0430\u043d\u0438\u0439", None))
        self.groupBox_params.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox_loadEngine.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0432 \u0434\u0432\u0438\u0436\u043e\u043a", None))
        self.checkBox_yo.setText(QCoreApplication.translate("MainWindow", u"\u0415 = \u0401", None))
        self.btn_loadSectors.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440. \u0441\u0435\u043a\u0442\u043e\u0440\u044b", None))
        self.label_domain.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0435\u043d", None))
        self.label_levelNum.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.label_gameId.setText(QCoreApplication.translate("MainWindow", u"id \u0438\u0433\u0440\u044b", None))
        self.lineEdit_domain.setText(QCoreApplication.translate("MainWindow", u"tech.en.cx", None))
        self.label_pass.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_password.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.lineEdit_gameId.setText(QCoreApplication.translate("MainWindow", u"75356", None))
        self.btn_loadTask.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440. \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.label_startLoad.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442/ \u043a\u043e\u043d\u0435\u0446", None))
        self.btn_loadBonuses.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440. \u0431\u043e\u043d\u0443\u0441\u044b", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043d\u0443\u0441\u044b", None))
        self.label_hours.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u043e\u0432", None))
        self.label_minutes.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0443\u0442", None))
        self.label_seconds.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043a\u0443\u043d\u0434", None))
        self.label_login.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_login.setText(QCoreApplication.translate("MainWindow", u"Temig", None))
        self.label_uploadDelay.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430, \u043c\u0441", None))
        self.groupBox_fillImages.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430\u043c\u0438 \u0438\u0437 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.btn_saveToDisk.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430 \u0434\u0438\u0441\u043a", None))
        self.label_imagesDelay.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430, \u043c\u0441", None))
        self.label_prefix.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0444\u0438\u043a\u0441 ", None))
        self.lineEdit_prefix.setText(QCoreApplication.translate("MainWindow", u"Qg4g342g_1", None))
        self.lineEdit_yandexClass.setText(QCoreApplication.translate("MainWindow", u"avatars.mds.yandex.net.*?n=13", None))
        self.lineEdit_googleClass.setText(QCoreApplication.translate("MainWindow", u"DS1iW", None))
        self.btn_loadImagesYandex.setText(QCoreApplication.translate("MainWindow", u"\u042f\u043d\u0434\u0435\u043a\u0441", None))
        self.btn_loadImagesGoogle.setText(QCoreApplication.translate("MainWindow", u"Google", None))
        self.label_imagesRelevance.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043b\u0435\u0432\u0430\u043d\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.groupBox_fillAssoc.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 sociation.org", None))
        self.label_assocDelay.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430, \u043c\u0441", None))
        self.label_assocRelevance.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043b\u0435\u0432\u0430\u043d\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.groupBox_genGrid.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u0435\u0442\u043a\u0438", None))
        self.label_gridHeight.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u0435\u0442\u043a\u0438", None))
        self.spinBox_gridHeight.setSpecialValueText("")
        self.btn_generateGrid.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_clearGrid.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u043e\u043b\u0438\u043c\u043f\u0438\u0439\u043a\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.comboBox_formatType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.comboBox_formatType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0430\u0433\u0440\u0430\u043c\u043c\u0430 2", None))
        self.comboBox_formatType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u043e\u0433\u0440\u0438\u0444", None))
        self.comboBox_formatType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u043e\u0433\u0440\u0438\u0444 2", None))
        self.comboBox_formatType.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0411\u0440\u044e\u043a\u0432\u0430", None))
        self.comboBox_formatType.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0413\u0438\u0431\u0440\u0438\u0434 3", None))
        self.comboBox_formatType.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0413\u0438\u0431\u0440\u0438\u0434 4", None))
        self.comboBox_formatType.setItemText(7, QCoreApplication.translate("MainWindow", u"\u041f\u043b\u044e\u0441\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.comboBox_formatType.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.comboBox_formatType.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0440\u0430\u0434\u0430", None))
        self.comboBox_formatType.setItemText(10, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u043e\u0441\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435", None))

        self.btn_generateDump.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btn_addDump.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_clearDump.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u0441\u0435", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u043e1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0432\u043e2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442(\u044b)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"id1", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"id2", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u0432\u0430\u043b\u043a\u0438", None))
    # retranslateUi


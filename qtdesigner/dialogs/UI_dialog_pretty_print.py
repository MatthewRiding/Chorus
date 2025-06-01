# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_pretty_print.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_dialog_pretty_print(object):
    def setupUi(self, dialog_pretty_print):
        if not dialog_pretty_print.objectName():
            dialog_pretty_print.setObjectName(u"dialog_pretty_print")
        dialog_pretty_print.resize(1062, 667)
        self.verticalLayout_3 = QVBoxLayout(dialog_pretty_print)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(dialog_pretty_print)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_key = QHBoxLayout()
        self.horizontalLayout_key.setObjectName(u"horizontalLayout_key")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(dialog_pretty_print)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.scrollArea = QScrollArea(dialog_pretty_print)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMaximumSize(QSize(200, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 187, 533))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_title = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        self.lineEdit_title.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_title)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_y_label = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_y_label.setObjectName(u"lineEdit_y_label")
        self.lineEdit_y_label.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_5.addWidget(self.lineEdit_y_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.spinBox_width = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_width.setObjectName(u"spinBox_width")
        self.spinBox_width.setMaximum(100000)

        self.horizontalLayout_2.addWidget(self.spinBox_width)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.spinBox_height = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_height.setObjectName(u"spinBox_height")
        self.spinBox_height.setMaximum(100000)

        self.horizontalLayout_4.addWidget(self.spinBox_height)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_key.addLayout(self.verticalLayout_2)

        self.line = QFrame(dialog_pretty_print)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_key.addWidget(self.line)

        self.scrollArea_figure = QScrollArea(dialog_pretty_print)
        self.scrollArea_figure.setObjectName(u"scrollArea_figure")
        self.scrollArea_figure.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 834, 557))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_size_controller = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_size_controller.setObjectName(u"widget_size_controller")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_size_controller.sizePolicy().hasHeightForWidth())
        self.widget_size_controller.setSizePolicy(sizePolicy2)
        self.widget_size_controller.setMinimumSize(QSize(0, 0))
        self.widget_size_controller.setMaximumSize(QSize(1000000, 1000000))
        self.widget_size_controller.setBaseSize(QSize(600, 400))

        self.verticalLayout_4.addWidget(self.widget_size_controller, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.scrollArea_figure.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_key.addWidget(self.scrollArea_figure)


        self.verticalLayout_3.addLayout(self.horizontalLayout_key)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(dialog_pretty_print)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.pushButton_browse = QPushButton(dialog_pretty_print)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.buttonBox = QDialogButtonBox(dialog_pretty_print)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(dialog_pretty_print)
        self.buttonBox.accepted.connect(dialog_pretty_print.accept)
        self.buttonBox.rejected.connect(dialog_pretty_print.reject)

        QMetaObject.connectSlotsByName(dialog_pretty_print)
    # setupUi

    def retranslateUi(self, dialog_pretty_print):
        dialog_pretty_print.setWindowTitle(QCoreApplication.translate("dialog_pretty_print", u"Pretty Print", None))
        self.label_2.setText(QCoreApplication.translate("dialog_pretty_print", u"Pretty Print figure :", None))
        self.label_3.setText(QCoreApplication.translate("dialog_pretty_print", u"Parameters :", None))
        self.label.setText(QCoreApplication.translate("dialog_pretty_print", u"Title :", None))
        self.label_7.setText(QCoreApplication.translate("dialog_pretty_print", u"y label :", None))
        self.label_5.setText(QCoreApplication.translate("dialog_pretty_print", u"Width :", None))
        self.label_6.setText(QCoreApplication.translate("dialog_pretty_print", u"Height :", None))
        self.label_4.setText(QCoreApplication.translate("dialog_pretty_print", u"Save as :", None))
        self.pushButton_browse.setText("")
    # retranslateUi


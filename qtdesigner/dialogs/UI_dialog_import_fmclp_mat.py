# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_import_fmclp_mat.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_dialog_tfm_parameters_fmclp(object):
    def setupUi(self, dialog_tfm_parameters_fmclp):
        if not dialog_tfm_parameters_fmclp.objectName():
            dialog_tfm_parameters_fmclp.setObjectName(u"dialog_tfm_parameters_fmclp")
        dialog_tfm_parameters_fmclp.resize(466, 313)
        self.verticalLayout = QVBoxLayout(dialog_tfm_parameters_fmclp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_tfm_parameters = QLabel(dialog_tfm_parameters_fmclp)
        self.label_tfm_parameters.setObjectName(u"label_tfm_parameters")
        self.label_tfm_parameters.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_tfm_parameters.setFont(font)

        self.verticalLayout.addWidget(self.label_tfm_parameters)

        self.widget = QWidget(dialog_tfm_parameters_fmclp)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.line_edit_description = QLineEdit(self.widget)
        self.line_edit_description.setObjectName(u"line_edit_description")

        self.gridLayout_6.addWidget(self.line_edit_description, 0, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_file_path = QLineEdit(self.widget_2)
        self.lineEdit_file_path.setObjectName(u"lineEdit_file_path")

        self.gridLayout_7.addWidget(self.lineEdit_file_path, 0, 0, 1, 1)

        self.push_button_browse_for_file = QPushButton(self.widget_2)
        self.push_button_browse_for_file.setObjectName(u"push_button_browse_for_file")
        self.push_button_browse_for_file.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_7.addWidget(self.push_button_browse_for_file, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_2, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.groupBox = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setBold(False)
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.doubleSpinBox_time_min_us = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_time_min_us.setObjectName(u"doubleSpinBox_time_min_us")
        self.doubleSpinBox_time_min_us.setFont(font2)
        self.doubleSpinBox_time_min_us.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_time_min_us.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_time_min_us.setMaximum(1000.000000000000000)
        self.doubleSpinBox_time_min_us.setValue(-1.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_time_min_us, 0, 1, 1, 1)

        self.doubleSpinBox_time_max_us = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_time_max_us.setObjectName(u"doubleSpinBox_time_max_us")
        self.doubleSpinBox_time_max_us.setFont(font2)
        self.doubleSpinBox_time_max_us.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_time_max_us.setMinimum(-1000.000000000000000)
        self.doubleSpinBox_time_max_us.setMaximum(1000.000000000000000)
        self.doubleSpinBox_time_max_us.setValue(18.980000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_time_max_us, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout.addWidget(self.label_5)

        self.checkBox_detrend = QCheckBox(self.groupBox_3)
        self.checkBox_detrend.setObjectName(u"checkBox_detrend")
        self.checkBox_detrend.setMaximumSize(QSize(15, 16777215))
        self.checkBox_detrend.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_detrend)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(dialog_tfm_parameters_fmclp)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(dialog_tfm_parameters_fmclp)
        self.buttonBox.accepted.connect(dialog_tfm_parameters_fmclp.accept)
        self.buttonBox.rejected.connect(dialog_tfm_parameters_fmclp.reject)

        QMetaObject.connectSlotsByName(dialog_tfm_parameters_fmclp)
    # setupUi

    def retranslateUi(self, dialog_tfm_parameters_fmclp):
        dialog_tfm_parameters_fmclp.setWindowTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Dialog", None))
        self.label_tfm_parameters.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Import FMC-linear periodic from .mat 2D array format :", None))
        self.label.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Description :", None))
        self.label_2.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"File path :", None))
        self.push_button_browse_for_file.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Time record :", None))
        self.label_3.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Min :", None))
        self.doubleSpinBox_time_min_us.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"\u03bcs", None))
        self.doubleSpinBox_time_max_us.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"\u03bcs", None))
        self.label_4.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Max :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Pre-processing :", None))
        self.label_5.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"De-trend", None))
        self.checkBox_detrend.setText("")
    # retranslateUi


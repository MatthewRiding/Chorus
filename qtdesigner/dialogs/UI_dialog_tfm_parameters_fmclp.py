# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_tfm_parameters_fmclp.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_dialog_tfm_parameters_fmclp(object):
    def setupUi(self, dialog_tfm_parameters_fmclp):
        if not dialog_tfm_parameters_fmclp.objectName():
            dialog_tfm_parameters_fmclp.setObjectName(u"dialog_tfm_parameters_fmclp")
        dialog_tfm_parameters_fmclp.resize(286, 670)
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
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.line_edit_description = QLineEdit(self.widget)
        self.line_edit_description.setObjectName(u"line_edit_description")

        self.gridLayout_6.addWidget(self.line_edit_description, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.groupBox_2 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(True)
        self.groupBox_2.setFont(font1)
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 0))
        font2 = QFont()
        font2.setBold(False)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.doubleSpinBox_pitch_mm = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_pitch_mm.setObjectName(u"doubleSpinBox_pitch_mm")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_pitch_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_pitch_mm.setSizePolicy(sizePolicy)
        self.doubleSpinBox_pitch_mm.setFont(font2)
        self.doubleSpinBox_pitch_mm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_pitch_mm.setDecimals(4)
        self.doubleSpinBox_pitch_mm.setValue(0.100000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_pitch_mm)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setFont(font1)
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(90, 0))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.doubleSpinBox_v_L_ms = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_v_L_ms.setObjectName(u"doubleSpinBox_v_L_ms")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_v_L_ms.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_v_L_ms.setSizePolicy(sizePolicy)
        self.doubleSpinBox_v_L_ms.setFont(font2)
        self.doubleSpinBox_v_L_ms.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_v_L_ms.setMaximum(100000.000000000000000)
        self.doubleSpinBox_v_L_ms.setValue(6000.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_v_L_ms)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.doubleSpinBox_v_T_ms = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_v_T_ms.setObjectName(u"doubleSpinBox_v_T_ms")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_v_T_ms.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_v_T_ms.setSizePolicy(sizePolicy)
        self.doubleSpinBox_v_T_ms.setFont(font2)
        self.doubleSpinBox_v_T_ms.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_v_T_ms.setMaximum(100000.000000000000000)
        self.doubleSpinBox_v_T_ms.setValue(3000.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_v_T_ms)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setFont(font1)
        self.formLayout_3 = QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(90, 0))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_grid_size_x_mm = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_grid_size_x_mm.setObjectName(u"doubleSpinBox_grid_size_x_mm")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_grid_size_x_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_grid_size_x_mm.setSizePolicy(sizePolicy)
        self.doubleSpinBox_grid_size_x_mm.setFont(font2)
        self.doubleSpinBox_grid_size_x_mm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_grid_size_x_mm.setMaximum(1000.000000000000000)
        self.doubleSpinBox_grid_size_x_mm.setValue(40.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_grid_size_x_mm)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(90, 0))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.doubleSpinBox_grid_size_z_mm = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_grid_size_z_mm.setObjectName(u"doubleSpinBox_grid_size_z_mm")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_grid_size_z_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_grid_size_z_mm.setSizePolicy(sizePolicy)
        self.doubleSpinBox_grid_size_z_mm.setFont(font2)
        self.doubleSpinBox_grid_size_z_mm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_grid_size_z_mm.setMaximum(1000.000000000000000)
        self.doubleSpinBox_grid_size_z_mm.setValue(15.000000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_grid_size_z_mm)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(90, 0))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.spinBox_n_pixels_z = QSpinBox(self.groupBox_4)
        self.spinBox_n_pixels_z.setObjectName(u"spinBox_n_pixels_z")
        sizePolicy.setHeightForWidth(self.spinBox_n_pixels_z.sizePolicy().hasHeightForWidth())
        self.spinBox_n_pixels_z.setSizePolicy(sizePolicy)
        self.spinBox_n_pixels_z.setFont(font2)
        self.spinBox_n_pixels_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_n_pixels_z.setMaximum(10000)
        self.spinBox_n_pixels_z.setValue(100)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinBox_n_pixels_z)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_filter = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_filter.setObjectName(u"groupBox_filter")
        self.groupBox_filter.setMinimumSize(QSize(0, 0))
        self.groupBox_filter.setFont(font1)
        self.groupBox_filter.setCheckable(True)
        self.groupBox_filter.setChecked(True)
        self.formLayout_4 = QFormLayout(self.groupBox_filter)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_11 = QLabel(self.groupBox_filter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(90, 0))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.spinBox_butter_order = QSpinBox(self.groupBox_filter)
        self.spinBox_butter_order.setObjectName(u"spinBox_butter_order")
        sizePolicy.setHeightForWidth(self.spinBox_butter_order.sizePolicy().hasHeightForWidth())
        self.spinBox_butter_order.setSizePolicy(sizePolicy)
        self.spinBox_butter_order.setFont(font2)
        self.spinBox_butter_order.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_butter_order.setValue(10)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.spinBox_butter_order)

        self.label_12 = QLabel(self.groupBox_filter)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(90, 0))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.doubleSpinBox_band_min_MHz = QDoubleSpinBox(self.groupBox_filter)
        self.doubleSpinBox_band_min_MHz.setObjectName(u"doubleSpinBox_band_min_MHz")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_band_min_MHz.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_band_min_MHz.setSizePolicy(sizePolicy)
        self.doubleSpinBox_band_min_MHz.setFont(font2)
        self.doubleSpinBox_band_min_MHz.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_band_min_MHz.setMaximum(100.000000000000000)
        self.doubleSpinBox_band_min_MHz.setSingleStep(0.100000000000000)
        self.doubleSpinBox_band_min_MHz.setValue(4.000000000000000)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_band_min_MHz)

        self.label_13 = QLabel(self.groupBox_filter)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(90, 0))
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.doubleSpinBox_band_max_MHz = QDoubleSpinBox(self.groupBox_filter)
        self.doubleSpinBox_band_max_MHz.setObjectName(u"doubleSpinBox_band_max_MHz")
        sizePolicy.setHeightForWidth(self.doubleSpinBox_band_max_MHz.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_band_max_MHz.setSizePolicy(sizePolicy)
        self.doubleSpinBox_band_max_MHz.setFont(font2)
        self.doubleSpinBox_band_max_MHz.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_band_max_MHz.setMaximum(100.000000000000000)
        self.doubleSpinBox_band_max_MHz.setSingleStep(0.100000000000000)
        self.doubleSpinBox_band_max_MHz.setValue(12.000000000000000)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_band_max_MHz)


        self.verticalLayout.addWidget(self.groupBox_filter)

        self.groupBox_gen_mask = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_gen_mask.setObjectName(u"groupBox_gen_mask")
        self.groupBox_gen_mask.setFont(font1)
        self.groupBox_gen_mask.setCheckable(True)
        self.groupBox_gen_mask.setChecked(False)
        self.formLayout_5 = QFormLayout(self.groupBox_gen_mask)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_3 = QLabel(self.groupBox_gen_mask)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 0))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.comboBox_mask_angle = QComboBox(self.groupBox_gen_mask)
        self.comboBox_mask_angle.setObjectName(u"comboBox_mask_angle")
        self.comboBox_mask_angle.setFont(font2)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.comboBox_mask_angle)

        self.doubleSpinBox_mask_angle = QDoubleSpinBox(self.groupBox_gen_mask)
        self.doubleSpinBox_mask_angle.setObjectName(u"doubleSpinBox_mask_angle")
        self.doubleSpinBox_mask_angle.setFont(font2)
        self.doubleSpinBox_mask_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_mask_angle.setReadOnly(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_mask_angle)

        self.label_4 = QLabel(self.groupBox_gen_mask)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboBox_mask_behaviour = QComboBox(self.groupBox_gen_mask)
        self.comboBox_mask_behaviour.setObjectName(u"comboBox_mask_behaviour")
        self.comboBox_mask_behaviour.setFont(font2)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.comboBox_mask_behaviour)


        self.verticalLayout.addWidget(self.groupBox_gen_mask)

        self.frame = QFrame(dialog_tfm_parameters_fmclp)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.comboBox_wave_set = QComboBox(self.frame)
        self.comboBox_wave_set.setObjectName(u"comboBox_wave_set")
        sizePolicy.setHeightForWidth(self.comboBox_wave_set.sizePolicy().hasHeightForWidth())
        self.comboBox_wave_set.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.comboBox_wave_set, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

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

        self.comboBox_mask_angle.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(dialog_tfm_parameters_fmclp)
    # setupUi

    def retranslateUi(self, dialog_tfm_parameters_fmclp):
        dialog_tfm_parameters_fmclp.setWindowTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Dialog", None))
        self.label_tfm_parameters.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"TFM parameters :", None))
        self.label.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Image name :", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Array parameters:", None))
        self.label_5.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Pitch :", None))
        self.doubleSpinBox_pitch_mm.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"mm", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Wave speeds:", None))
        self.label_6.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"v_L :", None))
        self.doubleSpinBox_v_L_ms.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"ms\u207b\u00b9", None))
        self.label_2.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"v_T :", None))
        self.doubleSpinBox_v_T_ms.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"ms\u207b\u00b9", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Grid parameters:", None))
        self.label_8.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Grid size x :", None))
        self.doubleSpinBox_grid_size_x_mm.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"mm", None))
        self.label_9.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Grid size z :", None))
        self.doubleSpinBox_grid_size_z_mm.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"mm", None))
        self.label_10.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"n pixels z :", None))
        self.groupBox_filter.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Scipy 'butter' bandpass filter :", None))
        self.label_11.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Order N :", None))
        self.label_12.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Band min :", None))
        self.doubleSpinBox_band_min_MHz.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"MHz", None))
        self.label_13.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Band max :", None))
        self.doubleSpinBox_band_max_MHz.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"MHz", None))
        self.groupBox_gen_mask.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Generation ray angle mask :", None))
        self.label_3.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Mask angle :", None))
        self.comboBox_mask_angle.setCurrentText("")
        self.doubleSpinBox_mask_angle.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Mask behaviour :", None))
        self.label_7.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Wave set:", None))
    # retranslateUi


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
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_dialog_tfm_parameters_fmclp(object):
    def setupUi(self, dialog_tfm_parameters_fmclp):
        if not dialog_tfm_parameters_fmclp.objectName():
            dialog_tfm_parameters_fmclp.setObjectName(u"dialog_tfm_parameters_fmclp")
        dialog_tfm_parameters_fmclp.resize(984, 732)
        self.verticalLayout_2 = QVBoxLayout(dialog_tfm_parameters_fmclp)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.line_edit_description = QLineEdit(self.widget)
        self.line_edit_description.setObjectName(u"line_edit_description")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit_description.sizePolicy().hasHeightForWidth())
        self.line_edit_description.setSizePolicy(sizePolicy1)

        self.gridLayout_6.addWidget(self.line_edit_description, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.groupBox_2 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setBold(True)
        self.groupBox_2.setFont(font1)
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setBold(False)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.doubleSpinBox_pitch_mm = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_pitch_mm.setObjectName(u"doubleSpinBox_pitch_mm")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_pitch_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_pitch_mm.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_pitch_mm.setFont(font2)
        self.doubleSpinBox_pitch_mm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_pitch_mm.setDecimals(4)
        self.doubleSpinBox_pitch_mm.setValue(0.100000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_pitch_mm)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setMaximumSize(QSize(250, 16777215))
        self.groupBox_4.setFont(font1)
        self.formLayout_3 = QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_grid_size_x_mm = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_grid_size_x_mm.setObjectName(u"doubleSpinBox_grid_size_x_mm")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_grid_size_x_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_grid_size_x_mm.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_grid_size_x_mm.setFont(font2)
        self.doubleSpinBox_grid_size_x_mm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_grid_size_x_mm.setMaximum(1000.000000000000000)
        self.doubleSpinBox_grid_size_x_mm.setValue(40.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_grid_size_x_mm)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.doubleSpinBox_grid_size_z_mm = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_grid_size_z_mm.setObjectName(u"doubleSpinBox_grid_size_z_mm")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_grid_size_z_mm.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_grid_size_z_mm.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_grid_size_z_mm.setFont(font2)
        self.doubleSpinBox_grid_size_z_mm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_grid_size_z_mm.setMaximum(1000.000000000000000)
        self.doubleSpinBox_grid_size_z_mm.setValue(15.000000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_grid_size_z_mm)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.spinBox_n_pixels_z = QSpinBox(self.groupBox_4)
        self.spinBox_n_pixels_z.setObjectName(u"spinBox_n_pixels_z")
        sizePolicy1.setHeightForWidth(self.spinBox_n_pixels_z.sizePolicy().hasHeightForWidth())
        self.spinBox_n_pixels_z.setSizePolicy(sizePolicy1)
        self.spinBox_n_pixels_z.setFont(font2)
        self.spinBox_n_pixels_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_n_pixels_z.setMaximum(10000)
        self.spinBox_n_pixels_z.setValue(100)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinBox_n_pixels_z)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(250, 16777215))
        self.groupBox_3.setFont(font1)
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.doubleSpinBox_c_l_mpers = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_c_l_mpers.setObjectName(u"doubleSpinBox_c_l_mpers")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_c_l_mpers.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_c_l_mpers.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_c_l_mpers.setFont(font2)
        self.doubleSpinBox_c_l_mpers.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_c_l_mpers.setMaximum(100000.000000000000000)
        self.doubleSpinBox_c_l_mpers.setValue(6000.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_c_l_mpers)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.doubleSpinBox_c_t_mpers = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_c_t_mpers.setObjectName(u"doubleSpinBox_c_t_mpers")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_c_t_mpers.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_c_t_mpers.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_c_t_mpers.setFont(font2)
        self.doubleSpinBox_c_t_mpers.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_c_t_mpers.setMaximum(100000.000000000000000)
        self.doubleSpinBox_c_t_mpers.setValue(3000.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_c_t_mpers)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 0))
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.doubleSpinBox_c_lsaw_mpers = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_c_lsaw_mpers.setObjectName(u"doubleSpinBox_c_lsaw_mpers")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_c_lsaw_mpers.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_c_lsaw_mpers.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_c_lsaw_mpers.setFont(font2)
        self.doubleSpinBox_c_lsaw_mpers.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_c_lsaw_mpers.setMaximum(100000.000000000000000)
        self.doubleSpinBox_c_lsaw_mpers.setValue(6000.000000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_c_lsaw_mpers)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_filter = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_filter.setObjectName(u"groupBox_filter")
        sizePolicy.setHeightForWidth(self.groupBox_filter.sizePolicy().hasHeightForWidth())
        self.groupBox_filter.setSizePolicy(sizePolicy)
        self.groupBox_filter.setMinimumSize(QSize(0, 0))
        self.groupBox_filter.setMaximumSize(QSize(250, 16777215))
        self.groupBox_filter.setFont(font1)
        self.groupBox_filter.setCheckable(True)
        self.groupBox_filter.setChecked(True)
        self.formLayout_4 = QFormLayout(self.groupBox_filter)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_11 = QLabel(self.groupBox_filter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.spinBox_butter_order = QSpinBox(self.groupBox_filter)
        self.spinBox_butter_order.setObjectName(u"spinBox_butter_order")
        sizePolicy1.setHeightForWidth(self.spinBox_butter_order.sizePolicy().hasHeightForWidth())
        self.spinBox_butter_order.setSizePolicy(sizePolicy1)
        self.spinBox_butter_order.setFont(font2)
        self.spinBox_butter_order.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_butter_order.setValue(10)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.spinBox_butter_order)

        self.label_12 = QLabel(self.groupBox_filter)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 0))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.doubleSpinBox_band_min_MHz = QDoubleSpinBox(self.groupBox_filter)
        self.doubleSpinBox_band_min_MHz.setObjectName(u"doubleSpinBox_band_min_MHz")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_band_min_MHz.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_band_min_MHz.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_band_min_MHz.setFont(font2)
        self.doubleSpinBox_band_min_MHz.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_band_min_MHz.setMaximum(100.000000000000000)
        self.doubleSpinBox_band_min_MHz.setSingleStep(0.100000000000000)
        self.doubleSpinBox_band_min_MHz.setValue(4.000000000000000)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_band_min_MHz)

        self.label_13 = QLabel(self.groupBox_filter)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 0))
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_13)

        self.doubleSpinBox_band_max_MHz = QDoubleSpinBox(self.groupBox_filter)
        self.doubleSpinBox_band_max_MHz.setObjectName(u"doubleSpinBox_band_max_MHz")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_band_max_MHz.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_band_max_MHz.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_band_max_MHz.setFont(font2)
        self.doubleSpinBox_band_max_MHz.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_band_max_MHz.setMaximum(100.000000000000000)
        self.doubleSpinBox_band_max_MHz.setSingleStep(0.100000000000000)
        self.doubleSpinBox_band_max_MHz.setValue(12.000000000000000)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_band_max_MHz)


        self.verticalLayout.addWidget(self.groupBox_filter)

        self.groupBox_gen_mask = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox_gen_mask.setObjectName(u"groupBox_gen_mask")
        sizePolicy.setHeightForWidth(self.groupBox_gen_mask.sizePolicy().hasHeightForWidth())
        self.groupBox_gen_mask.setSizePolicy(sizePolicy)
        self.groupBox_gen_mask.setMaximumSize(QSize(250, 16777215))
        self.groupBox_gen_mask.setFont(font1)
        self.groupBox_gen_mask.setCheckable(True)
        self.groupBox_gen_mask.setChecked(False)
        self.formLayout_5 = QFormLayout(self.groupBox_gen_mask)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_3 = QLabel(self.groupBox_gen_mask)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.comboBox_mask_angle = QComboBox(self.groupBox_gen_mask)
        self.comboBox_mask_angle.setObjectName(u"comboBox_mask_angle")
        sizePolicy1.setHeightForWidth(self.comboBox_mask_angle.sizePolicy().hasHeightForWidth())
        self.comboBox_mask_angle.setSizePolicy(sizePolicy1)
        self.comboBox_mask_angle.setFont(font2)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.comboBox_mask_angle)

        self.doubleSpinBox_mask_angle = QDoubleSpinBox(self.groupBox_gen_mask)
        self.doubleSpinBox_mask_angle.setObjectName(u"doubleSpinBox_mask_angle")
        sizePolicy1.setHeightForWidth(self.doubleSpinBox_mask_angle.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_mask_angle.setSizePolicy(sizePolicy1)
        self.doubleSpinBox_mask_angle.setFont(font2)
        self.doubleSpinBox_mask_angle.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.doubleSpinBox_mask_angle.setReadOnly(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_mask_angle)

        self.label_4 = QLabel(self.groupBox_gen_mask)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboBox_mask_behaviour = QComboBox(self.groupBox_gen_mask)
        self.comboBox_mask_behaviour.setObjectName(u"comboBox_mask_behaviour")
        sizePolicy1.setHeightForWidth(self.comboBox_mask_behaviour.sizePolicy().hasHeightForWidth())
        self.comboBox_mask_behaviour.setSizePolicy(sizePolicy1)
        self.comboBox_mask_behaviour.setFont(font2)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.comboBox_mask_behaviour)


        self.verticalLayout.addWidget(self.groupBox_gen_mask)

        self.groupBox = QGroupBox(dialog_tfm_parameters_fmclp)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setFont(font1)
        self.formLayout_6 = QFormLayout(self.groupBox)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.comboBox_send = QComboBox(self.groupBox)
        self.comboBox_send.setObjectName(u"comboBox_send")
        sizePolicy1.setHeightForWidth(self.comboBox_send.sizePolicy().hasHeightForWidth())
        self.comboBox_send.setSizePolicy(sizePolicy1)
        self.comboBox_send.setFont(font2)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.comboBox_send)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.comboBox_receive = QComboBox(self.groupBox)
        self.comboBox_receive.setObjectName(u"comboBox_receive")
        sizePolicy1.setHeightForWidth(self.comboBox_receive.sizePolicy().hasHeightForWidth())
        self.comboBox_receive.setSizePolicy(sizePolicy1)
        self.comboBox_receive.setFont(font2)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.comboBox_receive)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget_2 = QWidget(dialog_tfm_parameters_fmclp)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(dialog_tfm_parameters_fmclp)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


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
        self.groupBox_4.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Grid parameters:", None))
        self.label_8.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Grid size x :", None))
        self.doubleSpinBox_grid_size_x_mm.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"mm", None))
        self.label_9.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Grid size z :", None))
        self.doubleSpinBox_grid_size_z_mm.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"mm", None))
        self.label_10.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"n pixels z :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Wave speeds:", None))
        self.label_6.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Longitudinal (c<sub>L</sub>) :", None))
        self.doubleSpinBox_c_l_mpers.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"ms\u207b\u00b9", None))
        self.label_2.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Shear (c<sub>T</sub>) :", None))
        self.doubleSpinBox_c_t_mpers.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"ms\u207b\u00b9", None))
        self.label_15.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"<html><head/><body><p>LSAW (c<span style=\" vertical-align:sub;\">LSAW</span>) :</p></body></html>", None))
        self.doubleSpinBox_c_lsaw_mpers.setSuffix(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"ms\u207b\u00b9", None))
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
        self.groupBox.setTitle(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Send && receive wave types :", None))
        self.label_7.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Send :", None))
        self.label_14.setText(QCoreApplication.translate("dialog_tfm_parameters_fmclp", u"Receive :", None))
    # retranslateUi


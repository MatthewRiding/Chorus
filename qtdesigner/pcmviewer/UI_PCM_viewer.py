# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PCM_viewer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

from classdefs.modpcmplotwidget import PCMWidget
from classdefs.modphasorplotwidget import PhasorPlotWidget
from classdefs.modsumvsmaskanglewidget import SumVSMaskAngleWidget

class Ui_PCM_viewer(object):
    def setupUi(self, PCM_viewer):
        if not PCM_viewer.objectName():
            PCM_viewer.setObjectName(u"PCM_viewer")
        PCM_viewer.resize(1018, 581)
        self.horizontalLayout_2 = QHBoxLayout(PCM_viewer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(PCM_viewer)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_real = QCheckBox(self.widget_2)
        self.checkBox_real.setObjectName(u"checkBox_real")

        self.horizontalLayout.addWidget(self.checkBox_real)

        self.checkBox_imag = QCheckBox(self.widget_2)
        self.checkBox_imag.setObjectName(u"checkBox_imag")

        self.horizontalLayout.addWidget(self.checkBox_imag)

        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.check_box_crit = QCheckBox(self.widget_2)
        self.check_box_crit.setObjectName(u"check_box_crit")

        self.horizontalLayout.addWidget(self.check_box_crit)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.check_box_sign = QCheckBox(self.widget_2)
        self.check_box_sign.setObjectName(u"check_box_sign")

        self.horizontalLayout.addWidget(self.check_box_sign)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.mpl_widget_pcm = PCMWidget(PCM_viewer)
        self.mpl_widget_pcm.setObjectName(u"mpl_widget_pcm")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_widget_pcm.sizePolicy().hasHeightForWidth())
        self.mpl_widget_pcm.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.mpl_widget_pcm)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(PCM_viewer)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.tabWidget = QTabWidget(PCM_viewer)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox_mask_gen_angle_meaning = QComboBox(self.tab_2)
        self.comboBox_mask_gen_angle_meaning.setObjectName(u"comboBox_mask_gen_angle_meaning")
        self.comboBox_mask_gen_angle_meaning.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_mask_gen_angle_meaning)

        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.comboBox_sum_type = QComboBox(self.tab_2)
        self.comboBox_sum_type.setObjectName(u"comboBox_sum_type")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_sum_type)

        self.pushButton_plot_cumsum = QPushButton(self.tab_2)
        self.pushButton_plot_cumsum.setObjectName(u"pushButton_plot_cumsum")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_plot_cumsum)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.sum_vs_mask_angle_widget = SumVSMaskAngleWidget(self.tab_2)
        self.sum_vs_mask_angle_widget.setObjectName(u"sum_vs_mask_angle_widget")
        sizePolicy.setHeightForWidth(self.sum_vs_mask_angle_widget.sizePolicy().hasHeightForWidth())
        self.sum_vs_mask_angle_widget.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.sum_vs_mask_angle_widget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_phasor_scheme = QLabel(self.tab)
        self.label_phasor_scheme.setObjectName(u"label_phasor_scheme")

        self.horizontalLayout_3.addWidget(self.label_phasor_scheme)

        self.comboBox_phasor_schemes = QComboBox(self.tab)
        self.comboBox_phasor_schemes.setObjectName(u"comboBox_phasor_schemes")
        self.comboBox_phasor_schemes.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_phasor_schemes)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_re_calc_phasor = QPushButton(self.tab)
        self.pushButton_re_calc_phasor.setObjectName(u"pushButton_re_calc_phasor")

        self.horizontalLayout_3.addWidget(self.pushButton_re_calc_phasor)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.phasor_plot_widget = PhasorPlotWidget(self.tab)
        self.phasor_plot_widget.setObjectName(u"phasor_plot_widget")
        sizePolicy.setHeightForWidth(self.phasor_plot_widget.sizePolicy().hasHeightForWidth())
        self.phasor_plot_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.phasor_plot_widget)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(PCM_viewer)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PCM_viewer)
    # setupUi

    def retranslateUi(self, PCM_viewer):
        PCM_viewer.setWindowTitle(QCoreApplication.translate("PCM_viewer", u"Pixel contributions matrix viewer", None))
        self.checkBox_real.setText(QCoreApplication.translate("PCM_viewer", u"Real", None))
        self.checkBox_imag.setText(QCoreApplication.translate("PCM_viewer", u"Imag", None))
        self.check_box_crit.setText(QCoreApplication.translate("PCM_viewer", u"Critical angle", None))
        self.check_box_sign.setText(QCoreApplication.translate("PCM_viewer", u"Sign +/-", None))
        self.label.setText(QCoreApplication.translate("PCM_viewer", u"Mask gen angle meaning :", None))
        self.label_2.setText(QCoreApplication.translate("PCM_viewer", u"Sum type :", None))
        self.pushButton_plot_cumsum.setText(QCoreApplication.translate("PCM_viewer", u"Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("PCM_viewer", u"Sum vs mask gen angle", None))
        self.label_phasor_scheme.setText(QCoreApplication.translate("PCM_viewer", u"Phasor scheme :", None))
        self.pushButton_re_calc_phasor.setText(QCoreApplication.translate("PCM_viewer", u"Plot Phasor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("PCM_viewer", u"Phasor", None))
    # retranslateUi


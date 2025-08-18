# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chorusmainui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

from classdefs.modbscanviewwidget import BScanViewWidget
from classdefs.modisotimeplotwidget import IsoTimePlotWidget
from classdefs.modtfmimagewidget2d import TFMImageWidget2D

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1438, 805)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.four_views_widget = QWidget(self.centralwidget)
        self.four_views_widget.setObjectName(u"four_views_widget")
        self.gridLayout = QGridLayout(self.four_views_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_tfm = QFrame(self.four_views_widget)
        self.frame_tfm.setObjectName(u"frame_tfm")
        self.frame_tfm.setFrameShape(QFrame.StyledPanel)
        self.frame_tfm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tfm)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 6, 0)
        self.widget_4 = QWidget(self.frame_tfm)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 6)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(160, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_delete_tfm_image = QPushButton(self.widget_5)
        self.pushButton_delete_tfm_image.setObjectName(u"pushButton_delete_tfm_image")
        self.pushButton_delete_tfm_image.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_delete_tfm_image)

        self.pushButton_add_tfm_image = QPushButton(self.widget_5)
        self.pushButton_add_tfm_image.setObjectName(u"pushButton_add_tfm_image")
        self.pushButton_add_tfm_image.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_add_tfm_image)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.listView_tfm_images = QListView(self.widget_4)
        self.listView_tfm_images.setObjectName(u"listView_tfm_images")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_tfm_images.sizePolicy().hasHeightForWidth())
        self.listView_tfm_images.setSizePolicy(sizePolicy)
        self.listView_tfm_images.setMaximumSize(QSize(160, 16777215))
        self.listView_tfm_images.setBaseSize(QSize(160, 0))

        self.verticalLayout_2.addWidget(self.listView_tfm_images)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.tfm_image_widget_2D = TFMImageWidget2D(self.frame_tfm)
        self.tfm_image_widget_2D.setObjectName(u"tfm_image_widget_2D")

        self.horizontalLayout_2.addWidget(self.tfm_image_widget_2D)


        self.gridLayout.addWidget(self.frame_tfm, 0, 0, 1, 1)

        self.b_scan_view_widget_iso_gen = BScanViewWidget(self.four_views_widget)
        self.b_scan_view_widget_iso_gen.setObjectName(u"b_scan_view_widget_iso_gen")

        self.gridLayout.addWidget(self.b_scan_view_widget_iso_gen, 1, 0, 1, 1)

        self.b_scan_view_widget_iso_det = BScanViewWidget(self.four_views_widget)
        self.b_scan_view_widget_iso_det.setObjectName(u"b_scan_view_widget_iso_det")

        self.gridLayout.addWidget(self.b_scan_view_widget_iso_det, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.four_views_widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.iso_time_plot_widget = IsoTimePlotWidget(self.widget_6)
        self.iso_time_plot_widget.setObjectName(u"iso_time_plot_widget")

        self.horizontalLayout_4.addWidget(self.iso_time_plot_widget)

        self.frame_2 = QFrame(self.widget_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.pushButton_display_unfiltered = QPushButton(self.widget_2)
        self.pushButton_display_unfiltered.setObjectName(u"pushButton_display_unfiltered")
        self.pushButton_display_unfiltered.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_display_unfiltered)

        self.groupBox = QGroupBox(self.widget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.doubleSpinBox_colormap_max_abs_pm = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_colormap_max_abs_pm.setObjectName(u"doubleSpinBox_colormap_max_abs_pm")
        self.doubleSpinBox_colormap_max_abs_pm.setMinimum(0.000000000000000)
        self.doubleSpinBox_colormap_max_abs_pm.setMaximum(1000000.000000000000000)
        self.doubleSpinBox_colormap_max_abs_pm.setSingleStep(1.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_colormap_max_abs_pm, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label_gen_index = QLabel(self.widget)
        self.label_gen_index.setObjectName(u"label_gen_index")
        self.label_gen_index.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_gen_index, 0, 3, 1, 1)

        self.slider_det_index = QSlider(self.widget)
        self.slider_det_index.setObjectName(u"slider_det_index")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider_det_index.sizePolicy().hasHeightForWidth())
        self.slider_det_index.setSizePolicy(sizePolicy1)
        self.slider_det_index.setLayoutDirection(Qt.LeftToRight)
        self.slider_det_index.setMaximum(1000)
        self.slider_det_index.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.slider_det_index, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.slider_time_index = QSlider(self.widget)
        self.slider_time_index.setObjectName(u"slider_time_index")
        sizePolicy1.setHeightForWidth(self.slider_time_index.sizePolicy().hasHeightForWidth())
        self.slider_time_index.setSizePolicy(sizePolicy1)
        self.slider_time_index.setOrientation(Qt.Vertical)
        self.slider_time_index.setInvertedAppearance(True)

        self.gridLayout_2.addWidget(self.slider_time_index, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_det_index = QLabel(self.widget)
        self.label_det_index.setObjectName(u"label_det_index")
        self.label_det_index.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_det_index, 0, 1, 1, 1)

        self.slider_gen_index = QSlider(self.widget)
        self.slider_gen_index.setObjectName(u"slider_gen_index")
        sizePolicy1.setHeightForWidth(self.slider_gen_index.sizePolicy().hasHeightForWidth())
        self.slider_gen_index.setSizePolicy(sizePolicy1)
        self.slider_gen_index.setMaximum(1000)
        self.slider_gen_index.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.slider_gen_index, 2, 3, 1, 1, Qt.AlignHCenter)

        self.spinBox_det_index = QSpinBox(self.widget)
        self.spinBox_det_index.setObjectName(u"spinBox_det_index")
        self.spinBox_det_index.setMaximum(1000)

        self.gridLayout_2.addWidget(self.spinBox_det_index, 1, 1, 1, 1)

        self.spinBox_gen_index = QSpinBox(self.widget)
        self.spinBox_gen_index.setObjectName(u"spinBox_gen_index")
        self.spinBox_gen_index.setMaximum(1000)

        self.gridLayout_2.addWidget(self.spinBox_gen_index, 1, 3, 1, 1)

        self.doubleSpinBox_time_us = QDoubleSpinBox(self.widget)
        self.doubleSpinBox_time_us.setObjectName(u"doubleSpinBox_time_us")
        self.doubleSpinBox_time_us.setReadOnly(False)
        self.doubleSpinBox_time_us.setMinimum(-99.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_time_us, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.widget_6, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.four_views_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1438, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TFM images :", None))
        self.pushButton_delete_tfm_image.setText("")
        self.pushButton_add_tfm_image.setText("")
        self.pushButton_display_unfiltered.setText(QCoreApplication.translate("MainWindow", u"Display unfiltered", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Colormap limits (pm) : ", None))
        self.doubleSpinBox_colormap_max_abs_pm.setSuffix(QCoreApplication.translate("MainWindow", u"pm", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Max Abs :", None))
        self.label_gen_index.setText(QCoreApplication.translate("MainWindow", u"Gen :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.label_det_index.setText(QCoreApplication.translate("MainWindow", u"Det :", None))
#if QT_CONFIG(tooltip)
        self.spinBox_det_index.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Detection index used </p><p>for iso-detection B-scan</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBox_gen_index.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Generation index used </p><p>for iso-generation B-scan</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.doubleSpinBox_time_us.setSuffix(QCoreApplication.translate("MainWindow", u"\u03bcs", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


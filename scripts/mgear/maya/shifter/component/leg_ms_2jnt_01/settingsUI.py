# MGEAR is under the terms of the MIT License

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
# Date:       2016 / 10 / 10
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(255, 709)
        self.ikRefArray_groupBox = QtGui.QGroupBox(Form)
        self.ikRefArray_groupBox.setGeometry(QtCore.QRect(0, 330, 249, 169))
        self.ikRefArray_groupBox.setObjectName("ikRefArray_groupBox")
        self.layoutWidget = QtGui.QWidget(self.ikRefArray_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.ikRefArray_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.ikRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ikRefArray_horizontalLayout.setObjectName("ikRefArray_horizontalLayout")
        self.ikRefArray_verticalLayout_1 = QtGui.QVBoxLayout()
        self.ikRefArray_verticalLayout_1.setObjectName("ikRefArray_verticalLayout_1")
        self.ikRefArray_listWidget = QtGui.QListWidget(self.layoutWidget)
        self.ikRefArray_listWidget.setDragDropOverwriteMode(True)
        self.ikRefArray_listWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.ikRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ikRefArray_listWidget.setAlternatingRowColors(True)
        self.ikRefArray_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ikRefArray_listWidget.setSelectionRectVisible(False)
        self.ikRefArray_listWidget.setObjectName("ikRefArray_listWidget")
        self.ikRefArray_verticalLayout_1.addWidget(self.ikRefArray_listWidget)
        self.ikRefArray_copyRef_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.ikRefArray_copyRef_pushButton.setObjectName("ikRefArray_copyRef_pushButton")
        self.ikRefArray_verticalLayout_1.addWidget(self.ikRefArray_copyRef_pushButton)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_1)
        self.ikRefArray_verticalLayout_2 = QtGui.QVBoxLayout()
        self.ikRefArray_verticalLayout_2.setObjectName("ikRefArray_verticalLayout_2")
        self.ikRefArrayAdd_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.ikRefArrayAdd_pushButton.setObjectName("ikRefArrayAdd_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayAdd_pushButton)
        self.ikRefArrayRemove_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.ikRefArrayRemove_pushButton.setObjectName("ikRefArrayRemove_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayRemove_pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.ikRefArray_verticalLayout_2.addItem(spacerItem)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_2)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 1, 249, 161))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 10, 231, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.ikfk_label = QtGui.QLabel(self.layoutWidget1)
        self.ikfk_label.setObjectName("ikfk_label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ikfk_label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ikfk_slider = QtGui.QSlider(self.layoutWidget1)
        self.ikfk_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.ikfk_slider.setMaximum(100)
        self.ikfk_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ikfk_slider.setObjectName("ikfk_slider")
        self.horizontalLayout_3.addWidget(self.ikfk_slider)
        self.ikfk_spinBox = QtGui.QSpinBox(self.layoutWidget1)
        self.ikfk_spinBox.setMaximum(100)
        self.ikfk_spinBox.setObjectName("ikfk_spinBox")
        self.horizontalLayout_3.addWidget(self.ikfk_spinBox)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.maxStretch_label = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_label.sizePolicy().hasHeightForWidth())
        self.maxStretch_label.setSizePolicy(sizePolicy)
        self.maxStretch_label.setObjectName("maxStretch_label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.maxStretch_label)
        self.maxStretch_spinBox = QtGui.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_spinBox.sizePolicy().hasHeightForWidth())
        self.maxStretch_spinBox.setSizePolicy(sizePolicy)
        self.maxStretch_spinBox.setMinimum(1.0)
        self.maxStretch_spinBox.setSingleStep(0.5)
        self.maxStretch_spinBox.setProperty("value", 2.0)
        self.maxStretch_spinBox.setObjectName("maxStretch_spinBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.maxStretch_spinBox)
        self.knee_spinBox = QtGui.QDoubleSpinBox(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knee_spinBox.sizePolicy().hasHeightForWidth())
        self.knee_spinBox.setSizePolicy(sizePolicy)
        self.knee_spinBox.setMinimum(0.0)
        self.knee_spinBox.setSingleStep(0.1)
        self.knee_spinBox.setProperty("value", 0.0)
        self.knee_spinBox.setObjectName("knee_spinBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.knee_spinBox)
        self.knee_label = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knee_label.sizePolicy().hasHeightForWidth())
        self.knee_label.setSizePolicy(sizePolicy)
        self.knee_label.setObjectName("knee_label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.knee_label)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.divisions_label = QtGui.QLabel(self.layoutWidget1)
        self.divisions_label.setObjectName("divisions_label")
        self.horizontalLayout.addWidget(self.divisions_label)
        self.div0_spinBox = QtGui.QSpinBox(self.layoutWidget1)
        self.div0_spinBox.setMinimum(1)
        self.div0_spinBox.setProperty("value", 3)
        self.div0_spinBox.setObjectName("div0_spinBox")
        self.horizontalLayout.addWidget(self.div0_spinBox)
        self.div1_spinBox = QtGui.QSpinBox(self.layoutWidget1)
        self.div1_spinBox.setMinimum(1)
        self.div1_spinBox.setProperty("value", 3)
        self.div1_spinBox.setObjectName("div1_spinBox")
        self.horizontalLayout.addWidget(self.div1_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 130, 229, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.squashStretchProfile_pushButton = QtGui.QPushButton(self.layoutWidget2)
        self.squashStretchProfile_pushButton.setObjectName("squashStretchProfile_pushButton")
        self.horizontalLayout_2.addWidget(self.squashStretchProfile_pushButton)
        self.upvRefArray_groupBox = QtGui.QGroupBox(Form)
        self.upvRefArray_groupBox.setGeometry(QtCore.QRect(0, 500, 249, 170))
        self.upvRefArray_groupBox.setObjectName("upvRefArray_groupBox")
        self.layoutWidget_2 = QtGui.QWidget(self.upvRefArray_groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.upvRefArray_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.upvRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.upvRefArray_horizontalLayout.setObjectName("upvRefArray_horizontalLayout")
        self.upvRefArray_verticalLayout_1 = QtGui.QVBoxLayout()
        self.upvRefArray_verticalLayout_1.setObjectName("upvRefArray_verticalLayout_1")
        self.upvRefArray_listWidget = QtGui.QListWidget(self.layoutWidget_2)
        self.upvRefArray_listWidget.setDragDropOverwriteMode(True)
        self.upvRefArray_listWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.upvRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.upvRefArray_listWidget.setAlternatingRowColors(True)
        self.upvRefArray_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.upvRefArray_listWidget.setSelectionRectVisible(False)
        self.upvRefArray_listWidget.setObjectName("upvRefArray_listWidget")
        self.upvRefArray_verticalLayout_1.addWidget(self.upvRefArray_listWidget)
        self.upvRefArray_copyRef_pushButton = QtGui.QPushButton(self.layoutWidget_2)
        self.upvRefArray_copyRef_pushButton.setObjectName("upvRefArray_copyRef_pushButton")
        self.upvRefArray_verticalLayout_1.addWidget(self.upvRefArray_copyRef_pushButton)
        self.upvRefArray_horizontalLayout.addLayout(self.upvRefArray_verticalLayout_1)
        self.upvRefArray_verticalLayout_2 = QtGui.QVBoxLayout()
        self.upvRefArray_verticalLayout_2.setObjectName("upvRefArray_verticalLayout_2")
        self.upvRefArrayAdd_pushButton = QtGui.QPushButton(self.layoutWidget_2)
        self.upvRefArrayAdd_pushButton.setObjectName("upvRefArrayAdd_pushButton")
        self.upvRefArray_verticalLayout_2.addWidget(self.upvRefArrayAdd_pushButton)
        self.upvRefArrayRemove_pushButton = QtGui.QPushButton(self.layoutWidget_2)
        self.upvRefArrayRemove_pushButton.setObjectName("upvRefArrayRemove_pushButton")
        self.upvRefArray_verticalLayout_2.addWidget(self.upvRefArrayRemove_pushButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.upvRefArray_verticalLayout_2.addItem(spacerItem1)
        self.upvRefArray_horizontalLayout.addLayout(self.upvRefArray_verticalLayout_2)
        self.fkRefArray_groupBox = QtGui.QGroupBox(Form)
        self.fkRefArray_groupBox.setGeometry(QtCore.QRect(0, 160, 249, 169))
        self.fkRefArray_groupBox.setObjectName("fkRefArray_groupBox")
        self.layoutWidget_3 = QtGui.QWidget(self.fkRefArray_groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.fkRefArray_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.fkRefArray_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fkRefArray_horizontalLayout.setObjectName("fkRefArray_horizontalLayout")
        self.fkRefArray_verticalLayout_1 = QtGui.QVBoxLayout()
        self.fkRefArray_verticalLayout_1.setObjectName("fkRefArray_verticalLayout_1")
        self.fkRefArray_listWidget = QtGui.QListWidget(self.layoutWidget_3)
        self.fkRefArray_listWidget.setDragDropOverwriteMode(True)
        self.fkRefArray_listWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.fkRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.fkRefArray_listWidget.setAlternatingRowColors(True)
        self.fkRefArray_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fkRefArray_listWidget.setSelectionRectVisible(False)
        self.fkRefArray_listWidget.setObjectName("fkRefArray_listWidget")
        self.fkRefArray_verticalLayout_1.addWidget(self.fkRefArray_listWidget)
        self.fkRefArray_copyRef_pushButton = QtGui.QPushButton(self.layoutWidget_3)
        self.fkRefArray_copyRef_pushButton.setObjectName("fkRefArray_copyRef_pushButton")
        self.fkRefArray_verticalLayout_1.addWidget(self.fkRefArray_copyRef_pushButton)
        self.fkRefArray_horizontalLayout.addLayout(self.fkRefArray_verticalLayout_1)
        self.fkRefArray_verticalLayout_2 = QtGui.QVBoxLayout()
        self.fkRefArray_verticalLayout_2.setObjectName("fkRefArray_verticalLayout_2")
        self.fkRefArrayAdd_pushButton = QtGui.QPushButton(self.layoutWidget_3)
        self.fkRefArrayAdd_pushButton.setObjectName("fkRefArrayAdd_pushButton")
        self.fkRefArray_verticalLayout_2.addWidget(self.fkRefArrayAdd_pushButton)
        self.fkRefArrayRemove_pushButton = QtGui.QPushButton(self.layoutWidget_3)
        self.fkRefArrayRemove_pushButton.setObjectName("fkRefArrayRemove_pushButton")
        self.fkRefArray_verticalLayout_2.addWidget(self.fkRefArrayRemove_pushButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.fkRefArray_verticalLayout_2.addItem(spacerItem2)
        self.fkRefArray_horizontalLayout.addLayout(self.fkRefArray_verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ikfk_slider, QtCore.SIGNAL("sliderMoved(int)"), self.ikfk_spinBox.setValue)
        QtCore.QObject.connect(self.ikfk_spinBox, QtCore.SIGNAL("valueChanged(int)"), self.ikfk_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.ikRefArray_groupBox.setTitle(QtGui.QApplication.translate("Form", "IK Reference Array", None, QtGui.QApplication.UnicodeUTF8))
        self.ikRefArray_copyRef_pushButton.setText(QtGui.QApplication.translate("Form", "Copy from UpV Ref", None, QtGui.QApplication.UnicodeUTF8))
        self.ikRefArrayAdd_pushButton.setText(QtGui.QApplication.translate("Form", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.ikRefArrayRemove_pushButton.setText(QtGui.QApplication.translate("Form", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.ikfk_label.setText(QtGui.QApplication.translate("Form", "FK/IK Blend", None, QtGui.QApplication.UnicodeUTF8))
        self.maxStretch_label.setText(QtGui.QApplication.translate("Form", "Max Stretch", None, QtGui.QApplication.UnicodeUTF8))
        self.knee_label.setText(QtGui.QApplication.translate("Form", "Knee Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.divisions_label.setText(QtGui.QApplication.translate("Form", "Divisions", None, QtGui.QApplication.UnicodeUTF8))
        self.squashStretchProfile_pushButton.setText(QtGui.QApplication.translate("Form", "Squash and Stretch Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.upvRefArray_groupBox.setTitle(QtGui.QApplication.translate("Form", "UpV Reference Array", None, QtGui.QApplication.UnicodeUTF8))
        self.upvRefArray_copyRef_pushButton.setText(QtGui.QApplication.translate("Form", "Copy from IK Ref", None, QtGui.QApplication.UnicodeUTF8))
        self.upvRefArrayAdd_pushButton.setText(QtGui.QApplication.translate("Form", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.upvRefArrayRemove_pushButton.setText(QtGui.QApplication.translate("Form", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.fkRefArray_groupBox.setTitle(QtGui.QApplication.translate("Form", "FK Reference Array", None, QtGui.QApplication.UnicodeUTF8))
        self.fkRefArray_copyRef_pushButton.setText(QtGui.QApplication.translate("Form", "Copy from IK Ref", None, QtGui.QApplication.UnicodeUTF8))
        self.fkRefArrayAdd_pushButton.setText(QtGui.QApplication.translate("Form", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.fkRefArrayRemove_pushButton.setText(QtGui.QApplication.translate("Form", ">>", None, QtGui.QApplication.UnicodeUTF8))


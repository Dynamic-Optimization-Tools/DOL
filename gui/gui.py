import sys

from src.opt import opt
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.mplwidget import MplWidget
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class params:
    a = None
    b = None
    c = None
    d = None
    r = None
    left_bound = None
    right_bound = None
    max_iter = None
    method = None
    accuracy = None

    def __init__(self, a=1, b=1, c=1, d=1, r=2, left_bound=0 , right_bound=10, max_iter=100, accuracy=0.01):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.r = r
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.max_iter = max_iter
        self.accuracy = accuracy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 740)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout.addWidget(self.MplWidget, 0, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.solutionX = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.solutionX.setFont(font)
        self.solutionX.setObjectName("solutionX")
        self.verticalLayout.addWidget(self.solutionX)
        self.solutionY = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.solutionY.setFont(font)
        self.solutionY.setObjectName("solutionY")
        self.verticalLayout.addWidget(self.solutionY)
        self.solutionIterCount = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.solutionIterCount.setFont(font)
        self.solutionIterCount.setObjectName("solutionIterCount")
        self.verticalLayout.addWidget(self.solutionIterCount)
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.verticalLayout.addWidget(self.pushButtonClear)
        self.pushButtonCalculate = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.verticalLayout.addWidget(self.pushButtonCalculate)
        self.gridLayout.addWidget(self.groupBox_2, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.funcParamA = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamA.setObjectName("funcParamA")
        self.horizontalLayout_2.addWidget(self.funcParamA)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.funcParamB = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamB.setObjectName("funcParamB")
        self.horizontalLayout_2.addWidget(self.funcParamB)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.funcParamC = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamC.setObjectName("funcParamC")
        self.horizontalLayout_2.addWidget(self.funcParamC)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.funcParamD = QtWidgets.QLineEdit(self.groupBox_5)
        self.funcParamD.setObjectName("funcParamD")
        self.horizontalLayout_2.addWidget(self.funcParamD)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.funcParamLeftB = QtWidgets.QLineEdit(self.groupBox_6)
        self.funcParamLeftB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.funcParamLeftB.setObjectName("funcParamLeftB")
        self.horizontalLayout_3.addWidget(self.funcParamLeftB)
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.funcParamRightB = QtWidgets.QLineEdit(self.groupBox_6)
        self.funcParamRightB.setMaximumSize(QtCore.QSize(100, 16777215))
        self.funcParamRightB.setObjectName("funcParamRightB")
        self.horizontalLayout_3.addWidget(self.funcParamRightB)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonPiyavsky = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButtonPiyavsky.setFont(font)
        self.radioButtonPiyavsky.setObjectName("radioButtonPiyavsky")
        self.verticalLayout_2.addWidget(self.radioButtonPiyavsky)
        self.radioButtonStrongin = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButtonStrongin.setFont(font)
        self.radioButtonStrongin.setObjectName("radioButtonStrongin")
        self.verticalLayout_2.addWidget(self.radioButtonStrongin)
        self.radioButtonBrutforce = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButtonBrutforce.setFont(font)
        self.radioButtonBrutforce.setObjectName("radioButtonBrutforce")
        self.verticalLayout_2.addWidget(self.radioButtonBrutforce)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelR = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelR.setFont(font)
        self.labelR.setObjectName("labelR")
        self.horizontalLayout.addWidget(self.labelR)
        self.r = QtWidgets.QLineEdit(self.groupBox_4)
        self.r.setObjectName("r")
        self.horizontalLayout.addWidget(self.r)
        self.labelIter = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelIter.setFont(font)
        self.labelIter.setObjectName("labelIter")
        self.horizontalLayout.addWidget(self.labelIter)
        self.maxIterCount = QtWidgets.QLineEdit(self.groupBox_4)
        self.maxIterCount.setObjectName("maxIterCount")
        self.horizontalLayout.addWidget(self.maxIterCount)
        self.labelacc = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelacc.setFont(font)
        self.labelacc.setObjectName("labelacc")
        self.horizontalLayout.addWidget(self.labelacc)
        self.accuracy = QtWidgets.QLineEdit(self.groupBox_4)
        self.accuracy.setObjectName("accuracy")
        self.horizontalLayout.addWidget(self.accuracy)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButtonClear.clicked.connect(self.ClearPlot)
        self.pushButtonCalculate.clicked.connect(self.DisplaySolution)
        MainWindow.addToolBar(NavigationToolbar(self.MplWidget.canvas, MainWindow))
        self.initInputContainers()
        self.retranslateUi(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная. Кутовой Вадим 381606-1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Решение"))
        self.solutionX.setText(_translate("MainWindow", "x"))
        self.solutionY.setText(_translate("MainWindow", "y"))
        self.solutionIterCount.setText(_translate("MainWindow", "iter"))
        self.pushButtonClear.setText(_translate("MainWindow", "Сброс"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Поиск"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Функция"))
        self.label_4.setText(_translate("MainWindow", "F(x) ="))
        self.label_5.setText(_translate("MainWindow", "* sin("))
        self.label_6.setText(_translate("MainWindow", " B * x ) + "))
        self.label_8.setText(_translate("MainWindow", " * cos("))
        self.label_9.setText(_translate("MainWindow", "* x)"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Интервал поиска"))
        self.label_7.setText(_translate("MainWindow", "Левая граница"))
        self.label_10.setText(_translate("MainWindow", "Правая граница"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Методы"))
        self.radioButtonPiyavsky.setText(_translate("MainWindow", "Метод Пиявского"))
        self.radioButtonStrongin.setText(_translate("MainWindow", "Метод Стронгина"))
        self.radioButtonBrutforce.setText(_translate("MainWindow", "Метод перебора"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Дополнительные параметры"))
        self.labelR.setText(_translate("MainWindow", "Коэффициент надежности"))
        self.labelIter.setText(_translate("MainWindow", "Максимальное число итераций"))
        self.labelacc.setText(_translate("MainWindow", "Точность"))

    def initInputContainers(self):
        default_params = params()
        self.funcParamA.setText(str(default_params.a))
        self.funcParamB.setText(str(default_params.b))
        self.funcParamC.setText(str(default_params.c))
        self.funcParamD.setText(str(default_params.d))
        self.funcParamLeftB.setText(str(default_params.left_bound))
        self.funcParamRightB.setText(str(default_params.right_bound))
        self.r.setText(str(default_params.r))
        self.maxIterCount.setText(str(default_params.max_iter))
        self.accuracy.setText(str(default_params.accuracy))
        self.radioButtonPiyavsky.setChecked(True)

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def ClearPlot(self):
        self.solutionX.setText("")
        self.solutionY.setText("")
        self.solutionIterCount.setText("")
        self.MplWidget.canvas.axes.cla()
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()

    def DisplaySolution(self):
        optimizer = opt()
        opt_params = params()

        opt_params.a = float(self.funcParamA.text())
        opt_params.b = float(self.funcParamB.text())
        opt_params.c = float(self.funcParamC.text())
        opt_params.d = float(self.funcParamD.text())
        opt_params.left_bound = float(self.funcParamLeftB.text())
        opt_params.right_bound = float(self.funcParamRightB.text())
        opt_params.max_iter = int(self.maxIterCount.text())
        opt_params.accuracy = float(self.accuracy.text())
        opt_params.r = float(self.r.text())

        if self.radioButtonBrutforce.isChecked():
            opt_params.method = optimizer.methods.BruteForse
        elif self.radioButtonPiyavsky.isChecked():
            opt_params.method = optimizer.methods.Piyavsky
        elif self.radioButtonStrongin.isChecked():
            opt_params.method = optimizer.methods.Strongin

        for param in dir(opt_params):
            if "__" not in param:
                print(param, "=", getattr(opt_params, param), type(getattr(opt_params, param)))

        optimizer.SetFunctionParameters(opt_params.a, opt_params.b, opt_params.c, opt_params.d)
        solution = optimizer.Minimize(opt_params.left_bound, opt_params.right_bound, opt_params.r, opt_params.method, max_iter=opt_params.max_iter, eps=opt_params.accuracy)

        points_multiplier = 100
        num_points = int(abs(opt_params.right_bound - opt_params.left_bound) * points_multiplier)
        step = abs(opt_params.right_bound - opt_params.left_bound)/num_points

        x = []
        for i in range(num_points):
            x.append(i * step + opt_params.left_bound)

        y = [optimizer.Func(point) for point in x]

        self.MplWidget.canvas.axes.plot(x, y)
        
        for point in solution.points:
            self.MplWidget.canvas.axes.plot(point[0], solution.minimum[1] - 0.1, color="green", marker="*")

        self.MplWidget.canvas.axes.plot(solution.minimum[0], solution.minimum[1], color="red", marker="o")
        self.solutionX.setText("x = " + str(round(solution.minimum[0], 7)))
        self.solutionY.setText("y = " + str(round(solution.minimum[1], 7)))
        self.solutionIterCount.setText("Количество итераций : " + str(solution.spent_iter))

        self.MplWidget.canvas.draw()

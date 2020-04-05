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

    def __init__(self, a=1, b=1, c=1, d=1, r=2, left_bound=0 , right_bound=10, max_iter=100):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.r = r
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.max_iter = max_iter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 541, 551))
        self.groupBox.setObjectName("groupBox")
        self.labelFunc = QtWidgets.QLabel(self.groupBox)
        self.labelFunc.setGeometry(QtCore.QRect(30, 30, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelFunc.setFont(font)
        self.labelFunc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelFunc.setObjectName("labelFunc")
        self.funcParamA = QtWidgets.QPlainTextEdit(self.groupBox)
        self.funcParamA.setGeometry(QtCore.QRect(90, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.funcParamA.setFont(font)
        self.funcParamA.setObjectName("funcParamA")
        self.funcParamB = QtWidgets.QPlainTextEdit(self.groupBox)
        self.funcParamB.setGeometry(QtCore.QRect(190, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.funcParamB.setFont(font)
        self.funcParamB.setObjectName("funcParamB")
        self.funcParamC = QtWidgets.QPlainTextEdit(self.groupBox)
        self.funcParamC.setGeometry(QtCore.QRect(290, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.funcParamC.setFont(font)
        self.funcParamC.setObjectName("funcParamC")
        self.funcParamD = QtWidgets.QPlainTextEdit(self.groupBox)
        self.funcParamD.setGeometry(QtCore.QRect(400, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.funcParamD.setFont(font)
        self.funcParamD.setObjectName("funcParamD")
        self.labelIter = QtWidgets.QLabel(self.groupBox)
        self.labelIter.setGeometry(QtCore.QRect(70, 160, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelIter.setFont(font)
        self.labelIter.setObjectName("labelIter")
        self.maxIterCount = QtWidgets.QPlainTextEdit(self.groupBox)
        self.maxIterCount.setGeometry(QtCore.QRect(300, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.maxIterCount.setFont(font)
        self.maxIterCount.setObjectName("maxIterCount")
        self.labelInterval = QtWidgets.QLabel(self.groupBox)
        self.labelInterval.setGeometry(QtCore.QRect(70, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.labelInterval.setFont(font)
        self.labelInterval.setObjectName("labelInterval")
        self.funcParamRightB = QtWidgets.QPlainTextEdit(self.groupBox)
        self.funcParamRightB.setGeometry(QtCore.QRect(170, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.funcParamRightB.setFont(font)
        self.funcParamRightB.setObjectName("funcParamRightB")
        self.funcParamLeftB = QtWidgets.QPlainTextEdit(self.groupBox)
        self.funcParamLeftB.setGeometry(QtCore.QRect(120, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.funcParamLeftB.setFont(font)
        self.funcParamLeftB.setObjectName("funcParamLeftB")
        self.r = QtWidgets.QPlainTextEdit(self.groupBox)
        self.r.setGeometry(QtCore.QRect(300, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.r.setFont(font)
        self.r.setObjectName("r")
        self.labelR = QtWidgets.QLabel(self.groupBox)
        self.labelR.setGeometry(QtCore.QRect(70, 200, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelR.setFont(font)
        self.labelR.setObjectName("labelR")
        self.radioButtonPiyavsky = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonPiyavsky.setGeometry(QtCore.QRect(80, 240, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButtonPiyavsky.setFont(font)
        self.radioButtonPiyavsky.setObjectName("radioButtonPiyavsky")
        self.radioButtonStrongin = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonStrongin.setGeometry(QtCore.QRect(80, 260, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButtonStrongin.setFont(font)
        self.radioButtonStrongin.setObjectName("radioButtonStrongin")
        self.radioButtonBrutforce = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonBrutforce.setGeometry(QtCore.QRect(80, 280, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioButtonBrutforce.setFont(font)
        self.radioButtonBrutforce.setObjectName("radioButtonBrutforce")
        self.pushButtonCalculate = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(360, 480, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButtonCalculate.setFont(font)
        self.pushButtonCalculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.solutionX = QtWidgets.QLabel(self.groupBox)
        self.solutionX.setGeometry(QtCore.QRect(360, 350, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.solutionX.setFont(font)
        self.solutionX.setText("")
        self.solutionX.setObjectName("solutionX")
        self.solutionY = QtWidgets.QLabel(self.groupBox)
        self.solutionY.setGeometry(QtCore.QRect(360, 380, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.solutionY.setFont(font)
        self.solutionY.setText("")
        self.solutionY.setObjectName("solutionY")
        self.labelInterval.raise_()
        self.labelFunc.raise_()
        self.funcParamA.raise_()
        self.funcParamB.raise_()
        self.funcParamC.raise_()
        self.funcParamD.raise_()
        self.labelIter.raise_()
        self.maxIterCount.raise_()
        self.funcParamRightB.raise_()
        self.funcParamLeftB.raise_()
        self.r.raise_()
        self.labelR.raise_()
        self.radioButtonPiyavsky.raise_()
        self.radioButtonStrongin.raise_()
        self.radioButtonBrutforce.raise_()
        self.pushButtonCalculate.raise_()
        self.solutionX.raise_()
        self.solutionY.raise_()
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(580, 20, 511, 541))
        self.MplWidget.setObjectName("MplWidget")
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClear.setGeometry(QtCore.QRect(200, 480, 161, 61))
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.pushButtonClear.raise_()
        self.pushButtonClear.clicked.connect(self.ClearPlot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButtonCalculate.clicked.connect(self.DisplaySolution)
        MainWindow.addToolBar(NavigationToolbar(self.MplWidget.canvas, MainWindow))
        self.initInputContainers()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dynamic optimisation tool"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры"))
        self.labelFunc.setText(_translate("MainWindow", "f(x) =     * sin(      * x) +      * cos(      * x)"))
        self.labelIter.setText(_translate("MainWindow", "Максимальное число итераций"))
        self.labelInterval.setText(_translate("MainWindow", "x ∈[      ;     ]"))
        self.labelR.setText(_translate("MainWindow", "Коэффициент надежности"))
        self.radioButtonPiyavsky.setText(_translate("MainWindow", "Метод Пиявского"))
        self.radioButtonStrongin.setText(_translate("MainWindow", "Метод Стронгина"))
        self.radioButtonBrutforce.setText(_translate("MainWindow", "Метод перебора"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Вычислить"))
        self.pushButtonClear.setText(_translate("MainWindow", "Очистить"))

    def initInputContainers(self):
        default_params = params()
        self.funcParamA.setPlainText(str(default_params.a))
        self.funcParamB.setPlainText(str(default_params.b))
        self.funcParamC.setPlainText(str(default_params.c))
        self.funcParamD.setPlainText(str(default_params.d))
        self.funcParamLeftB.setPlainText(str(default_params.left_bound))
        self.funcParamRightB.setPlainText(str(default_params.right_bound))
        self.r.setPlainText(str(default_params.r))
        self.maxIterCount.setPlainText(str(default_params.max_iter))
        self.radioButtonPiyavsky.setChecked(True)

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def ClearPlot(self):
        self.MplWidget.canvas.axes.cla()
        self.MplWidget.canvas.axes.clear()

    def DisplaySolution(self):
        optimizer = opt()
        opt_params = params()

        opt_params.a = float(self.funcParamA.toPlainText())
        opt_params.b = float(self.funcParamB.toPlainText())
        opt_params.c = float(self.funcParamC.toPlainText())
        opt_params.d = float(self.funcParamD.toPlainText())
        opt_params.left_bound = float(self.funcParamLeftB.toPlainText())
        opt_params.right_bound = float(self.funcParamRightB.toPlainText())
        opt_params.max_iter = int(self.maxIterCount.toPlainText())
        opt_params.r = float(self.r.toPlainText())

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
        solution = optimizer.Minimize(opt_params.left_bound, opt_params.right_bound, opt_params.r, opt_params.method, max_iter=params.max_iter)

        points_multiplier = 100
        num_points = int(abs(opt_params.right_bound - opt_params.left_bound) * points_multiplier)
        step = abs(opt_params.right_bound - opt_params.left_bound)/num_points

        x = []
        for i in range(num_points):
            x.append(i * step + opt_params.left_bound)

        y = [optimizer.Func(point) for point in x]

        self.MplWidget.canvas.axes.plot(x, y)
        
        for point in solution.points:
            self.MplWidget.canvas.axes.plot(point[0], point[1], color="green", marker="*")

        self.MplWidget.canvas.axes.plot(solution.minimum[0], solution.minimum[1], color="red", marker="o")
        self.solutionX.setText("x = " + str(round(solution.minimum[0], 7)))
        self.solutionY.setText("y = " + str(round(solution.minimum[1], 7)))

        self.MplWidget.canvas.draw()


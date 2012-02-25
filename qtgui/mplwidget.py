from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

class MplWidget(QtGui.QWidget):

  def __init__(self, parent = None):
    QtGui.QWidget.__init__(self, parent)


    self.fig = Figure()
    self.canvas = FigureCanvas(self.fig)
    self.canvas.setParent(self)
    self.axes = self.fig.add_subplot(111)

    self.mpl_toolbar = NavigationToolbar(self.canvas, self)

    vbox = QtGui.QVBoxLayout()
    vbox.addWidget(self.canvas)
    vbox.addWidget(self.mpl_toolbar)
    self.setLayout(vbox)

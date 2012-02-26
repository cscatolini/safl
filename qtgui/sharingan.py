import numpy as np
from PyQt4 import QtCore
from PyQt4 import QtGui
from qtdesigner import Ui_MainWindow
import sys, scipy, pylab, simplejson
import scipy.misc


class DesignerMainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)

        QtCore.QObject.connect(self.actionLoad_Config, QtCore.SIGNAL("triggered()"), self.parseConfig)
        QtCore.QObject.connect(self.actionClose_2, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT("quit()"))

    def parseConfig(self):
#		configFile = str(QtGui.QFileDialog.getOpenFileName())
#		if file:
#			self.params = simplejson.load(open(configFile))
#			image = self.params['root_directory'] + '/frames/' + self.params['filename_format']%int(sys.argv[2])
        self.refreshImages('image')


    def refreshImages(self, image):
        imL = [self.im1, self.im2, self.im3, self.im4]
        for im in imL:
            im.axes.clear()
            im.axes.imshow(scipy.misc.lena(), cmap=pylab.cm.bone,
                interpolation='nearest')
            im.canvas.draw()
        self.cid = self.im1.canvas.mpl_connect('pick_event', self.onpick)
        edges = np.load('edges-00000001.npz')
        self.plotEdges(edges['edges'],self.im1)

    def onpick(self, event):
      for indx, line in enumerate(self.im1.axes.lines):
        if (event.artist == line):
          li = self.im1.axes.lines.pop(indx)
          self.im2.axes.plot( li.get_xdata(orig=True), li.get_ydata(orig=True) , picker=1)
          break
      
      self.im1.canvas.draw()
      self.im2.canvas.draw()

    def plotEdges(self, edges, im):
      for line in edges:
        flag = True
        for point in line:
          if (point[0] < 0 or point[1] < 0):
            flag = False
        if (flag):
          im.axes.plot(line, picker=1)
      im.canvas.draw()
        

app = QtGui.QApplication(sys.argv)

dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())

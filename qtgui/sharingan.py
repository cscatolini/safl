import numpy as np
from PyQt4 import QtCore
from PyQt4 import QtGui
from PIL import Image
from qtdesigner import Ui_MainWindow
import sys, scipy, pylab, simplejson
import scipy.misc


class DesignerMainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)


        for i in xrange(1,4):
          self.comboBox.addItem(str(i))

        QtCore.QObject.connect(self.actionLoad_Config, QtCore.SIGNAL("triggered()"), self.parseConfig)
        QtCore.QObject.connect(self.actionClose_2, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT("quit()"))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.prevImage)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.nextImage)

    def prevImage(self):
      self.init -= 1
      self.loadNew(self.init)

    def nextImage(self):
      self.init += 1
      self.loadNew(self.init)

    def parseConfig(self):
      configFile = str(QtGui.QFileDialog.getOpenFileName())
      self.init = 1
      try:
        self.params = simplejson.load(open(configFile))
        imageFilename = self.params['root_directory'] + '/frames/' + self.params['filename_format']%int(self.init)                
        image = np.asarray(Image.open(imageFilename))
        edges = self.params['root_directory'] + '/edges/' + self.params['edgesfile_format']%int(self.init)
        self.refreshImages(image, edges)
        self.statusBar.showMessage("Image:" + imageFilename)
      except Exception:
        self.statusBar.showMessage("Error")

    def loadNew(self,init):
      try:				
        imageFilename = self.params['root_directory'] + '/frames/' + self.params['filename_format']%int(init)
        image = np.asarray(Image.open(imageFilename))
        edges = self.params['root_directory'] + '/edges/' + self.params['edgesfile_format']%int(init)
        self.refreshImages(image, edges)
        self.statusBar.showMessage("Image:" + imageFilename)
      except Exception:
        self.statusBar.showMessage("Error")


    def refreshImages(self, image, edges):
        imL = [self.im1, self.im2, self.im3, self.im4]
        for im in imL:
            im.axes.clear()
            im.axes.imshow(image, cmap=pylab.cm.bone,
                interpolation='nearest')
            im.canvas.draw()
        self.cid = self.im1.canvas.mpl_connect('pick_event', self.onpick)
        edges = np.load(edges)
        self.plotEdges(edges['edges'],self.im1)

    def onpick(self, event):
      for indx, line in enumerate(self.im1.axes.lines):
        if (event.artist == line):
          li = self.im1.axes.lines.pop(indx)

          id = self.comboBox.currentIndex()+1
          
          if id == 1:						
            self.im2.axes.plot( li.get_xdata(orig=True), li.get_ydata(orig=True) , picker=1)
            self.im2.canvas.draw()
          elif id == 2:
            self.im3.axes.plot( li.get_xdata(orig=True), li.get_ydata(orig=True) , picker=1)
            self.im3.canvas.draw()
          elif id == 3:
            self.im4.axes.plot( li.get_xdata(orig=True), li.get_ydata(orig=True) , picker=1)
            self.im4.canvas.draw()
          self.im1.canvas.draw()
          break						

    def plotEdges(self, edges, im):
      for line in edges:
        flag = True
        for point in line:
          if (point[0] < 0 or point[1] < 0):
            flag = False
        if (flag):
          im.axes.plot(line, picker=3)
      im.canvas.draw()
        

app = QtGui.QApplication(sys.argv)

dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())

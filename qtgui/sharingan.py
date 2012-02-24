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
			im.canvas.ax.clear()
			im.canvas.ax.imshow(scipy.misc.lena(), cmap=pylab.cm.bone, interpolation='nearest')
			im.canvas.draw()

		self.cid = self.im1.canvas.mpl_connect('button_press_event', self.onclick)

	def onclick(self,event):
		print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata)

app = QtGui.QApplication(sys.argv)

dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())



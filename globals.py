import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from queue import Queue

app = QApplication(sys.argv)       
widget= QtWidgets.QStackedWidget()

i=1
sectionsNum=0 
junctionsNum=0  
maxtime=0#in micro second
Vp=0
impedanceArray=[]
times=[]
node_list = []
node_list_plot = []
node_list_print = []
queue = Queue(maxsize=400)

Tau_V1_2 = []
Tau_V2_1 = []
Rau_V1_2 = []
Rau_V2_1 = []






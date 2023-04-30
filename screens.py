from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
import globals
from operations import operation
import pyqtgraph as pg

class screen1(QDialog):

    def __init__(self):
        super(screen1, self).__init__()
        loadUi("screen1.ui",self)
        self.StartButton.clicked.connect(self.clicked_start)

    def clicked_start(self):
        globals.widget.setCurrentIndex(1)

class screen2(QDialog):

    def __init__(self):
        super(screen2, self).__init__()       
        loadUi("screen2.ui",self)
        self.NextButton.clicked.connect(self.clicked_next)
        self.PreviousButton.clicked.connect(self.clicked_previous)

    def clicked_next(self):
        globals.sectionsNum= int(self.NumOfSectionsInput.text())
        globals.junctionsNum= globals.sectionsNum-1
        globals.Vp= float(self.InitialIncidentVoltageInput.text())
        globals.widget.setCurrentIndex(2)

    def clicked_previous(self):
        globals.widget.setCurrentIndex(0)

class screen3(QDialog):

    def __init__(self):
        super(screen3, self).__init__()       
        loadUi("screen3.ui",self)
        self.Impedancelabel.setText("Enter impedance of section "+str(globals.i))
        self.Lengthlabel.setText("Enter length of section "+str(globals.i))
        self.NextButton.clicked.connect(self.clicked_next)
        self.PreviousButton.clicked.connect(self.clicked_previous)

    def clicked_next(self):
        z= float(self.ImpedanceInput.text())
        l= float(self.LengthInput.text())
        v= float(self.WaveVelocityInput.text())
        globals.impedanceArray.append(z)
        globals.times.append((l*1000)/v)
        self.ImpedanceInput.clear()
        self.LengthInput.clear()
        self.WaveVelocityInput.clear()
        globals.i+=1    
        if (globals.i == globals.junctionsNum+2):
            operation.calcInit()
            operation.calcNodes(20)
            globals.widget.setCurrentIndex(3)
            print(globals.impedanceArray) 
            print(globals.times)
            print(globals.Tau_V1_2)
            print(globals.Tau_V2_1)
        else: 
            self.Impedancelabel.setText("Enter impedance of section "+str(globals.i))
            self.Lengthlabel.setText("Enter length of section "+str(globals.i))
            if (globals.i == globals.sectionsNum):
                self.NextButton.setText("Finish")

    def clicked_previous(self):
        globals.i=1
        globals.widget.setCurrentIndex(1)
        globals.impedanceArray=[]
        globals.times=[]

class screen4(QDialog):
    
    def __init__(self):
        super(screen4, self).__init__()       
        loadUi("screen4.ui",self)
        self.IterationsNumInput.setText(str(20)) #initial iteration number
        self.DisplayButton.clicked.connect(self.clicked_display)

    def clicked_display(self):
        print(globals.node_list_plot)
        globals.node_list_chart=[]
        x=[]
        y=[]
        iterations= int(self.IterationsNumInput.text())
        junctionToDisplay = int(self.JunctionNumInput.text())
        if (iterations == 20):
            for element in globals.node_list_plot: 
                if (element["Junction"] == junctionToDisplay):
                    globals.node_list_chart.append(element)  
            globals.node_list_chart.sort(key=lambda node: node["time"])
            print(globals.node_list_chart)
            cumVoltage=0
            if (junctionToDisplay != 1):
                x.append(0)
                y.append(0)
            if (self.DisplayTypeComboBox.currentText() == "Absolute voltage"):
                for element in globals.node_list_chart:
                    x.append(element['time'])
                    y.append(element['volt'])
            elif (self.DisplayTypeComboBox.currentText() == "cumulative voltage"):  
                for element in globals.node_list_chart:
                    x.append(element['time'])
                    cumVoltage+= element['volt']
                    y.append(cumVoltage)                      
        else :
            operation.calcNodes(iterations)
            for element in globals.node_list_plot: 
                if (element["Junction"] == junctionToDisplay):
                    globals.node_list_chart.append(element)  
            globals.node_list_chart.sort(key=lambda node: node["time"])
            for element in globals.node_list_chart:
                x.append(element['time'])
                y.append(element['volt'])
            
            #x = [{k: d[k] for k in ('time')} for d in node_list_chart]
            #y = [{k: d[k] for k in ('volt')} for d in node_list_chart]
        print(x)
        print(y)
        # creating a pyqtgraph plot window
        window = pg.plot()
        window.setGeometry(100, 100, 600, 400)
        # title for the plot window
        title = "Voltage of junction "+str(junctionToDisplay)
        # setting window title to plot window
        window.setWindowTitle(title)
        # create pyqt5graph bar graph item
        # with width = 0.6
        # with bar colors = blue
        bargraph = pg.BarGraphItem(x = x, height = y, width = 1, brush ='b') #b is short for blue
        # add item to plot window
        # adding bargraph item to the window
        window.addItem(bargraph)
    
 
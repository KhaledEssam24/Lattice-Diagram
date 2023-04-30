import sys
from screens import screen1,screen2,screen3,screen4
import globals

screen1 = screen1()
screen2 = screen2()
screen3 = screen3()
screen4 = screen4()

globals.widget.addWidget(screen1)
globals.widget.addWidget(screen2)
globals.widget.addWidget(screen3)
globals.widget.addWidget(screen4)

globals.widget.setFixedWidth(600)
globals.widget.setFixedHeight(400)

globals.widget.show()

sys.exit(globals.app.exec_())



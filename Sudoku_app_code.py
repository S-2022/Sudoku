from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from functools import partial
import sys
import random

class MainWindow(QDialog):
    
    def __init__(self):
        super().__init__()

        self.quit=QPushButton('QUIT',self)
        self.quit.setGeometry(QRect(800,550,100,50))
        self.quit.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.quit.setFont(QFont('Arial Black',13))
        self.quit.clicked.connect(lambda:self.QApplication.quit())
        
        self.label=QLabel(self)
        self.label.resize(390,100)
        self.label.move(270,100)
        self.label.setFont(QFont('Times New Roman',40))
        self.label.setText('SUDOKU')

        self.label=QLabel(self)
        self.label.resize(375,75)
        self.label.move(255,240)
        self.label.setFont(QFont('Arial',13))
        self.label.setText('CHOOSE DIFFICULTY LEVEL : ')

        self.label=QPushButton('EASY',self)
        self.label.setGeometry(QRect(330,335,220,60))
        self.label.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.label.setFont(QFont('Arial Black',13))
        self.label.clicked.connect(self.easy)

        self.label=QPushButton('MEDIUM',self)
        self.label.setGeometry(QRect(330,395,220,60))
        self.label.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.label.setFont(QFont('Arial Black',13))
        self.label.clicked.connect(self.medium)

        self.label=QPushButton('DIFFICULT',self)
        self.label.setGeometry(QRect(330,455,220,60))
        self.label.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.label.setFont(QFont('Arial Black',13))
        self.label.clicked.connect(self.difficult)        

    def easy(self):
        r=random.randint(10,14)
        self.generate_sudoku(r)

    def medium(self):
        r=random.randint(5,9)
        self.generate_sudoku(r)

    def difficult(self):
        r=random.randint(0,4)
        self.generate_sudoku(r)

    def generate_sudoku(self,r):
        global puzzle,soln,wrong
        wrong=[0]
        f1=open('puzzle.txt','r')
        f2=open('soln.txt','r')
        i=random.randint(0,4)
        
        d={'.':0}
        for c in range(65,74):
            while(True):
                rand=random.randint(1,9)
                if rand not in d.values():
                    break
            d[chr(c)]=rand
        
        puzzle=[d[x] for x in f1.readlines()[i][:81]]
        soln=[d[x] for x in f2.readlines()[i][:81]]
        f1.close()
        f2.close()
        for k in range(r):
            r1=random.randint(0,80)
            puzzle[r1]=soln[r1]
        
        temp1=[]
        temp2=[]
        for i in [0,3,6]:
            l=[]
            for x in range(3):
                while(True):
                    rand=random.randint(i,i+2)
                    if rand not in l:
                        break
                l.append(rand)
            for x in l:
                temp1.extend(puzzle[x*9:x*9+9])
                temp2.extend(soln[x*9:x*9+9])
        puzzle=list(temp1)
        soln=list(temp2)
        
        temp1=[0 for x in range(81)]
        temp2=[0 for x in range(81)]
        for i in [0,3,6]:
            l=[]
            for x in range(3):
                while(True):
                    rand=random.randint(i,i+2)
                    if rand not in l:
                        break
                l.append(rand)
            for x in l:
                for y in range(9):
                    temp1[y*9+i]=puzzle[y*9+x]
                    temp2[y*9+i]=soln[y*9+x]
                i+=1
        puzzle=list(temp1)
        soln=list(temp2)

        i=0
        temp1=[]
        temp2=[]
        l=[]
        for x in range(3):
            while(True):
                rand=random.randint(i,i+2)
                if rand not in l:
                    break
            l.append(rand)
        l=[3*x for x in l]
        for x in l:
            temp1.extend(puzzle[x*9:x*9+27])
            temp2.extend(soln[x*9:x*9+27])
        puzzle=list(temp1)
        soln=list(temp2)
        
        temp1=[0 for x in range(81)]
        temp2=[0 for x in range(81)]
        l=[]
        for x in range(3):
            while(True):
                rand=random.randint(i,i+2)
                if rand not in l:
                    break
            l.append(rand)
        l=[3*x for x in l]
        i=0
        for x in l:
            for y in range(x,x+3):
                for z in range(9):
                    temp1[z*9+i]=puzzle[z*9+y]
                    temp2[z*9+i]=soln[z*9+y]
                i+=1
        puzzle=list(temp1)
        soln=list(temp2)
        
        gw=GameWindow()
        widget.addWidget(gw)
        widget.setCurrentIndex(widget.currentIndex()+1)

class GameWindow(QDialog):
    
    def __init__(self):
        super().__init__()
        global index,button_val
        index=[90]
        button_val=0
        
        self.home=QPushButton('HOME',self)
        self.home.setGeometry(QRect(0,550,100,50))
        self.home.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.home.setFont(QFont('Arial Black',13))
        self.home.clicked.connect(self.gohome)
        
        self.quit=QPushButton('QUIT',self)
        self.quit.setGeometry(QRect(800,550,100,50))
        self.quit.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.quit.setFont(QFont('Arial Black',13))
        self.quit.clicked.connect(lambda:self.QApplication.quit())
        
        for i in range(81):
            e=1
            if(i%9 in [3,4,5]):
                e=3
            if(i%9 in [6,7,8]):
                e=5
            w=1
            if(i//9 in [3,4,5]):
                w=3
            if(i//9 in [6,7,8]):
                w=5
            if(puzzle[i]!=0):
                self.b=QLabel(self)
                self.b.resize(50,50)
                self.b.move(350+(i%9)*50+e,75+(i//9)*50+w)
                self.b.setStyleSheet('border:1px solid gray;')
                self.b.setFont(QFont('Times New Roman',23))
                self.b.setText(str(puzzle[i]))
            else:
                self.b=QPushButton(' ',self)
                self.b.setGeometry(QRect(350+(i%9)*50+e,75+(i//9)*50+w,50,50))
                self.b.setStyleSheet("QPushButton"
                                     "{"
                                     "border:1px solid gray;"
                                     "}"
                                     "QPushButton::hover"
                                     "{"
                                     "background-color:mistyrose;"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color:salmon;"
                                     "}"
                                     )
                self.b.clicked.connect(partial(self.check1,i))
        
        self.a1=QPushButton('1',self)
        self.a1.setGeometry(QRect(100,150,50,50))
        self.a1.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a1.clicked.connect(partial(self.check3,1))
        
        self.a2=QPushButton('2',self)
        self.a2.setGeometry(QRect(160,150,50,50))
        self.a2.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a2.clicked.connect(partial(self.check3,2))
        
        self.a3=QPushButton('3',self)
        self.a3.setGeometry(QRect(220,150,50,50))
        self.a3.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a3.clicked.connect(partial(self.check3,3))
        
        self.a4=QPushButton('4',self)
        self.a4.setGeometry(QRect(100,210,50,50))
        self.a4.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a4.clicked.connect(partial(self.check3,4))
        
        self.a5=QPushButton('5',self)
        self.a5.setGeometry(QRect(160,210,50,50))
        self.a5.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a5.clicked.connect(partial(self.check3,5))
        
        self.a6=QPushButton('6',self)
        self.a6.setGeometry(QRect(220,210,50,50))
        self.a6.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a6.clicked.connect(partial(self.check3,6))
        
        self.a7=QPushButton('7',self)
        self.a7.setGeometry(QRect(100,270,50,50))
        self.a7.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a7.clicked.connect(partial(self.check3,7))
        
        self.a8=QPushButton('8',self)
        self.a8.setGeometry(QRect(160,270,50,50))
        self.a8.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a8.clicked.connect(partial(self.check3,8))
        
        self.a9=QPushButton('9',self)
        self.a9.setGeometry(QRect(220,270,50,50))
        self.a9.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.a9.clicked.connect(partial(self.check3,9))

        self.w=QLabel(self)
        self.w.resize(150,50)
        self.w.move(100,350)
        self.w.setFont(QFont('Times New Roman',14))
        self.w.setText('Errors : ')

        self.w=QLabel(self)
        self.w.resize(150,50)
        self.w.move(190,350)
        self.w.setFont(QFont('Arial Black',14))
        self.w.setStyleSheet("color:red")
        self.w.setText(str(' X'*wrong[0]))     

    def paintEvent(self, event):
        painter=QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #vertical:
        painter.drawLine(349,74,349,531)
        painter.drawLine(501,74,501,531)
        painter.drawLine(653,74,653,531)
        painter.drawLine(806,74,806,531)
        #horizontal:
        painter.drawLine(349,74,806,74)
        painter.drawLine(349,226,806,226)
        painter.drawLine(349,378,806,378)
        painter.drawLine(349,531,806,531)

    def check1(self,i):
        index.append(i)

    def check3(self,n):
        global msg
        button_val=n        
        if(index[-1]!=90):
            if(soln[index[-1]]==button_val):
                puzzle[index[-1]]=button_val
            else:
                wrong[0]+=1
        if(puzzle.count(0)==0):
            msg='CONGRATULATIONS!'
            Lw=LastWindow()
            widget.addWidget(Lw)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif(wrong[0]==3):
            msg='TOO MANY ERRORS!'
            Lw=LastWindow()
            widget.addWidget(Lw)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            gwn=GameWindow()
            widget.addWidget(gwn)
            widget.setCurrentIndex(widget.currentIndex()+1)
                
    def gohome(self):
        puzzle=[]
        soln=[]
        mwn=MainWindow()
        widget.addWidget(mwn)
        widget.setCurrentIndex(widget.currentIndex()+1)
                
class LastWindow(QDialog):
    
    def __init__(self):
        
        super().__init__()
        
        self.home=QPushButton('HOME',self)
        self.home.setGeometry(QRect(0,550,100,50))
        self.home.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.home.setFont(QFont('Arial Black',13))
        self.home.clicked.connect(self.gohome)
        
        self.quit=QPushButton('QUIT',self)
        self.quit.setGeometry(QRect(800,550,100,50))
        self.quit.setStyleSheet("QPushButton::hover""{""background-color:mistyrose;""}")
        self.quit.setFont(QFont('Arial Black',13))
        self.quit.clicked.connect(lambda:self.QApplication.quit())

        self.label=QLabel(self)
        self.label.resize(800,200)
        self.label.move(150,200)
        self.label.setFont(QFont('Times New Roman',30))
        self.label.setText(msg)

    def gohome(self):
        puzzle=[]
        soln=[]
        mwn=MainWindow()
        widget.addWidget(mwn)
        widget.setCurrentIndex(widget.currentIndex()+1)

app=QApplication(sys.argv)
widget=QStackedWidget()
mw=MainWindow()
widget.addWidget(mw)
widget.setFixedHeight(600)
widget.setFixedWidth(900)
widget.setWindowFlag(Qt.FramelessWindowHint)
widget.setStyleSheet("background-color:seashell;")
widget.show()
sys.exit(app.exec())

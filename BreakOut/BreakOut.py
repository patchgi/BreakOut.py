# coding: utf-8

# Python2.X encoding wrapper (Windows dedicated processing)
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

class BreakOut:


    def __init__(self,_x,_y):
        self.mapx=_x
        self.mapy=_y

        self.ballPosX=5
        self.ballPosY=5

        self.barPosX=5
        self.addBarX=1

        self.addX=1
        self.addY=1

        ###self.block=[[0 for j in range(self.x)] for i in range(2)]
       
    def update(self):
        field=[]

        for i in range(self.mapy):
            for j in range(self.mapx):
                if i==0 or i==self.mapy-1:
                    if j==0:
                        field.append("+")
                    elif j==self.mapx-1:
                        field.append("+")
                        field.append("\n")   
                    else:
                        field.append("-")

                elif i==self.mapy-3:
                    if j==0:
                        field.append("|")

                    elif j==self.mapx-1:
                        field.append("|")
                        field.append("\n")

                    elif j==self.ballPosX and i==self.ballPosY:
                        field.append("o")

                    elif j==self.barPosX:
                        field.append("=")

                    else :
                        field.append(" ")




                else:        
                    if j==0:
                        field.append("|")

                    elif j==self.mapx-1:
                        field.append("|")
                        field.append("\n")

                    elif j==self.ballPosX and i==self.ballPosY:
                        field.append("o")
                        
                    else :
                        field.append(" ")

        

        if self.ballPosX<2 or self.ballPosX>self.mapx-3:
            self.addX*=-1
        if self.ballPosY<2 or self.ballPosY>self.mapy-3:
            self.addY*=-1
        """for blockX in  range(self.mapx):
            for blockY in range(2):
                if self.ballPosX==blockX and self.ballPosY==blockY:
                        self.block[blockY][blockX]=1
                        """
        if self.ballPosY==self.mapy-3 and self.ballPosX==self.barPosX:
            self.addY*=-1

        map_string="".join(field)

        self.ballPosX+=self.addX
        self.ballPosY+=self.addY
        self.barPosX=self.ballPosX

        print map_string.rstrip()

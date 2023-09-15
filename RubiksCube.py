from Exceptions import IncorrectMoveException, IncorrectTileException
from random import randrange
import copy

def colorSymbol(color):
    colorcode = ''
    if color == "blue":
        colorcode = '\033[94m'
    elif color == "red":
        colorcode = '\033[91m'
    elif color  == "white":
        colorcode = '\33[37m'
    elif color == "yellow":
        colorcode = '\033[93m'
    elif color == "green":
        colorcode = '\33[32m'
    elif color == "orange":
        colorcode = '\33[31m'+'\33[43m'
    return colorcode+color.upper()[0]+'\33[37m'+'\33[40m'

class RubiksCube:
    def __init__(self):
        #Setting tiles of the self
        self.side1 = ["white", "white", "white", "white", "white", "white", "white", "white", "white"] #white side
        self.side2 = ["yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"] #yellow side
        self.side3 = ["orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange"] #orange side
        self.side4 = ["red", "red", "red", "red", "red", "red", "red", "red", "red"] #red side
        self.side5 = ["green", "green", "green", "green", "green", "green", "green", "green", "green"] #green side
        self.side6 = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"] #blue side
    def getTile(self, side, tile):
        if side<1 or side>6 or tile<1 or tile>9:
            raise IncorrectTileException("Incorrect side or tile number!")
        if side==1:
            return self.side1[tile-1]
        elif side==2:
            return self.side2[tile-1]
        elif side==3:
            return self.side3[tile-1]
        elif side==4:
            return self.side4[tile-1]
        elif side==5:
            return self.side5[tile-1]
        elif side==6:
            return self.side6[tile-1]
    def visualize(self):
        print(" "*4 + colorSymbol(self.side2[0]) + colorSymbol(self.side2[1]) + colorSymbol(self.side2[2]))
        print(" "*4 + colorSymbol(self.side2[3]) + colorSymbol(self.side2[4]) + colorSymbol(self.side2[5]))
        print(" "*4 + colorSymbol(self.side2[6]) + colorSymbol(self.side2[7]) + colorSymbol(self.side2[8])+"\n")
        print(colorSymbol(self.side5[0]) + colorSymbol(self.side5[1]) + colorSymbol(self.side5[2]) + " " + colorSymbol(self.side3[0]) + colorSymbol(self.side3[1]) + colorSymbol(self.side3[2]) + " " + colorSymbol(self.side6[0]) + colorSymbol(self.side6[1]) + colorSymbol(self.side6[2]) + " " + colorSymbol(self.side4[0]) + colorSymbol(self.side4[1]) + colorSymbol(self.side4[2]))
        print(colorSymbol(self.side5[3]) + colorSymbol(self.side5[4]) + colorSymbol(self.side5[5]) + " " + colorSymbol(self.side3[3]) + colorSymbol(self.side3[4]) + colorSymbol(self.side3[5]) + " " + colorSymbol(self.side6[3]) + colorSymbol(self.side6[4]) + colorSymbol(self.side6[5]) + " " + colorSymbol(self.side4[3]) + colorSymbol(self.side4[4]) + colorSymbol(self.side4[5]))
        print(colorSymbol(self.side5[6]) + colorSymbol(self.side5[7]) + colorSymbol(self.side5[8]) + " " + colorSymbol(self.side3[6]) + colorSymbol(self.side3[7]) + colorSymbol(self.side3[8]) + " " + colorSymbol(self.side6[6]) + colorSymbol(self.side6[7]) + colorSymbol(self.side6[8]) + " " + colorSymbol(self.side4[6]) + colorSymbol(self.side4[7]) + colorSymbol(self.side4[8]))
        print("\n"+" "*4 + colorSymbol(self.side1[0]) + colorSymbol(self.side1[1]) + colorSymbol(self.side1[2]))
        print(" "*4 + colorSymbol(self.side1[3]) + colorSymbol(self.side1[4]) + colorSymbol(self.side1[5]))
        print(" "*4 + colorSymbol(self.side1[6]) + colorSymbol(self.side1[7]) + colorSymbol(self.side1[8]))

    moves = ["U", "Up", "D", "Dp", "R", "Rp", "L", "Lp", "F", "Fp", "B", "Bp", "M", "Mp", "E", "Ep", "S", "Sp"]
    def moveCube(self, move):
        if move not in self.moves:
            raise IncorrectMoveException("Incorrect movement!")
        oldCube = copy.deepcopy(self)
        if move=="U":
            for i in range(0, 3):
                self.side3[i]=oldCube.side6[i]
                self.side6[i]=oldCube.side4[i]
                self.side4[i]=oldCube.side5[i]
                self.side5[i]=oldCube.side3[i]
            self.side2[0]=oldCube.side2[6]
            self.side2[1]=oldCube.side2[3]
            self.side2[2]=oldCube.side2[0]
            self.side2[3]=oldCube.side2[7]
            self.side2[5]=oldCube.side2[1]
            self.side2[6]=oldCube.side2[8]
            self.side2[7]=oldCube.side2[5]
            self.side2[8]=oldCube.side2[2]
        elif move=="Up":
            for i in range(0, 3):
                self.side6[i]=oldCube.side3[i]
                self.side4[i]=oldCube.side6[i]
                self.side5[i]=oldCube.side4[i]
                self.side3[i]=oldCube.side5[i]
            self.side2[6]=oldCube.side2[0]
            self.side2[3]=oldCube.side2[1]
            self.side2[0]=oldCube.side2[2]
            self.side2[7]=oldCube.side2[3]
            self.side2[1]=oldCube.side2[5]
            self.side2[8]=oldCube.side2[6]
            self.side2[5]=oldCube.side2[7]
            self.side2[2]=oldCube.side2[8]
        elif move=="D":
            for i in range(0, 3):
                self.side6[i+6]=oldCube.side3[i+6]
                self.side4[i+6]=oldCube.side6[i+6]
                self.side5[i+6]=oldCube.side4[i+6]
                self.side3[i+6]=oldCube.side5[i+6]
            self.side1[0]=oldCube.side1[6]
            self.side1[1]=oldCube.side1[3]
            self.side1[2]=oldCube.side1[0]
            self.side1[3]=oldCube.side1[7]
            self.side1[5]=oldCube.side1[1]
            self.side1[6]=oldCube.side1[8]
            self.side1[7]=oldCube.side1[5]
            self.side1[8]=oldCube.side1[2]
        elif move=="Dp":
            for i in range(0, 3):
                self.side3[i+6]=oldCube.side6[i+6]
                self.side6[i+6]=oldCube.side4[i+6]
                self.side4[i+6]=oldCube.side5[i+6]
                self.side5[i+6]=oldCube.side3[i+6]
            self.side1[6]=oldCube.side1[0]
            self.side1[3]=oldCube.side1[1]
            self.side1[0]=oldCube.side1[2]
            self.side1[7]=oldCube.side1[3]
            self.side1[1]=oldCube.side1[5]
            self.side1[8]=oldCube.side1[6]
            self.side1[5]=oldCube.side1[7]
            self.side1[2]=oldCube.side1[8]
        elif move=="R":
            for i in range(0, 3):
                self.side3[(i+1)*3-1]=oldCube.side1[(i+1)*3-1]
                self.side1[(i+1)*3-1]=oldCube.side4[9-(i+1)*3]
                self.side4[(i+1)*3-3]=oldCube.side2[8-i*3]
                self.side2[(i+1)*3-1]=oldCube.side3[(i+1)*3-1]
            self.side6[0]=oldCube.side6[6]
            self.side6[1]=oldCube.side6[3]
            self.side6[2]=oldCube.side6[0]
            self.side6[3]=oldCube.side6[7]
            self.side6[5]=oldCube.side6[1]
            self.side6[6]=oldCube.side6[8]
            self.side6[7]=oldCube.side6[5]
            self.side6[8]=oldCube.side6[2]
        elif move=="Rp":
            for i in range(0, 3):
                self.side3[(i+1)*3-1]=oldCube.side2[(i+1)*3-1]
                self.side2[8-i*3]=oldCube.side4[(i+1)*3-3] #8<0 #5<3 #2<6
                self.side4[9-(i+1)*3]=oldCube.side1[(i+1)*3-1] 
                self.side1[(i+1)*3-1]=oldCube.side3[(i+1)*3-1]
            self.side6[6]=oldCube.side6[0]
            self.side6[3]=oldCube.side6[1]
            self.side6[0]=oldCube.side6[2]
            self.side6[7]=oldCube.side6[3]
            self.side6[1]=oldCube.side6[5]
            self.side6[8]=oldCube.side6[6]
            self.side6[5]=oldCube.side6[7]
            self.side6[2]=oldCube.side6[8]
        elif move=="Lp":
            for i in range(0, 3):
                self.side3[(i+1)*3-3]=oldCube.side1[(i+1)*3-3]
                self.side1[(i+1)*3-3]=oldCube.side4[8-i*3] #0>8 #3>5 #6>2
                self.side4[(i+1)*3-1]=oldCube.side2[(i+1)*3-3]
                self.side2[(i+1)*3-3]=oldCube.side3[(i+1)*3-3]
            self.side5[0]=oldCube.side5[6]
            self.side5[1]=oldCube.side5[3]
            self.side5[2]=oldCube.side5[0]
            self.side5[3]=oldCube.side5[7]
            self.side5[5]=oldCube.side5[1]
            self.side5[6]=oldCube.side5[8]
            self.side5[7]=oldCube.side5[5]
            self.side5[8]=oldCube.side5[2]
        elif move == "L":
            for i in range(0, 3):
                self.side3[(i+1)*3-3]=oldCube.side2[(i+1)*3-3]
                self.side2[(i+1)*3-3]=oldCube.side4[(i+1)*3-1]
                self.side4[8-i*3]=oldCube.side1[(i+1)*3-3]
                self.side1[(i+1)*3-3]=oldCube.side3[(i+1)*3-3]
            self.side5[6]=oldCube.side5[0]
            self.side5[3]=oldCube.side5[1]
            self.side5[0]=oldCube.side5[2]
            self.side5[7]=oldCube.side5[3]
            self.side5[1]=oldCube.side5[5]
            self.side5[8]=oldCube.side5[6]
            self.side5[5]=oldCube.side5[7]
            self.side5[2]=oldCube.side5[8]
        elif move=="F":
            for i in range(0, 3):
                self.side2[i+6]=oldCube.side5[8-i*3] #6<8 #7<5 #8<2
                self.side5[2+i*3]=oldCube.side1[i] #2<0 #5<1 #8<2
                self.side1[i]=oldCube.side6[9-(i+1)*3] #0<6 #1<3 #2<0
                self.side6[(i)*3]=oldCube.side2[i+6] #0<6 #3<7 #6<8
            self.side3[0]=oldCube.side3[6]
            self.side3[1]=oldCube.side3[3]
            self.side3[2]=oldCube.side3[0]
            self.side3[3]=oldCube.side3[7]
            self.side3[5]=oldCube.side3[1]
            self.side3[6]=oldCube.side3[8]
            self.side3[7]=oldCube.side3[5]
            self.side3[8]=oldCube.side3[2]
        elif move=="Fp":
            for i in range(0, 3):
                self.side2[i+6]=oldCube.side6[9-(i+1)*3]
                self.side6[(i)*3]=oldCube.side1[i]
                self.side1[i]=oldCube.side5[8-i*3]
                self.side5[2+i*3]=oldCube.side2[i+6]
            self.side3[6]=oldCube.side3[0]
            self.side3[3]=oldCube.side3[1]
            self.side3[0]=oldCube.side3[2]
            self.side3[7]=oldCube.side3[3]
            self.side3[1]=oldCube.side3[5]
            self.side3[8]=oldCube.side3[6]
            self.side3[5]=oldCube.side3[7]
            self.side3[2]=oldCube.side3[8]
        elif move=="B":
            for i in range(0, 3):
                self.side2[i]=oldCube.side6[2+i*3] #0<2 #1<5 #2<8
                self.side6[2+i*3]=oldCube.side1[8-i] #2<8 #5<7 #8<6
                self.side1[8-i]=oldCube.side5[i+6] #8<6 #7<7 #6<8
                self.side5[i*3]=oldCube.side2[2-i] #0<2 #3<1 #6<0
            self.side4[0]=oldCube.side4[6]
            self.side4[1]=oldCube.side4[3]
            self.side4[2]=oldCube.side4[0]
            self.side4[3]=oldCube.side4[7]
            self.side4[5]=oldCube.side4[1]
            self.side4[6]=oldCube.side4[8]
            self.side4[7]=oldCube.side4[5]
            self.side4[8]=oldCube.side4[2]
        elif move=="Bp":
            for i in range(0, 3):
                self.side2[i]=oldCube.side5[9-(i+1)*3] #0<6 #1<3 #2<0
                self.side5[i*3]=oldCube.side1[8-i]
                self.side1[8-i]=oldCube.side6[2+i*3]
                self.side6[2+i*3]=oldCube.side2[2-i]
            self.side4[6]=oldCube.side4[0]
            self.side4[3]=oldCube.side4[1]
            self.side4[0]=oldCube.side4[2]
            self.side4[7]=oldCube.side4[3]
            self.side4[1]=oldCube.side4[5]
            self.side4[8]=oldCube.side4[6]
            self.side4[5]=oldCube.side4[7]
            self.side4[2]=oldCube.side4[8]
        elif move=="M":
            for i in range(0, 3):
                self.side2[1+i*3]=oldCube.side4[10-3*(i+1)] #1<7 #4<4 #7<1
                self.side4[1+i*3]=oldCube.side1[10-3*(i+1)] 
                self.side1[1+i*3]=oldCube.side3[1+i*3]
                self.side3[1+i*3]=oldCube.side2[1+i*3]
        elif move=="Mp":
            for i in range(0, 3):
                self.side2[1+i*3]=oldCube.side3[1+i*3]
                self.side3[1+i*3]=oldCube.side1[10-3*(i+1)] 
                self.side1[1+i*3]=oldCube.side4[10-3*(i+1)]
                self.side4[1+i*3]=oldCube.side2[1+i*3]
        elif move=="E":
            for i in range(0, 3):
                self.side3[3+i]=oldCube.side5[3+i]
                self.side5[3+i]=oldCube.side4[3+i] 
                self.side4[3+i]=oldCube.side6[3+i]
                self.side6[3+i]=oldCube.side3[3+i]
        elif move=="Ep":
            for i in range(0, 3):
                self.side3[3+i]=oldCube.side6[3+i]
                self.side6[3+i]=oldCube.side4[3+i] 
                self.side4[3+i]=oldCube.side5[3+i]
                self.side5[3+i]=oldCube.side3[3+i]
        elif move=="S":
            for i in range(0, 3):
                self.side2[3+i]=oldCube.side5[7-3*i] #3<7 #4<4 #5<1
                self.side5[7-3*i]=oldCube.side1[5-i] #7<5 #4<4 #1<3
                self.side1[3+i]=oldCube.side6[7-3*i] #3<7 4<4 5<1
                self.side6[1+3*i]=oldCube.side2[3+i] #1<3 #4<4 #7<5
        elif move=="Sp":
            for i in range(0, 3):
                self.side2[3+i]=oldCube.side6[7-3*i]
                self.side6[1+3*i]=oldCube.side1[5-i]
                self.side1[3+i]=oldCube.side5[7-3*i]
                self.side5[7-3*i]=oldCube.side2[3+i]
    def rotate(self, axis, rots):
        if axis=="x":
            for i in range(rots):
                self.moveCube("U")
                self.moveCube("Dp")
                self.moveCube("Ep")
        if axis=="y":
            for i in range(rots):
                self.moveCube("R")
                self.moveCube("Lp")
                self.moveCube("Mp")

    def scramble(self, mvs):
        for i in range(mvs):
            self.moveCube(self.moves[randrange(0, 17)])
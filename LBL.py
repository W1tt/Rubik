from RubiksCube import RubiksCube

class LBL():
    @staticmethod
    def rotateCorrectly(cube):
        if cube.side3[4]=="orange":
            pass
        elif cube.side1[4]=="orange":
            cube.rotate("y", 1)
        elif cube.side2[4]=="orange":
            cube.rotate("y", 3)
        elif cube.side4[4]=="orange":
            cube.rotate("y", 2)
        elif cube.side5[4]=="orange":
            cube.rotate("x", 3)
        elif cube.side6[4]=="orange":
            cube.rotate("x", 1)
        if cube.side2[4]=="yellow":
            pass
        elif cube.side1[4]=="yellow":
            cube.rotate("y", 2)
            cube.rotate("x", 2)
        elif cube.side5[4]=="yellow":
            cube.rotate("x", 1)
            cube.rotate("y", 3)
            cube.rotate("x", 3)
        elif cube.side6[4]=="yellow":
            cube.rotate("x", 3)
            cube.rotate("y", 3)
            cube.rotate("x", 1)
    def whiteBorder(self, cube, side, ind, col):
        if side==1:
            if col=="orange":
                if ind==1:
                    pass
                if ind==3:
                    cube.moveCube("Lp")
                    cube.moveCube("E")
                    cube.moveCube("F")
                if ind==5:
                    cube.moveCube("R")
                    cube.moveCube("Ep")
                    cube.moveCube("Fp")
                if ind==7:
                    cube.moveCube("Bp")
                    cube.moveCube("E")
                    cube.moveCube("E")
                    cube.moveCube("F")
    def firstLayer(self, cube):
        self.rotateCorrectly(cube)
        try:
            side = 1
            ind = cube.side1.index("white")
            if ind==1:
                col = cube.side3[7]
            elif ind==3:
                col = cube.side5[7]
            elif ind==5:
                col = cube.side6[7]
            elif ind==7:
                col = cube.side4[7]
        except:
            pass
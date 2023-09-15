from RubiksCube import RubiksCube
from LBL import LBL





        

cube = RubiksCube()
cube.scramble(10)
LBL.firstLayer(cube)
cube.visualize()
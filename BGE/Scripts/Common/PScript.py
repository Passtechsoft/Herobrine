from bge import *
from mathutils import Vector, geometry, Matrix, Euler, Color
from math import cos, acos, sin, asin, tan, atan, sqrt, pi, degrees, radians, copysign, ceil, floor
from random import uniform as rand
from copy import deepcopy, copy
import sys
GameLogic = logic                                     
        
c = GameLogic.getCurrentController()
sce = GameLogic.getCurrentScene()
own = c.owner         
objList = sce.objects

inactList = sce.objectsInactive

CLASSIFICATOR_OBJECT = "~object"

SceOrigin = objList["SceOrigin"]


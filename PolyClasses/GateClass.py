##@package GateClass
#Consist of Gate class definition
from PolyClasses.StandartPolygonClass import *
from shapely.geometry import Polygon

##This class create Gate objects which inherited from StandartPolygon class
#
# The main difference that objects save from which two Layer objects Gate obj was created
class Gate(StandartPolygon):

    ##  The constructor of Gate
    #   @param self The object pointer
    #   @param array_of_dots array of (x,y)
    #   @param Layer LayerClass object
    #   @param FirstDerivativeLayer LayerClass object
    #   @param SecondDerivativeLayer LayerClass object
    def __init__(self,array_of_dots,Layer = None,FirstDerivativeLayer = None,SecondDerivativeLayer = None):
        self._array_of_dots = array_of_dots
        self._Layer = Layer
        self._poly = Polygon(array_of_dots)
        self.__derivative_from_layers = (FirstDerivativeLayer,SecondDerivativeLayer)
        if (None != Layer): self._Layer.put_polygon_into_layer(self)
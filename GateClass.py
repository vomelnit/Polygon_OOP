from StandartPolygonClass import *
from shapely.geometry import Polygon

class Gate(StandartPolygon):
    def __init__(self,array_of_dots,Layer = None,FirstDerivativeLayer = None,SecondDerivativeLayer = None):
        self._array_of_dots = array_of_dots
        self._Layer = Layer
        self._poly = Polygon(array_of_dots)
        self.__derivative_from_layers = (FirstDerivativeLayer,SecondDerivativeLayer)
        if (None != Layer): self._Layer.put_polygon_into_layer(self)
##@package StandartPolygonClass
#Consist of StandartPolygon class definition

from shapely.geometry import Polygon

##This class create Polygon object
#
# Create polygon object via array of points (exp. [(1,2),(4,3),(-4.55,6,98)] )
class StandartPolygon():

    ##  The constructor of StandartPolygon
    #   @param self The object pointer
    #   @param array_of_dots array of (x,y)
    #   @param Layer LayerClass object
    #   @param isDerivative Bool
    def __init__(self,array_of_dots,Layer = None, isDerivative = False):
        self._array_of_dots = array_of_dots
        self._Layer = Layer
        self._poly = Polygon(array_of_dots)
        self.__isDerivative = isDerivative
        if (None != Layer): self._Layer.put_polygon_into_layer(self)

    ##  Bind Polygon obj to certain Layer obj
    #   @param self The object pointer
    #   @param Layer Layer object
    def set_Layer(self, Layer):
        self._Layer = Layer
        self._Layer.put_polygon_into_layer(self)

    ##  Return Layer obj that own this StandartPolygon obj
    #   @param self The object pointer
    #   @return Layer object
    def get_Layer(self):
        return (self._Layer)

    ##  Unbind Polygon obj from current Layer obj
    #   @param self The object pointer
    def delete_Layer(self):
        self._Layer = None
        self._Layer.remove_polygon_into_layer(self)

    ##  Return array of polygon points
    #   @param self The object pointer
    #   @return array of (x,y)
    def get_array_of_dots(self):
        return self._array_of_dots

    ##  Return shapely package Polygon obj
    #   @param self The object pointer
    #   @return Polygon object
    def get_poly(self):
        return self._poly

    ##  Return if polygon is created by derivative way
    #   @param self The object pointer
    #   @return Bool
    def get_is_polygon_derivative(self):
        return self.__isDerivative
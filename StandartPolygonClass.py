from shapely.geometry import Polygon

class StandartPolygon():
    def __init__(self,array_of_dots,Layer = None, isDerivative = False):
        self._array_of_dots = array_of_dots
        self._Layer = Layer
        self._poly = Polygon(array_of_dots)
        self.__isDerivative = isDerivative
        if (None != Layer): self._Layer.put_polygon_into_layer(self)

    def set_Layer(self, Layer):
        self._Layer = Layer
        self._Layer.put_polygon_into_layer(self)

    def get_Layer(self):
        return (self._Layer)

    def delete_Layer(self):
        self._Layer = None
        self._Layer.remove_polygon_into_layer(self)

    def get_array_of_dots(self):
        return self._array_of_dots

    def get_poly(self):
        return self._poly

    def get_is_polygon_derivative(self):
        return self.__isDerivative
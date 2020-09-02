from shapely.geometry import Polygon


class DrawSpace:
    def __init__(self,dimensions):
        self.__width = dimensions.first
        self.__height = dimensions.second

    def get_DrawSpace_dimensions(self):
        return (self.__width,self.__height)

class Layer:
    def __init__(self,color,priority,DrawSpace = None):
        self.__color = color
        self.__priority = priority
        self.__DrawSpace = DrawSpace

    def get_color_of_layer(self):
        return (self.__color)

    def set_DrawSpace(self,DrawSpace):
        self.__DrawSpace = DrawSpace

    def get_DrawSpace(self):
        return(self.__DrawSpace)

    def delete_DrawSpace(self):
        self.__DrawSpace = None

    def get_priority_of_layer(self):
        return (self.__priority)

    def set_color_of_layer(self,color):
        self.__color = color

    def set_priority_of_layer(self,priority):
        self.__priority  = priority


class StandartPolygon():
    def __init__(self,array_of_dots,Layer = None, isDerivative = False):
        self.__array_of_dots = array_of_dots
        self.__Layer = Layer
        self.__poly = Polygon(array_of_dots)
        self.__isDerivative = isDerivative


    def set_Layer(self, Layer):
        self.__DrawSpace = DrawSpace

    def get_Layer(self):
        return (self.__Layer)

    def delete_Layer(self):
        self.__Layer = None

    def get_array_of_dots(self):
        return self.__array_of_dots

    def get_poly(self):
        return self.__poly

    def get_is_polygon_derivative(self):
        return self.__isDerivative


class BooleanOperationsBlock:

    def get_resulting_polygon_from_operation_OR(self, First_PolygonObj, Second_PolygonObj):
        if (First_PolygonObj.get_poly().intersects(Second_PolygonObj.get_poly())):
            Union_result_polynom = First_PolygonObj.get_poly().union(Second_PolygonObj.get_poly())
            return self.__get_list_of_points_from_polynom(Union_result_polynom)
        else:
            return None

    def get_resulting_polygon_from_operation_AND(self, First_PolygonObj, Second_PolygonObj):
        if (First_PolygonObj.get_poly().intersects(Second_PolygonObj.get_poly())):
            Intersection_result_polynom = First_PolygonObj.get_poly().intersection(Second_PolygonObj.get_poly())
            return self.__get_list_of_points_from_polynom(Intersection_result_polynom)
        else:
            return None

    def get_resulting_polygon_from_operation_NOT_OR(self, First_PolygonObj, Second_PolygonObj):
        Difference_result_polynom = First_PolygonObj.get_poly().difference(Second_PolygonObj.get_poly())
        if (Difference_result_polynom.is_empty()):
            return None
        else:
            return self.__get_list_of_points_from_polynom(Difference_result_polynom)

    def __get_list_of_points_from_polynom(self, Polynom):
        points_list_x, points_list_y = Polynom.exterior.coords.xy
        points_list = []
        for i in range(len(points_list_x)):
            points_list.append((points_list_x[i], points_list_y[i]))
        return points_list


if __name__ == "__main__":

    poly1 = StandartPolygon([(0,0),(6,0),(6,6),(0,6)])
    poly2 = StandartPolygon([(5, 5), (10, 5), (10, 10), (5, 10)])
    BooleanOperationsBlockObj = BooleanOperationsBlock()
    print(BooleanOperationsBlockObj.get_resulting_polygon_from_operation_AND(poly1,poly2))
    q = Polygon([(0, 0), (4, 0), (4, 4), (0, 4)])
    # q = Polygon([(0,0),(4,0),(4,4),(0,4)])
    # p = Polygon([(5, 5), (10, 5), (10, 10), (5, 10)])
    # print(p.intersection(q).is_empty)


from shapely.geometry import Polygon


class DrawSpace:
    def __init__(self,dimensions):
        self.__width = dimensions.first
        self.__height = dimensions.second

    def get_DrawSpace_dimensions(self):
        return (self.__width,self.__height)

class Layer:

    __layer_quantity = 0

    def __init__(self,DrawSpace = None):
        self.__polygon_array = []
        Layer.__layer_quantity += 1
        self.__color = Layer.__layer_quantity
        self.__priority = Layer.__layer_quantity
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

    def put_polygon_into_layer(self,StandartPoltObj):
        self.__polygon_array.append(StandartPoltObj)

    def remove_polygon_into_layer(self,StandartPoltObj):
        self.__polygon_array.remove(StandartPoltObj)

    def get_polygon_array_belong_layer(self):
        return self.__polygon_array
    #
    # def set_priority_of_layer(self,priority):
    #     self.__priority  = priority


class StandartPolygon():
    def __init__(self,array_of_dots,Layer = None, isDerivative = False):
        self._array_of_dots = array_of_dots
        self._Layer = Layer
        self._poly = Polygon(array_of_dots)
        self.__isDerivative = isDerivative
        if (None != Layer): self._Layer.put_polygon_into_layer(self)

    def set_Layer(self, Layer):
        self.__Layer = Layer
        self.__Layer.put_polygon_into_layer(self)

    def get_Layer(self):
        return (self.__Layer)

    def delete_Layer(self):
        self.__Layer = None
        self.__Layer.remove_polygon_into_layer(self)

    def get_array_of_dots(self):
        return self._array_of_dots

    def get_poly(self):
        return self._poly

    def get_is_polygon_derivative(self):
        return self.__isDerivative


class Gate(StandartPolygon):
    def __init__(self,array_of_dots,Layer = None,FirstDerivativeLayer = None,SecondDerivativeLayer = None):
        self._array_of_dots = array_of_dots
        self._Layer = Layer
        self._poly = Polygon(array_of_dots)
        self.__derivative_from_layers = (FirstDerivativeLayer,SecondDerivativeLayer)
        if (None != Layer): self._Layer.put_polygon_into_layer(self)

class BooleanOperationsBlock:

    def get_resulting_polygon_arr_from_operation_OR(self, First_PolygonObj, Second_PolygonObj):
        if (First_PolygonObj.get_poly().intersects(Second_PolygonObj.get_poly())):
            Union_result_polygom = First_PolygonObj.get_poly().union(Second_PolygonObj.get_poly())
            return self._get_arr_of_StandartPolygons(Union_result_polygom)
        else:
            return None

    def get_resulting_polygon_arr_from_operation_AND(self, First_PolygonObj, Second_PolygonObj):
        if (First_PolygonObj.get_poly().intersects(Second_PolygonObj.get_poly())):
            Intersection_result_polygom = First_PolygonObj.get_poly().intersection(Second_PolygonObj.get_poly())
            return self._get_arr_of_StandartPolygons(Intersection_result_polygom)
        else:
            return None

    def get_resulting_polygon_arr_from_operation_NOT_OR(self, First_PolygonObj, Second_PolygonObj):
        Difference_result_polygom = First_PolygonObj.get_poly().difference(Second_PolygonObj.get_poly())
        return self._get_arr_of_StandartPolygons(Difference_result_polygom)


    def _get_list_of_points_from_polynom(self, Polynom):
        points_list_x, points_list_y = Polynom.exterior.coords.xy
        points_list = []
        for i in range(len(points_list_x)):
            points_list.append((points_list_x[i], points_list_y[i]))
        return points_list

    def _get_arr_of_StandartPolygons(self,BoolOberationresult_polygon):
        array_of_polygons = []
        new_derivative_layer = Layer()
        #print(BoolOberationresult_polygon)
        if (BoolOberationresult_polygon.type == "Polygon"):
            array_of_polygons.append(StandartPolygon(self._get_list_of_points_from_polynom(BoolOberationresult_polygon),isDerivative=True,Layer=new_derivative_layer))
        elif (BoolOberationresult_polygon.type == "MultiPolygon"):
            for i in range(len(BoolOberationresult_polygon)):
                array_of_polygons.append(
                    StandartPolygon(self._get_list_of_points_from_polynom(BoolOberationresult_polygon[i]),isDerivative=True,Layer=new_derivative_layer))
        else:
            return None

        return array_of_polygons

class CheckBlockDRC:
    def isPoly_pass_width_check(self,PolygonObj,check_width_size,isVertical_check = True):
        bounds = PolygonObj.get_poly().bounds
        width = bounds[2]-bounds[0] if (True == isVertical_check) else bounds[3]-bounds[1]
        return True if (width<=check_width_size) else False

    def isPoly_pass_spacing_ckeck(self,PolygonObj1,PolygonObj2,spacing_size,isVertical_check = True):
        spacings = self.__get_spacings(PolygonObj1.get_poly().bounds,PolygonObj2.get_poly().bounds,isVertical_check)
        return True if (spacing_size.first<=spacing_size) and (spacing_size.second<=spacing_size) else False

    def isPoly_pass_enclosure_ckeck(self, PolygonObj1, PolygonObj2, enclosure_size):
        for i in range(4):
            if (PolygonObj1.get_poly().bounds[i]-PolygonObj2.get_poly().bounds[i]>enclosure_size): return False
        return True

    def __get_spacings(self,first_poly_bounds,second_poly_bounds,isVertical_check=True):

        if (True == isVertical_check):
            spacings = (first_poly_bounds[0]-second_poly_bounds[2],first_poly_bounds[2]-second_poly_bounds[0])
        else:
            spacings = (first_poly_bounds[1] - second_poly_bounds[3], first_poly_bounds[3] - second_poly_bounds[1])
        return spacings

class LayerCompareAnylizeBlock(BooleanOperationsBlock):
    def get_gates_arr_with_width_check(self,First_layer,Second_Layer,check_width_size):
        polygon_arr = self.get_polygon_arr_two_layers_intersection(First_Layer=First_layer, Second_Layer=Second_Layer)
        filtered_poly_arr = self.get_polygon_arr_with_width_check(polygon_arr,check_width_size)
        return self.get_Gate_arr_from_poly_arr(poly_arr=filtered_poly_arr, FirstLayer=First_layer, Second_Layer=Second_Layer)

    def get_polygon_arr_two_layers_intersection(self,First_Layer,Second_Layer):
        first_layer_polygon_arr = First_Layer.get_polygon_array_belong_layer()
        second_layer_polygon_arr = Second_Layer.get_polygon_array_belong_layer()
        intersection_polygon_arr = []
        for i in range(first_layer_polygon_arr):
            for j in range(second_layer_polygon_arr):
                result_of_intersect_two_polygons_arr = self._get_resulting_polygon_arr_from_operation_AND(first_layer_polygon_arr[i],second_layer_polygon_arr[j])
                if (None != result_of_intersect_two_polygons_arr):intersection_polygon_arr.extend(result_of_intersect_two_polygons_arr)
        return intersection_polygon_arr

    def get_polygon_arr_with_width_check(self,poly_arr,width_size):
        filtered_poly_arr = []
        for i in range(len(poly_arr)):
            bounds = poly_arr[i].get_poly().bounds
            if((bounds[2]-bounds[0])<width_size) or ((bounds[3]-bounds[1])<width_size): filtered_poly_arr.append(poly_arr[i])
        return filtered_poly_arr

    def get_Gate_arr_from_poly_arr(self,poly_arr,FirstLayer = None,SecondLayer = None):
        new_derivative_layer_for_gates = Layer()
        gate_arr = []
        for i in range(len(poly_arr)):
            gate_arr.append(Gate(poly_arr[i].get_array_of_dots),new_derivative_layer_for_gates,FirstLayer,SecondLayer)
        return gate_arr




if __name__ == "__main__":

    #Task1
    poly1 = StandartPolygon([(0,2),(10,2),(10,4),(0,4)])
    poly2 = StandartPolygon([(4, 0), (6, 0), (6, 10), (4, 10)])
    BooleanOperationsBlockObj = BooleanOperationsBlock()
    polyres1 = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_AND(poly1,poly2)[0]
    polyres2 = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_OR(poly1, poly2)[0]
    result = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_NOT_OR(polyres2, polyres1)
    for i in range(len(result)):
        print(BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_NOT_OR(polyres2, polyres1)[i].get_array_of_dots())

    print(poly1.get_poly().bounds)

    #q = Polygon([(0, 0), (4, 0), (4, 4), (0, 4)])
    # q = Polygon([(0,0),(4,0),(4,4),(0,4)])
    # p = Polygon([(5, 5), (10, 5), (10, 10), (5, 10)])
    # print(p.intersection(q).is_empty)


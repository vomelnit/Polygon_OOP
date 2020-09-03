from StandartPolygonClass import *
from LayerClass import *

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
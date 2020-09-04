from StandartPolygonClass import *
from LayerClass import *

class BooleanOperationsBlock:

    def get_resulting_polygon_arr_from_operation_OR(self, First_PolygonObj, Second_PolygonObj,DrawSpaceObj):
        Union_result_polygom = First_PolygonObj.get_poly().union(Second_PolygonObj.get_poly())
        return self._get_arr_of_StandartPolygons(Union_result_polygom,DrawSpaceObj)

    def get_resulting_polygon_arr_from_operation_AND(self, First_PolygonObj, Second_PolygonObj,DrawSpaceObj):
        if (First_PolygonObj.get_poly().intersects(Second_PolygonObj.get_poly())):
            Intersection_result_polygom = First_PolygonObj.get_poly().intersection(Second_PolygonObj.get_poly())
            return self._get_arr_of_StandartPolygons(Intersection_result_polygom,DrawSpaceObj)
        else:
            return []

    def get_resulting_polygon_arr_from_operation_NOT_OR(self, First_PolygonObj, Second_PolygonObj,DrawSpaceObj):
        Difference_result_polygom = First_PolygonObj.get_poly().difference(Second_PolygonObj.get_poly())
        if Difference_result_polygom.is_empty: return []
        return self._get_arr_of_StandartPolygons(Difference_result_polygom,DrawSpaceObj)


    def _get_list_of_points_from_polynom(self, Polynom):
        points_list_x, points_list_y = Polynom.exterior.coords.xy
        points_list = []
        for i in range(len(points_list_x)):
            points_list.append((points_list_x[i], points_list_y[i]))
        return points_list

    def _get_arr_of_StandartPolygons(self,BoolOberationResult_polygon,DrawSpaceObj):
        array_of_polygons = []
        new_derivative_layer = Layer(DrawSpaceObj)
        if (BoolOberationResult_polygon.type == "Polygon"):
            array_of_polygons.append(StandartPolygon(self._get_list_of_points_from_polynom(BoolOberationResult_polygon),isDerivative=True,Layer=new_derivative_layer))
        elif (BoolOberationResult_polygon.type == "MultiPolygon"):
            for i in range(len(BoolOberationResult_polygon)):
                array_of_polygons.append(
                    StandartPolygon(self._get_list_of_points_from_polynom(BoolOberationResult_polygon[i]),isDerivative=True,Layer=new_derivative_layer))
        else:
            return None

        return array_of_polygons
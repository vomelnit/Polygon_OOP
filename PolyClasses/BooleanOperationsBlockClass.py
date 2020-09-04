##@package BooleanOperationsBlockClass
#Consist of BooleanOperationsBlock class definition
from PolyClasses.StandartPolygonClass import *
from PolyClasses.LayerClass import *

##This class create BooleanOperationsBlock objects
#
#Realize boolean operations AND, OR, NOT_OR between two StandartPolygon objects
class BooleanOperationsBlock:

    ##  Return array of StandartPolygon objects that was result of OR operation between First_PolygonObj and Second_PolygonObj
    #   @param self The object pointer
    #   @param First_PolygonObj StandartPolygon object
    #   @param Second_PolygonObj StandartPolygon object
    #   @param DrawSpaceObj DrawSpace object
    #   @return array of StandartPolygon objects
    def get_resulting_polygon_arr_from_operation_OR(self, First_PolygonObj, Second_PolygonObj,DrawSpaceObj):
        Union_result_polygom = First_PolygonObj.get_poly().union(Second_PolygonObj.get_poly())
        return self._get_arr_of_StandartPolygons(Union_result_polygom,DrawSpaceObj)

    ##  Return array of StandartPolygon objects that was result of AND operation between First_PolygonObj and Second_PolygonObj
    #   @param self The object pointer
    #   @param First_PolygonObj StandartPolygon object
    #   @param Second_PolygonObj StandartPolygon object
    #   @param DrawSpaceObj DrawSpace object
    #   @return array of StandartPolygon objects
    def get_resulting_polygon_arr_from_operation_AND(self, First_PolygonObj, Second_PolygonObj,DrawSpaceObj):
        if (First_PolygonObj.get_poly().intersects(Second_PolygonObj.get_poly())):
            Intersection_result_polygom = First_PolygonObj.get_poly().intersection(Second_PolygonObj.get_poly())
            return self._get_arr_of_StandartPolygons(Intersection_result_polygom,DrawSpaceObj)
        else:
            return []

    ##  Return array of StandartPolygon objects that was result of NOT_OR operation between First_PolygonObj and Second_PolygonObj
    #   @param self The object pointer
    #   @param First_PolygonObj StandartPolygon object
    #   @param Second_PolygonObj StandartPolygon object
    #   @param DrawSpaceObj DrawSpace object
    #   @return array of StandartPolygon objects
    def get_resulting_polygon_arr_from_operation_NOT_OR(self, First_PolygonObj, Second_PolygonObj,DrawSpaceObj):
        Difference_result_polygom = First_PolygonObj.get_poly().difference(Second_PolygonObj.get_poly())
        if Difference_result_polygom.is_empty: return []
        return self._get_arr_of_StandartPolygons(Difference_result_polygom,DrawSpaceObj)

    ##  Return array of (x,y) points of shapely pachage Polygon object
    #   @param self The object pointer
    #   @param polygon shapely.geometry.Polygon object
    #   @return array of (x,y)
    def _get_list_of_points_from_polygon(self, polygon):
        points_list_x, points_list_y = polygon.exterior.coords.xy
        points_list = []
        for i in range(len(points_list_x)):
            points_list.append((points_list_x[i], points_list_y[i]))
        return points_list

    ##  Return array of StandartPolygon objects that was result of shapely pachage Polygon class method
    #   @param self The object pointer
    #   @param BoolOberationResult_polygon shapely.geometry.Polygon object
    #   @param DrawSpaceObj DrawSpace object
    #   @return array of StandartPolygon objects
    def _get_arr_of_StandartPolygons(self,BoolOberationResult_polygon,DrawSpaceObj):
        array_of_polygons = []
        new_derivative_layer = Layer(DrawSpaceObj)
        if (BoolOberationResult_polygon.type == "Polygon"):
            array_of_polygons.append(StandartPolygon(self._get_list_of_points_from_polygon(BoolOberationResult_polygon),isDerivative=True,Layer=new_derivative_layer))
        elif (BoolOberationResult_polygon.type == "MultiPolygon"):
            for i in range(len(BoolOberationResult_polygon)):
                array_of_polygons.append(
                    StandartPolygon(self._get_list_of_points_from_polygon(BoolOberationResult_polygon[i]),isDerivative=True,Layer=new_derivative_layer))
        else:
            return None

        return array_of_polygons
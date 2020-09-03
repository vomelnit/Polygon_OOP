from shapely.geometry import Polygon
from StandartPolygonClass import *
from DrawSpaceClass import *
from LayerClass import *
from BooleanOperationsBlockClass import *
from GUIPolygonCreatorClass import *

if __name__ == "__main__":

    #Task1
    Draw = DrawSpace(1000,1000)
    Lay = Layer(Draw)
    poly1 = StandartPolygon([(0,2),(10,2),(10,4),(0,4)],Lay)
    poly2 = StandartPolygon([(4, 0), (6, 0), (6, 10), (4, 10)])
    BooleanOperationsBlockObj = BooleanOperationsBlock()
    polyres1 = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_AND(poly1,poly2)[0]
    polyres2 = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_OR(poly1, poly2)[0]
    result = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_NOT_OR(polyres2, polyres1)
    for i in range(len(result)):
        print(BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_NOT_OR(polyres2, polyres1)[i].get_array_of_dots())

    GUI = GUIPolygonCreator()
    GUI.run(Draw)




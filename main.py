from shapely.geometry import Polygon
from StandartPolygonClass import *
from DrawSpaceClass import *
from LayerClass import *
from BooleanOperationsBlockClass import *
from GUIPolygonCreatorClass import *
from CheckBlockDRCClass import *
from LayerCompareAnylizeBlockClass import *

def Task1(polygon1,polygon2,DrawSpace):
    BooleanOperationsBlockObj = BooleanOperationsBlock()
    polyANDresultArr = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_AND(polygon1, polygon2, DrawSpace)
    print("Resulting polygons of AND operation:")
    for x in polyANDresultArr:
        print(x.get_array_of_dots())
    polyORresultArr = BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_OR(polygon1, polygon2, DrawSpace)
    print("Resulting polygons of OR operation:")
    for x in polyORresultArr:
        print(x.get_array_of_dots())
    if 0 == len(polyANDresultArr): return polyORresultArr
    finalPolyArr = []
    print("Resulting polygons of last operation:")
    for polyOR in polyORresultArr:
        for polyAND in  polyANDresultArr:
            for resultingPolygon in BooleanOperationsBlockObj.get_resulting_polygon_arr_from_operation_NOT_OR(polyOR, polyAND,DrawSpace):
                print(resultingPolygon.get_array_of_dots())
                finalPolyArr.append(resultingPolygon)
    return finalPolyArr

def Task2(poly1,poly2,widthCheck,SpacingCheck,EnclosureCheck):
    CheckBlockDRCObj = CheckBlockDRC()
    print("Check if polygon's width (x axis) less that <widthCheck> value:")
    print(CheckBlockDRCObj.isPolygonWidthLessThanCheckValue(PolygonObj=poly1,check_width_size=widthCheck,isVertical_check=True))
    print("Check if polygon1 and polygon2 distance (y axis) less that <SpacingCheck> value:")
    print(CheckBlockDRCObj.isPolysSpacingLessThanCheckValue(PolygonObj1=poly1,PolygonObj2=poly2,spacing_size=SpacingCheck,isVertical_check=False))
    print("Check if polygon2 enclose distanse to polygon1 by all sides less that <EnclosureCheck> value:")
    print(CheckBlockDRCObj.isPolysEnclosureByAllSidesLessThanCheckValue(PolygonObj1=poly1,PolygonObj2=poly2,enclosure_size=EnclosureCheck))
    print("Check if polygon2 enclose distanse to polygon1 by Bottom side less that <EnclosureCheck> value:")
    print(CheckBlockDRCObj.isPolysEnclosureByOneSidesLessThanCheckValue(PolygonObj1=poly1,PolygonObj2=poly2,enclosure_size=EnclosureCheck,checkSide="Bottom"))


def Task3(Layer1,Layer2,gateWidth):
    LayerCompareAnylizeBlockObj = LayerCompareAnylizeBlock()
    gateArray = LayerCompareAnylizeBlockObj.get_gates_arr_with_width_check(Layer1,Layer2,gateWidth)
    print("Gates points:")
    for x in gateArray:
        print(x.get_array_of_dots())

def Task4(DrawSpace):
    GUI = GUIPolygonCreator()
    GUI.run(Draw)

if __name__ == "__main__":

    #Task1
    print("TASK 1\n")
    Draw = DrawSpace(width=1000,height=1000)
    Layer1 = Layer(DrawSpace=Draw)
    poly1 = StandartPolygon(array_of_dots =[(0,2),(10,2),(10,4),(0,4)],Layer=Layer1)
    poly2 = StandartPolygon(array_of_dots =[(4, 0), (6, 0), (6, 10), (4, 10)],Layer=Layer1)
    Task1Polygon = Task1(poly1,poly2,Draw)


    #Task2
    print("TASK 2\n")
    Task2(poly1,poly2,4,2,1)
    print("\nTASK 2 END")

    #Task 3
    print("TASK 3\n")
    Layer2 = Layer(DrawSpace=Draw)
    poly3 = StandartPolygon(array_of_dots = [(0, 1), (10, 1), (10, 4), (0, 4)], Layer=Layer2)
    poly4 = StandartPolygon(array_of_dots = [(5.5, 0), (6, 0), (6, 10), (5.5, 10)], Layer=Layer2)
    Task3(Layer1=Layer1,Layer2=Layer2,gateWidth=1)
    print("\nTASK 3 END")

    #Task4
    Task4(Draw)



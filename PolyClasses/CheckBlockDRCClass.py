##@package CheckBlockDRCClass
#Consist of CheckBlockDRC class definition

##This class create CheckBlockDRC objects
#
#Realize Standard DRC Checks: width of polygon check, spacing between polygons check, enclosure between polygons check
class CheckBlockDRC:

    ##  Return True if PolygonObj size not bigger than check_width_size and if isVertical_check is True check width of polygon
    #   And if isVertical_check is False check height of polygon
    #   @param self The object pointer
    #   @param PolygonObj StandartPolygon object
    #   @param check_width_size float
    #   @param isVertical_check Bool
    #   @return Bool
    def isPolygonWidthLessThanCheckValue(self,PolygonObj,check_width_size,isVertical_check = True):
        bounds = PolygonObj.get_poly().bounds
        width = bounds[2]-bounds[0] if (True == isVertical_check) else bounds[3]-bounds[1]
        return True if (width<=check_width_size) else False

    ##  Return True if PolygonObjs spacing between each other not bigger than <spacing_size>
    #   And if <isVertical_check> is True check width of polygon
    #   And if <isVertical_check> is False check height of polygon
    #   @param self The object pointer
    #   @param PolygonObj1 StandartPolygon object
    #   @param PolygonObj2 StandartPolygon object
    #   @param spacing_size float
    #   @param isVertical_check Bool
    #   @return Bool
    def isPolysSpacingLessThanCheckValue(self,PolygonObj1,PolygonObj2,spacing_size,isVertical_check = True):
        spacings = self.__get_spacings(PolygonObj1.get_poly().bounds,PolygonObj2.get_poly().bounds,isVertical_check)
        return True if (spacings[0]<=spacing_size) and (spacings[1]<=spacing_size) else False

    ##  Return True if <PolygonObj1> enclosure by all 4 bounds to <PolygonObj1>  not bigger than <enclosure_size>
    #   @param self The object pointer
    #   @param PolygonObj1 StandartPolygon object
    #   @param PolygonObj2 StandartPolygon object
    #   @param enclosure_size float
    #   @return Bool
    def isPolysEnclosureByAllSidesLessThanCheckValue(self, PolygonObj1, PolygonObj2, enclosure_size):
        for i in range(4):
            if (PolygonObj1.get_poly().bounds[i]-PolygonObj2.get_poly().bounds[i]>enclosure_size): return False
        return True

    ##  Return True if <PolygonObj1> enclosure by <checkSide> to <PolygonObj1>  not bigger than <enclosure_size>
    #   @param self The object pointer
    #   @param PolygonObj1 StandartPolygon object
    #   @param PolygonObj2 StandartPolygon object
    #   @param enclosure_size float
    #   @param checkSide string
    #   @return Bool
    def isPolysEnclosureByOneSidesLessThanCheckValue(self, PolygonObj1, PolygonObj2, enclosure_size, checkSide):
        aviableSides = ["Left","Top","Right","Bottom"]
        checkResult = None
        for side in aviableSides:
            if checkSide == side:
                checkResult = (PolygonObj1.get_poly().bounds[aviableSides.index(checkSide)]-PolygonObj2.get_poly().bounds[aviableSides.index(checkSide)]>enclosure_size)
        if checkResult is None: raise Exception("Cannot get bounds at side '{1}'",format(checkSide))
        return checkResult

    ##  Return spacings beetween two polygons' bounds in format (x,y)
    #   @param self The object pointer
    #   @param first_poly_bounds array of float (4 elements)
    #   @param second_poly_bounds array of float (4 elements)
    #   @param isVertical_check float
    #   @return tuple
    def __get_spacings(self,first_poly_bounds,second_poly_bounds,isVertical_check=True):
        if (True == isVertical_check):
            spacings = (first_poly_bounds[0]-second_poly_bounds[2],first_poly_bounds[2]-second_poly_bounds[0])
        else:
            spacings = (first_poly_bounds[1] - second_poly_bounds[3], first_poly_bounds[3] - second_poly_bounds[1])
        return spacings

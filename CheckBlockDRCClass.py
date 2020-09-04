
class CheckBlockDRC:
    def isPolygonWidthLessThanCheckValue(self,PolygonObj,check_width_size,isVertical_check = True):
        bounds = PolygonObj.get_poly().bounds
        width = bounds[2]-bounds[0] if (True == isVertical_check) else bounds[3]-bounds[1]
        return True if (width<=check_width_size) else False


    def isPolysSpacingLessThanCheckValue(self,PolygonObj1,PolygonObj2,spacing_size,isVertical_check = True):
        spacings = self.__get_spacings(PolygonObj1.get_poly().bounds,PolygonObj2.get_poly().bounds,isVertical_check)
        return True if (spacings[0]<=spacing_size) and (spacings[1]<=spacing_size) else False

    def isPolysEnclosureByAllSidesLessThanCheckValue(self, PolygonObj1, PolygonObj2, enclosure_size):
        for i in range(4):
            if (PolygonObj1.get_poly().bounds[i]-PolygonObj2.get_poly().bounds[i]>enclosure_size): return False
        return True

    def isPolysEnclosureByOneSidesLessThanCheckValue(self, PolygonObj1, PolygonObj2, enclosure_size, checkSide):
        aviableSides = ["Left","Top","Right","Bottom"]
        checkResult = None
        for side in aviableSides:
            if checkSide == side:
                checkResult = (PolygonObj1.get_poly().bounds[aviableSides.index(checkSide)]-PolygonObj2.get_poly().bounds[aviableSides.index(checkSide)]>enclosure_size)
        if checkResult is None: raise Exception("Cannot get bounds at side '{1}'",format(checkSide))
        return checkResult

    def __get_spacings(self,first_poly_bounds,second_poly_bounds,isVertical_check=True):

        if (True == isVertical_check):
            spacings = (first_poly_bounds[0]-second_poly_bounds[2],first_poly_bounds[2]-second_poly_bounds[0])
        else:
            spacings = (first_poly_bounds[1] - second_poly_bounds[3], first_poly_bounds[3] - second_poly_bounds[1])
        return spacings
